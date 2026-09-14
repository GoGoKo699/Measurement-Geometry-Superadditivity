#!/usr/bin/env python3
"""Check current scientific identities without replaying editorial history.

This checks bytes, scientific source relationships and independent verifier
boundaries. It does not run the entropy proof or certify its mathematics.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import re
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
INVENTORY = "integrity/SCIENTIFIC_FILES.json"
INVENTORY_SHA256 = "3e47d6aaf143321ed7f77be58a4ecf4fa4cd628f71d0af0952b9edfd9fc34b2b"
FILE_KEYS_SHA256 = "b22e5286ac29b8b7e7ea4b9c9fb52141e45073c9b5c672267643244374515484"
PROTECTED_FILE_COUNT = 174
ADDITIONAL_FILES = frozenset({
    "CITATION.cff",
    "LICENSES/CC-BY-4.0.txt",
    "LICENSES/DejaVu.txt",
    "LICENSES/MIT.txt",
    "LICENSES/STIX.txt",
    "reader/assets/figure_01_channel_and_witness.svg",
    "reader/assets/figure_02_guaranteed_region.svg",
    "reader/assets/figure_03_coplanar_limit.svg",
    "website/learning_bridge.json",
    "website/palette.json",
})


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, "Duplicate JSON key: " + key)
        result[key] = value
    return result


def decode_json(raw):
    try:
        return json.loads(raw, object_pairs_hook=unique_object)
    except (json.JSONDecodeError, UnicodeDecodeError) as error:
        raise ValueError("Malformed integrity JSON") from error


def file_path(root, relative):
    require(isinstance(relative, str) and bool(relative), "Malformed protected path")
    path = PurePosixPath(relative)
    require(
        bool(path.parts)
        and not path.is_absolute()
        and path.as_posix() == relative
        and "\\" not in relative
        and all(part not in {".", ".."} for part in path.parts),
        "Malformed protected path: " + relative,
    )
    target = root
    for part in path.parts:
        target = target / part
        require(not target.is_symlink(), "Symlink in protected path: " + relative)
    require(target.is_file(), "Missing protected file: " + relative)
    return target


def load_inventory(root):
    raw = file_path(root, INVENTORY).read_bytes()
    record = decode_json(raw)
    require(isinstance(record, dict) and set(record) == {"schema_version", "scope", "files"},
            "Malformed scientific inventory fields")
    require(type(record["schema_version"]) is int and record["schema_version"] == 1,
            "Unexpected scientific inventory version")
    require(isinstance(record["scope"], str) and bool(record["scope"].strip()),
            "Malformed scientific inventory scope")
    entries = record["files"]
    require(isinstance(entries, dict), "Malformed scientific inventory files")
    for relative, expected in entries.items():
        # Validate paths before opening any member named in the inventory.
        path = PurePosixPath(relative)
        require(bool(relative) and bool(path.parts) and not path.is_absolute()
                and path.as_posix() == relative and "\\" not in relative
                and all(part not in {".", ".."} for part in path.parts),
                "Malformed protected path: " + relative)
        require(isinstance(expected, str) and re.fullmatch(r"[0-9a-f]{64}", expected),
                "Malformed protected digest: " + relative)
    keys_digest = digest(json.dumps(sorted(entries), separators=(",", ":")).encode())
    require(len(entries) == PROTECTED_FILE_COUNT and keys_digest == FILE_KEYS_SHA256,
            "Scientific inventory path coverage changed")
    require(digest(raw) == INVENTORY_SHA256, "Scientific inventory identity mismatch")
    return entries


def check_current_manifest(root, entries):
    record = decode_json(file_path(root, "BASELINE_MANIFEST.json").read_bytes())
    require(isinstance(record, dict) and isinstance(record.get("files"), dict),
            "Malformed current manifest")
    current = record["files"]
    scientific = set(entries) - ADDITIONAL_FILES
    require(set(current) == scientific | {"README.md", "STATUS.md"},
            "Current manifest path coverage changed")
    for relative in scientific:
        require(current[relative] == entries[relative],
                "Current manifest scientific identity changed: " + relative)
    # verify.py checks the current README/STATUS bytes. Their historical values
    # are deliberately not a dependency of this scientific identity check.
    return len(scientific)


def check(root=ROOT):
    root = Path(root)
    require(root.is_dir() and not root.is_symlink(), "Invalid integrity root")
    entries = load_inventory(root)
    for relative, expected in entries.items():
        require(digest(file_path(root, relative).read_bytes()) == expected,
                "Protected scientific artifact changed: " + relative)
    manifest_count = check_current_manifest(root, entries)

    # Import the existing helper only after verifying its protected bytes.
    spec = importlib.util.spec_from_file_location(
        "measurement_scientific_baseline", root / "baseline_tools.py")
    require(spec is not None and spec.loader is not None, "Cannot load scientific integrity helper")
    baseline = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(baseline)
    provenance = baseline.check_provenance(root)
    approved = baseline.check_protected(root)
    require(approved == 27, "Approved graphical artifact coverage changed")
    baseline.check_inputs(root)
    baseline.code_boundaries(root)
    reader_svgs = [p for p in entries if p.startswith("reader/assets/") and p.endswith(".svg")]
    require(len(reader_svgs) == 3, "Accepted reader figure coverage changed")
    return {
        "passed": True,
        "protected_files": len(entries),
        "current_manifest_scientific_entries": manifest_count,
        "approved_graphical_artifacts_unchanged": approved,
        "accepted_reader_svgs_unchanged": len(reader_svgs),
        "scientific_provenance": provenance,
        "independent_verifier_boundaries": True,
        "scope": "Current artifact identity and scientific dependency checks; not mathematical proof verification.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.output is not None:
        require(not args.output.exists() and not args.output.is_symlink(),
                "Use a fresh integrity output path")
    result = check()
    rendered = json.dumps(result, indent=2) + "\n"
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("x", encoding="utf-8") as stream:
            stream.write(rendered)
    print(rendered, end="")


if __name__ == "__main__":
    main()
