#!/usr/bin/env python3
"""Read two pinned historical Git blobs without extracting or executing a ZIP.

This bounded structural and credential-pattern inspection is not permission to
publish history, a malware scan, or a determination of third-party rights.
Only Python's standard library and the local Git object database are used.
"""
from __future__ import annotations

import argparse
import binascii
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import platform
import re
import stat
import struct
import subprocess
import sys
import zipfile
import zlib

OBJECTS = {
    "baseline.zip": ("f4442ae622a7d96a2346c66acedcea54783a598f", 2540928),
    "figure.png": ("0bac8266cbd5495b9b3a3ef7eecfd642b347af6d", 85639),
}
LIMITS = {
    "zip_members": 5000,
    "zip_member_bytes": 64 * 1024 * 1024,
    "zip_total_bytes": 256 * 1024 * 1024,
    "zip_compression_ratio": 1000,
    "png_metadata_bytes": 8 * 1024 * 1024,
    "png_pixels": 100_000_000,
}
PATTERNS = {
    "private_key": r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----",
    "github_token": r"\b(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,})\b",
    "aws_key": r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b",
    "api_key": r"\bsk-(?:proj-|svcacct-)?[A-Za-z0-9_-]{24,}\b",
    "slack_token": r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b",
    "signed_url": r"https?://[^\s<>\"']+[?&](?:sig|X-Amz-Signature|token)=[A-Za-z0-9%+/_-]{12,}",
    "credential_url": r"https?://[^\s/@:]+:[^\s/@]+@",
}


class InspectionError(ValueError):
    """A failed or unsupported inspection obligation."""


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def validate_git_blob(data: bytes, oid: str, expected_size: int) -> None:
    if len(data) != expected_size:
        raise InspectionError("Git blob byte count differs from the pinned size")
    actual = hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()
    if actual != oid:
        raise InspectionError("Git blob identity differs from the pinned object")


def read_git_blob(repo: Path, name: str) -> bytes:
    if name not in OBJECTS:
        raise InspectionError("Only the two pinned objects may be read")
    oid, size = OBJECTS[name]

    def git(*args: str) -> bytes:
        result = subprocess.run(["git", "-C", str(repo), "cat-file", *args],
                                capture_output=True, check=False, timeout=30)
        if result.returncode:
            raise InspectionError(f"Pinned object {oid} is unavailable to git cat-file")
        return result.stdout

    if git("-t", oid).strip() != b"blob":
        raise InspectionError("Pinned object is not a Git blob")
    if git("-s", oid).strip() != str(size).encode():
        raise InspectionError("Git blob size differs from the pinned size")
    data = git("blob", oid)
    validate_git_blob(data, oid, size)
    return data


def credential_candidates(text: str) -> list[dict]:
    """Emit only pattern names, one-based line numbers and counts, never values."""
    findings = []
    for kind, pattern in PATTERNS.items():
        lines: dict[int, int] = {}
        for match in re.finditer(pattern, text):
            line = text.count("\n", 0, match.start()) + 1
            lines[line] = lines.get(line, 0) + 1
        findings.extend({"type": kind, "line": line, "count": count}
                        for line, count in sorted(lines.items()))
    return findings


def validated_member_name(info: zipfile.ZipInfo) -> str:
    name = info.orig_filename
    if (not name or "\0" in name or "\\" in name or name.startswith("/")
            or re.match(r"^[A-Za-z]:", name)):
        raise InspectionError("ZIP contains an absolute, drive, NUL or backslash path")
    parts = name.removesuffix("/").split("/")
    if any(part in ("", ".", "..") for part in parts):
        raise InspectionError("ZIP contains a traversal or noncanonical path")
    mode = info.external_attr >> 16
    file_type = stat.S_IFMT(mode)
    if file_type not in (0, stat.S_IFREG, stat.S_IFDIR):
        raise InspectionError("ZIP contains a symlink or other special file")
    directories = parts if info.is_dir() else parts[:-1]
    prohibited = {"boundaryentanglingsusceptibility", "mytone"}
    if any(re.sub(r"[^a-z0-9]", "", part.lower()).startswith(project)
           for part in directories for project in prohibited):
        raise InspectionError("ZIP contains a separate prohibited-project subtree; no member content read")
    if info.flag_bits & (1 | 64):
        raise InspectionError("Encrypted ZIP members are unsupported")
    if info.compress_type not in (zipfile.ZIP_STORED, zipfile.ZIP_DEFLATED):
        raise InspectionError("ZIP member uses an unsupported compression method")
    if info.file_size < 0 or info.compress_size < 0:
        raise InspectionError("ZIP has an invalid declared member size")
    return "/".join(parts)


def compare_member(repo: Path, name: str, digest: str, prefix: str | None) -> dict:
    candidates = [name]
    if prefix and name.startswith(prefix + "/"):
        candidates.append(name[len(prefix) + 1:])
    root = repo.resolve()
    for candidate in candidates:
        current = root.joinpath(*PurePosixPath(candidate).parts)
        resolved = current.resolve()
        if not resolved.is_relative_to(root) or current.is_symlink():
            continue
        if current.is_file():
            current_hash = sha256(current.read_bytes())
            return {"status": "identical" if current_hash == digest else "changed",
                    "repository_path": candidate, "current_sha256": current_hash}
    return {"status": "unmatched"}


def inspect_zip(data: bytes, repo: Path, limits: dict | None = None) -> dict:
    bounds = LIMITS if limits is None else {**LIMITS, **limits}
    rows = []
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        infos = archive.infolist()
        if len(infos) > bounds["zip_members"]:
            raise InspectionError("ZIP exceeds the member-count ceiling")
        seen: set[str] = set()
        total = 0
        for info in infos:
            name = validated_member_name(info)
            if name in seen:
                raise InspectionError("ZIP contains duplicate normalized member paths")
            seen.add(name)
            total += info.file_size
            if info.file_size > bounds["zip_member_bytes"] or total > bounds["zip_total_bytes"]:
                raise InspectionError("ZIP exceeds an uncompressed-size ceiling")
            if info.file_size > max(1, info.compress_size) * bounds["zip_compression_ratio"]:
                raise InspectionError("ZIP exceeds the compression-ratio ceiling")
            if info.is_dir() and info.file_size:
                raise InspectionError("ZIP directory contains nonempty data")
        file_names = [i.filename for i in infos if not i.is_dir()]
        top = {name.split("/", 1)[0] for name in file_names}
        prefix = next(iter(top)) if len(top) == 1 and all("/" in n for n in file_names) else None
        for info in infos:
            # Reading through EOF makes zipfile verify the CRC. No member is extracted.
            with archive.open(info) as stream:
                content = stream.read(min(info.file_size, bounds["zip_member_bytes"]) + 1)
                if len(content) != info.file_size or stream.read(1):
                    raise InspectionError("ZIP member length differs from the central directory")
            if binascii.crc32(content) & 0xffffffff != info.CRC:
                raise InspectionError("ZIP member CRC mismatch")
            row = {"path": info.filename, "directory": info.is_dir(),
                   "bytes": len(content), "compressed_bytes": info.compress_size,
                   "crc32": f"{info.CRC:08x}", "sha256": sha256(content)}
            if not info.is_dir():
                row["comparison"] = compare_member(repo, info.filename, row["sha256"], prefix)
                try:
                    text = content.decode("utf-8")
                except UnicodeDecodeError:
                    row["text_scan"] = "not_utf8"
                    row["credential_candidates"] = []
                else:
                    # NUL-containing binary material is not classified as prose.
                    row["text_scan"] = "utf8_with_nul" if "\0" in text else "utf8"
                    row["credential_candidates"] = credential_candidates(text)
            rows.append(row)
    counts = {status: sum(r.get("comparison", {}).get("status") == status for r in rows)
              for status in ("identical", "changed", "unmatched")}
    return {"structure_and_crc": "passed", "member_count": len(rows),
            "uncompressed_bytes": total, "common_top_directory": prefix,
            "comparison_counts": counts, "members": rows,
            "credential_candidate_count": sum(f["count"] for r in rows for f in r.get("credential_candidates", [])),
            "scope": "No member extracted or executed. Binary member contents, rights and personal data require separate review."}


def bounded_inflate(data: bytes, limit: int) -> bytes:
    decoder = zlib.decompressobj()
    result = decoder.decompress(data, limit + 1)
    if len(result) > limit or decoder.unconsumed_tail:
        raise InspectionError("PNG metadata exceeds its decompression ceiling")
    if not decoder.eof or decoder.unused_data:
        raise InspectionError("PNG compressed metadata has a truncated or trailing stream")
    return result


def png_text(kind: bytes, payload: bytes) -> tuple[bytes, str]:
    if len(payload) > LIMITS["png_metadata_bytes"]:
        raise InspectionError("PNG text metadata exceeds its byte ceiling")
    if b"\0" not in payload:
        raise InspectionError("PNG text metadata lacks its keyword delimiter")
    key, rest = payload.split(b"\0", 1)
    if not 1 <= len(key) <= 79:
        raise InspectionError("PNG text keyword length is invalid")
    if kind == b"tEXt":
        return key, rest.decode("latin-1")
    if kind == b"zTXt":
        if not rest or rest[0] != 0:
            raise InspectionError("PNG text compression method is unsupported")
        return key, bounded_inflate(rest[1:], LIMITS["png_metadata_bytes"]).decode("latin-1")
    if len(rest) < 2 or rest[0] not in (0, 1) or rest[1] != 0:
        raise InspectionError("PNG international-text compression flags are invalid")
    flag, body = rest[0], rest[2:]
    fields = body.split(b"\0", 2)
    if len(fields) != 3:
        raise InspectionError("PNG international-text delimiters are missing")
    language, translated, body = fields
    language.decode("ascii")
    translated.decode("utf-8")
    if flag:
        body = bounded_inflate(body, LIMITS["png_metadata_bytes"])
    # Include all textual fields in the scan without reproducing their values.
    return key, "\n".join((language.decode("ascii"), translated.decode("utf-8"), body.decode("utf-8")))


def inspect_png(data: bytes) -> dict:
    if not data.startswith(b"\x89PNG\r\n\x1a\n"):
        raise InspectionError("PNG signature is invalid")
    offset, chunks, metadata = 8, [], []
    dimensions = None
    saw_idat, ended_idat, saw_iend = False, False, False
    while offset < len(data):
        if len(data) - offset < 12:
            raise InspectionError("PNG chunk header is truncated")
        length, kind = struct.unpack(">I4s", data[offset:offset + 8])
        end = offset + 12 + length
        if end > len(data) or not re.fullmatch(b"[A-Za-z]{4}", kind):
            raise InspectionError("PNG chunk bounds or type are invalid")
        payload = data[offset + 8:offset + 8 + length]
        expected_crc, = struct.unpack(">I", data[offset + 8 + length:end])
        if binascii.crc32(kind + payload) & 0xffffffff != expected_crc:
            raise InspectionError("PNG chunk CRC mismatch")
        if not chunks and kind != b"IHDR":
            raise InspectionError("PNG must start with IHDR")
        if kind == b"IHDR":
            if chunks or length != 13:
                raise InspectionError("PNG IHDR order or length is invalid")
            width, height, depth, color, compression, filtering, interlace = struct.unpack(">IIBBBBB", payload)
            allowed_depths = {0: (1, 2, 4, 8, 16), 2: (8, 16), 3: (1, 2, 4, 8), 4: (8, 16), 6: (8, 16)}
            if (not width or not height or width * height > LIMITS["png_pixels"]
                    or depth not in allowed_depths.get(color, ())
                    or compression != 0 or filtering != 0 or interlace not in (0, 1)):
                raise InspectionError("PNG dimensions or image parameters are invalid")
            dimensions = {"width": width, "height": height, "bit_depth": depth,
                          "color_type": color, "interlace": interlace}
        elif kind == b"IDAT":
            if ended_idat:
                raise InspectionError("PNG IDAT chunks are not contiguous")
            saw_idat = True
        elif saw_idat:
            ended_idat = True
        if kind[0] < 97 and kind not in (b"IHDR", b"PLTE", b"IDAT", b"IEND"):
            raise InspectionError("PNG has an unsupported critical chunk")
        if kind in (b"tEXt", b"zTXt", b"iTXt"):
            key, text = png_text(kind, payload)
            metadata.append({"chunk_index": len(chunks), "type": kind.decode(),
                             "keyword_sha256": sha256(key), "text_characters": len(text),
                             "credential_candidates": credential_candidates(key.decode("latin-1") + "\n" + text)})
        chunks.append({"type": kind.decode(), "bytes": length, "sha256": sha256(payload)})
        offset = end
        if kind == b"IEND":
            if length or offset != len(data) or not saw_idat:
                raise InspectionError("PNG IEND, image-data presence or trailing bytes are invalid")
            saw_iend = True
            break
    if not dimensions or not saw_iend:
        raise InspectionError("PNG lacks required terminal structure")
    return {"structure_and_crc": "passed", "image": dimensions, "chunks": chunks,
            "text_metadata": metadata,
            "credential_candidate_count": sum(f["count"] for row in metadata for f in row["credential_candidates"]),
            "pixel_decode": "not performed; separate visual inspection required",
            "opaque_ancillary_chunks": [c["type"] for c in chunks
                                        if c["type"][0].islower() and c["type"] not in ("tEXt", "zTXt", "iTXt")],
            "scope": "Text values withheld from the report. Pattern scanning does not clear personal metadata or third-party rights."}


def run(repo: Path, output: Path) -> dict:
    output.mkdir(parents=True, exist_ok=False)
    report = {"status": "failed", "python": sys.version.split()[0],
              "platform": platform.platform(), "limits": LIMITS,
              "credential_patterns": PATTERNS, "objects": {},
              "publication_clearance": False,
              "scope": "Two pinned Git blobs only; no network, archive execution or archive extraction."}
    try:
        for name, (oid, size) in OBJECTS.items():
            data = read_git_blob(repo, name)
            (output / name).write_bytes(data)
            item = {"git_blob": oid, "bytes": size, "sha256": sha256(data),
                    "byte_identity": "verified", "output_file": name}
            report["objects"][name] = item
            item["inspection"] = inspect_zip(data, repo) if name.endswith(".zip") else inspect_png(data)
        report["credential_candidate_count"] = sum(item["inspection"]["credential_candidate_count"]
                                                   for item in report["objects"].values())
        report["status"] = ("review_required_pattern_candidates" if report["credential_candidate_count"]
                            else "passed_bounded_inspection")
    except (InspectionError, zipfile.BadZipFile, RuntimeError, OSError, UnicodeError,
            zlib.error, subprocess.TimeoutExpired) as exc:
        # Do not include arbitrary archive content, subprocess output or matches.
        report["failure"] = {"type": type(exc).__name__,
                             "reason": str(exc) if isinstance(exc, InspectionError) else "Inspection failed; no clearance recorded"}
    (output / "REPORT.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, required=True, help="Fresh directory for original blobs and REPORT.json")
    args = parser.parse_args()
    try:
        report = run(args.repo, args.output)
    except FileExistsError:
        parser.error("--output must name a fresh directory")
    print(json.dumps({"status": report["status"], "report": str(args.output / "REPORT.json"),
                      "publication_clearance": False}))
    return 0 if report["status"] == "passed_bounded_inspection" else 1


if __name__ == "__main__":
    raise SystemExit(main())
