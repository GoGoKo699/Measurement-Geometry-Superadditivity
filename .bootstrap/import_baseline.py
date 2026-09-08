#!/usr/bin/env python3
"""Import only the approved v1 baseline after exact input-hash validation.

Accepts the original ZIP, a browser-uploaded project folder, or files already
at root. Never downloads data, edits scientific contents, merges or force-pushes.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import shutil
import stat
import subprocess
import tempfile
import zipfile

ARCHIVE = 'Measurement-Geometry-scientific-baseline-v1-2026-09-08.zip'
ARCHIVE_SHA = '087dbe4b1128a1494abc411415434df2c9a52aa5967053783779a041a32c8944'
PROJECT = 'Measurement-Geometry-Superadditivity'
MANIFEST_SHA = 'cc0ea1a941b746791162fd34a83b3419fa87dbe939baf0ff9a55384dcedef0ec'
GITIGNORE = b'.venv/\n__pycache__/\n.pytest_cache/\n*.py[cod]\nbuild/\n.DS_Store\n'

def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()

def safe_path(name: str) -> str:
    p = PurePosixPath(name)
    if not name or p.is_absolute() or '..' in p.parts or '\\' in name or '\x00' in name:
        raise ValueError('Unsafe path: ' + repr(name))
    if name != p.as_posix() or '.git' in p.parts:
        raise ValueError('Unexpected path: ' + repr(name))
    return name

def verify_payload(raw: dict[str, bytes]) -> dict:
    if 'BASELINE_MANIFEST.json' not in raw:
        raise ValueError('The scientific baseline manifest is missing')
    if digest(raw['BASELINE_MANIFEST.json']) != MANIFEST_SHA:
        raise ValueError('Not the approved baseline manifest')
    manifest = json.loads(raw['BASELINE_MANIFEST.json'])
    files = manifest['files']
    if len(files) != 165:
        raise ValueError('Unexpected baseline member count')
    # Some browser folder uploads omit hidden files. Restore this one exact,
    # already approved file rather than silently using a different ignore rule.
    if '.gitignore' not in raw:
        raw['.gitignore'] = GITIGNORE
    if set(raw) != set(files) | {'BASELINE_MANIFEST.json'}:
        raise ValueError('Unexpected or missing baseline files')
    for name, expected in files.items():
        safe_path(name)
        if digest(raw[name]) != expected:
            raise ValueError('Baseline file hash mismatch: ' + name)
    approved = json.loads(raw['provenance/APPROVED_FIGURE_HASHES.json'])['files']
    if len(approved) != 27:
        raise ValueError('Unexpected approved figure count')
    for name, expected in approved.items():
        if digest(raw[name]) != expected:
            raise ValueError('Approved figure differs: ' + name)
    return {'baseline_files': len(raw), 'manifest_entries': len(files),
            'approved_artifacts': len(approved), 'manifest_sha256': MANIFEST_SHA}

def read_payload(root: Path):
    archive = root / ARCHIVE
    removals = []
    if archive.is_file():
        if archive.is_symlink() or digest(archive.read_bytes()) != ARCHIVE_SHA:
            raise ValueError('Archive SHA-256 mismatch; refusing the import')
        raw = {}
        with zipfile.ZipFile(archive) as z:
            if z.testzip() is not None:
                raise ValueError('ZIP CRC failure')
            for info in z.infolist():
                name = info.filename.rstrip('/')
                safe_path(name)
                if stat.S_ISLNK(info.external_attr >> 16):
                    raise ValueError('Symlink in archive')
                if info.is_dir():
                    continue
                prefix = PROJECT + '/'
                if not name.startswith(prefix):
                    raise ValueError('Unexpected archive root')
                rel = safe_path(name[len(prefix):])
                if rel in raw:
                    raise ValueError('Duplicate archive path')
                raw[rel] = z.read(info)
        removals = [ARCHIVE]
        mode = 'approved archive'
    else:
        directory = root / PROJECT
        if directory.is_dir():
            raw = {}
            for p in directory.rglob('*'):
                if p.is_symlink():
                    raise ValueError('Symlink in uploaded folder')
                if p.is_file():
                    rel = safe_path(p.relative_to(directory).as_posix())
                    raw[rel] = p.read_bytes()
                    removals.append(p.relative_to(root).as_posix())
            mode = 'uploaded baseline directory'
        elif (root / 'BASELINE_MANIFEST.json').is_file():
            mraw = (root / 'BASELINE_MANIFEST.json').read_bytes()
            if digest(mraw) != MANIFEST_SHA:
                raise ValueError('Wrong root manifest')
            expected = json.loads(mraw)['files']
            raw = {'BASELINE_MANIFEST.json': mraw}
            for rel in expected:
                safe_path(rel)
                p = root / rel
                if p.is_symlink():
                    raise ValueError('Symlink in root files')
                if p.is_file():
                    raw[rel] = p.read_bytes()
            mode = 'uploaded files at repository root'
        else:
            raise FileNotFoundError('Upload the unchanged approved baseline ZIP first')
    checked = verify_payload(raw)
    return raw, removals, mode, checked

def prepare(root: Path):
    raw, removals, mode, checked = read_payload(root)
    # Validate the whole payload before changing any repository target.
    for rel, content in raw.items():
        target = root / rel
        if target.is_symlink() or any(p.is_symlink() for p in target.parents if p != root.parent):
            raise ValueError('Unsafe destination: ' + rel)
    for rel, content in raw.items():
        target = root / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(content)
        target.chmod(0o644)
    for rel in removals:
        (root / rel).unlink()
    folder = root / PROJECT
    if folder.is_dir():
        for p in sorted(folder.rglob('*'), key=lambda p: len(p.parts), reverse=True):
            if p.is_dir():
                p.rmdir()
        folder.rmdir()
    # This transient path list stages only approved baseline files and removals,
    # never workflow files, credentials, build products, or unrelated user files.
    stage = sorted(set(raw) | set(removals))
    bootstrap = root / '.bootstrap'
    bootstrap.mkdir(exist_ok=True)
    (bootstrap / 'stage-paths').write_bytes(b'\0'.join(p.encode() for p in stage) + b'\0')
    report = {'passed': True, 'input_mode': mode, 'source_archive_sha256': ARCHIVE_SHA,
              **checked, 'scientific_files_changed': False, 'main_modified': False,
              'note': 'Hash verification only; CI must execute mathematical and rendering checks separately.'}
    dest = root / 'build/import/TRANSFER_VERIFICATION.json'
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))
    return report

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path.cwd())
    args = parser.parse_args()
    prepare(args.root.resolve())
