"""Replay reader-only preservation checks without numerical evaluation or network."""
import argparse, hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PIN = 'f0015c56a19fd953c6797b2c64d9b507105234e3'
EDITABLE = {
    'README.md', 'STATUS.md', 'BASELINE_MANIFEST.json', 'WEBSITE.md',
    'website/build.py', 'website/check.py', 'website/repository_preview.py',
    'website/browser_check.py', 'website/site.json', 'website/editorial_map.json',
    'website/assets/site.js', 'reader/PREVIEW_MANIFEST.json',
}

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def check(root=ROOT):
    baseline = json.loads((root/'website/provenance/preskill_starting_manifest.json').read_text())
    assert baseline['commit'] == PIN
    unchanged, editorial = [], []
    for name, old in baseline['files'].items():
        current = digest(root/name)
        if current == old:
            unchanged.append(name)
            continue
        allowed = name in EDITABLE or name.startswith(('website/pages/', 'website/tests/'))
        allowed |= name.startswith('reader/') and name.endswith('.md')
        assert allowed, ('Protected starting artifact changed', name)
        editorial.append({'file': name, 'before_sha256': old, 'after_sha256': current})
    manifest = json.loads((root/'BASELINE_MANIFEST.json').read_text())
    for name in ('README.md', 'STATUS.md'):
        assert manifest['files'][name] == digest(root/name)
        manifest['files'][name] = baseline['files'][name]
    restored = (json.dumps(manifest, indent=2, ensure_ascii=False)+'\n').encode()
    assert hashlib.sha256(restored).hexdigest() == baseline['files']['BASELINE_MANIFEST.json'], 'Only root editorial identities may change in the manifest'
    protected = json.loads((root/'provenance/APPROVED_FIGURE_HASHES.json').read_text())['files']
    assert all(name in unchanged for name in protected)
    for prefix in ('docs/', 'verification/', 'numerics/', 'data/', 'evidence/', 'certificates/', 'provenance/', 'figures/'):
        assert all(name in unchanged for name in baseline['files'] if name.startswith(prefix)), prefix
    assert all(name in unchanged for name in baseline['files'] if name.startswith('reader/assets/'))
    return {'passed': True, 'starting_commit': PIN, 'starting_tree': baseline['tree'],
            'starting_files_checked': len(baseline['files']), 'unchanged_count': len(unchanged),
            'unchanged_files': unchanged, 'authorized_editorial_changes': editorial,
            'approved_original_graphics_unchanged': len(protected), 'accepted_reader_svgs_unchanged': 3,
            'root_manifest_changes': ['README.md identity', 'STATUS.md identity'],
            'science_recomputed': False, 'scope': 'Byte preservation and authorized editorial scope, not theorem correctness.'}

if __name__ == '__main__':
    parser = argparse.ArgumentParser();parser.add_argument('--output', type=Path)
    args = parser.parse_args();result = check()
    if args.output:
        assert not args.output.exists(), 'Use a fresh evidence output path'
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('unchanged_files', 'authorized_editorial_changes')}, indent=2))
