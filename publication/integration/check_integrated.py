#!/usr/bin/env python3
"""Check the authorized integration against the exact reviewed checkpoint.

This offline, standard-library-only identity check does not query GitHub or
certify scientific correctness, ownership or public clearance. Older checkers
and their results retain their original commit scopes. The reader build also
checks mathematical preservation and inverse documentary substitutions.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
START = "deba96a1a2fb3781a357a5d4d2660e6edda638da"
TREE = "1bbe9651bb1b524c2083df66374bc6a2464e6971"
INVENTORY_SHA256 = "d8c00b1d3d061d89260ad984b0982098a0e4f982ade04b1d69f5da6de1367234"
STAGE_PATHS = frozenset({
    "README.md", "STATUS.md", "WEBSITE.md", "PUBLICATION.md",
    "publication/READINESS.json", "website/pages/status.md",
    "website/pages/materials.md", "reader/status.md", "reader/materials.md",
    "reader/PREVIEW_MANIFEST.json", "BASELINE_MANIFEST.json", "website/build.py",
    ".github/workflows/reader-site.yml",
    ".github/workflows/historical-object-review.yml",
    ".github/workflows/integration-candidate.yml",
})
EDITS_PATH = "publication/integration/INTEGRATED_EDITS.json"
INVENTORY_PATH = "publication/integration/INTEGRATED_STARTING_FILES.json"
MANIFEST_ROOT_DOCUMENTS = ("README.md", "STATUS.md")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path):
    return json.loads(path.read_text())


def check(root=ROOT):
    root = Path(root).resolve()
    inventory_path = root / INVENTORY_PATH
    require(inventory_path.is_file() and not inventory_path.is_symlink(),
            "Integrated starting inventory missing or symlinked")
    require(digest(inventory_path) == INVENTORY_SHA256,
            "Integrated starting inventory changed")
    baseline = load(inventory_path)
    require(baseline["commit"] == START and baseline["tree"] == TREE,
            "Unexpected integrated comparison checkpoint")
    edits_path = root / EDITS_PATH
    require(edits_path.is_file() and not edits_path.is_symlink(),
            "Integrated edit record missing or symlinked")
    edits = load(edits_path)
    require(isinstance(edits, dict) and
            {"status", "starting_commit", "files"} <= set(edits),
            "Malformed integrated edit record")
    require(edits["status"] == "authorized_integration" and
            edits["starting_commit"] == START, "Integrated edit scope differs")
    changes = edits["files"]
    require(isinstance(changes, dict) and set(changes) <= STAGE_PATHS,
            "Unauthorized integrated edit path")
    require(set(changes) <= set(baseline["files"]),
            "Integrated edit has no checkpoint source")
    for name, entry in changes.items():
        require(isinstance(entry, dict) and
                set(entry) == {"before_sha256", "after_sha256"},
                "Malformed integrated edit: " + name)
        require(entry["before_sha256"] == baseline["files"][name],
                "Integrated starting hash differs: " + name)
        require(isinstance(entry["after_sha256"], str) and
                re.fullmatch(r"[0-9a-f]{64}", entry["after_sha256"]),
                "Malformed integrated after hash: " + name)
        require(entry["before_sha256"] != entry["after_sha256"],
                "No-op integrated edit: " + name)

    unchanged = []
    for name, before in baseline["files"].items():
        path = root / name
        require(path.is_file() and not path.is_symlink() and
                path.resolve().is_relative_to(root),
                "Starting file missing, symlinked or outside checkout: " + name)
        expected = changes[name]["after_sha256"] if name in changes else before
        require(digest(path) == expected, "Unrecorded integrated file change: " + name)
        if name not in changes:
            unchanged.append(name)

    # This checkpoint already includes the reviewed nine-file core correction.
    # Current stage prose may refresh exactly the two root document identities.
    # Restoring only those two entries must recover the entire earlier manifest.
    manifest = load(root / "BASELINE_MANIFEST.json")
    for name in MANIFEST_ROOT_DOCUMENTS:
        require(manifest["files"][name] == digest(root / name),
                "Current manifest does not identify " + name)
        manifest["files"][name] = baseline["files"][name]
    restored = (json.dumps(manifest, indent=2, ensure_ascii=False) + "\n").encode()
    require(hashlib.sha256(restored).hexdigest() ==
            baseline["files"]["BASELINE_MANIFEST.json"],
            "Manifest changes extend beyond README and STATUS identities")

    graphics = load(root / "provenance/APPROVED_FIGURE_HASHES.json")["files"]
    require(len(graphics) == 27, "Protected original graphical inventory differs")
    for name, expected in graphics.items():
        require(name in unchanged and digest(root / name) == expected,
                "Protected original graphic differs: " + name)
    reader_svgs = [name for name in baseline["files"]
                   if name.startswith("reader/assets/") and name.endswith(".svg")]
    require(len(reader_svgs) == 3 and all(name in unchanged for name in reader_svgs),
            "Accepted reader SVG inventory differs")

    readiness = load(root / "publication/READINESS.json")
    require(readiness["license_active"] is True,
            "Confirmed operative licenses must remain active")
    require(readiness["public_visibility_changed"] is False,
            "This integration check does not authorize public visibility")
    return {
        "passed": True,
        "scope": "Offline identity and bounded stage-change preservation; no live repository query, scientific proof check or public clearance",
        "starting_commit": START,
        "starting_tree": TREE,
        "starting_files_checked": len(baseline["files"]),
        "starting_files_byte_unchanged": len(unchanged),
        "recorded_stage_changes": sorted(changes),
        "protected_original_graphics": len(graphics),
        "accepted_reader_svgs_unchanged": len(reader_svgs),
        "historical_checkers_and_evidence_unchanged": True,
        "current_manifest_changes": list(MANIFEST_ROOT_DOCUMENTS),
        "full_science_recomputed_by_this_command": False,
        "live_merge_or_visibility_status_verified": False,
    }


def write_result(path, result):
    path = Path(path)
    require(not path.exists() and not path.is_symlink(), "Use a fresh result path")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x") as stream:
        stream.write(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = check()
    if args.output:
        write_result(args.output, result)
    print(json.dumps(result, indent=2))
