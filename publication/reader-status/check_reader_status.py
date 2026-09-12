#!/usr/bin/env python3
"""Check this reader-status edit and replay the unchanged integration checkpoint.

This standard-library-only check uses exact file identities and local snapshots.
It neither contacts GitHub nor establishes scientific correctness or publication
clearance. Historical checks run on their reconstructed historical scope, never
on rewritten approval records.
"""
import argparse
from contextlib import contextmanager
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import tempfile

ROOT = Path(__file__).resolve().parents[2]
START = "ba5fe59a31b7b833a458ee3761fbc9777d8c47e4"
TREE = "4adee205cbb23ff54b16094f0084593fa0c97aa0"
INVENTORY_PATH = "publication/reader-status/STARTING_FILES.json"
INVENTORY_SHA256 = "36ad73f305f838f5c4bd2f3845c11fd265c0ae686f2f34660a381a0309d1806c"
EDITS_PATH = "publication/reader-status/EDITS.json"
BEFORE_PATH = "publication/reader-status/BEFORE_TEXT.json"
HISTORICAL_CHECKER = "publication/integration/check_integrated.py"
STAGE_PATHS = frozenset({
    "README.md", "STATUS.md", "WEBSITE.md", "PUBLICATION.md",
    "publication/READINESS.json", "BASELINE_MANIFEST.json",
    "website/pages/index.md", "website/pages/status.md",
    "website/pages/materials.md", "website/pages/verification.md",
    "website/pages/background.md", "website/pages/visual-design.md",
    "website/build.py", "website/repository_preview.py",
    "website/site.json", "website/editorial_map.json",
    "reader/README.md", "reader/status.md", "reader/materials.md",
    "reader/verification.md", "reader/background.md", "reader/visual-design.md",
    "reader/channel.md", "reader/figures.md", "reader/limits.md",
    "reader/proof-guide.md", "reader/PREVIEW_MANIFEST.json",
    "website/tests/test_integrated_preservation.py",
    "website/tests/test_repository_preview.py",
    ".github/workflows/integration-candidate.yml",
    ".github/workflows/historical-object-review.yml",
})


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def read_file(root, name):
    path = root / name
    require(path.is_file() and not path.is_symlink() and
            path.resolve().is_relative_to(root),
            "File missing, symlinked or outside checkout: " + name)
    return path.read_bytes()


def load_file(root, name):
    return json.loads(read_file(root, name))


def validate_state(root):
    root = Path(root).resolve()
    inventory_bytes = read_file(root, INVENTORY_PATH)
    require(sha(inventory_bytes) == INVENTORY_SHA256,
            "Reader-status starting inventory changed")
    baseline = json.loads(inventory_bytes)
    require(baseline["commit"] == START and baseline["tree"] == TREE,
            "Unexpected reader-status checkpoint")
    edits = load_file(root, EDITS_PATH)
    require(isinstance(edits, dict) and
            {"status", "starting_commit", "files"} <= set(edits),
            "Malformed reader-status edit record")
    require(edits["status"] == "authorized_reader_status_cleanup" and
            edits["starting_commit"] == START, "Reader-status edit scope differs")
    changes = edits["files"]
    require(isinstance(changes, dict) and set(changes) <= STAGE_PATHS and
            set(changes) <= set(baseline["files"]),
            "Unauthorized reader-status edit path")
    before = load_file(root, BEFORE_PATH)
    require(isinstance(before, dict) and set(before) == set(changes),
            "Historical text snapshots do not cover the exact recorded edits")
    for name, entry in changes.items():
        require(isinstance(entry, dict) and
                set(entry) == {"before_sha256", "after_sha256"},
                "Malformed reader-status edit: " + name)
        require(entry["before_sha256"] == baseline["files"][name],
                "Reader-status starting hash differs: " + name)
        require(isinstance(entry["after_sha256"], str) and
                re.fullmatch(r"[0-9a-f]{64}", entry["after_sha256"]),
                "Malformed reader-status after hash: " + name)
        require(entry["before_sha256"] != entry["after_sha256"],
                "No-op reader-status edit: " + name)
        require(isinstance(before[name], str) and
                sha(before[name].encode("utf-8")) == entry["before_sha256"],
                "Historical text snapshot differs: " + name)
    for name, expected in baseline["files"].items():
        if name in changes:
            expected = changes[name]["after_sha256"]
        require(sha(read_file(root, name)) == expected,
                "Unrecorded reader-status file change: " + name)

    # Current integrity identities may follow the two edited root documents.
    # No scientific or other manifest entry may be refreshed in this stage.
    manifest = load_file(root, "BASELINE_MANIFEST.json")
    for name in ("README.md", "STATUS.md"):
        require(manifest["files"][name] == sha(read_file(root, name)),
                "Current manifest does not identify " + name)
        manifest["files"][name] = baseline["files"][name]
    restored = (json.dumps(manifest, indent=2, ensure_ascii=False) + "\n").encode()
    require(sha(restored) == baseline["files"]["BASELINE_MANIFEST.json"],
            "Manifest changes extend beyond README and STATUS identities")
    readiness = load_file(root, "publication/READINESS.json")
    require(readiness["license_active"] is True,
            "Confirmed operative licenses must remain active")
    require(readiness["public_visibility_changed"] is False,
            "Reader-status cleanup does not change public visibility")
    return root, baseline, changes, before


def restore_checkpoint(state, destination):
    """Materialize only the pinned checkpoint, with validated pre-edit bytes."""
    root, baseline, changes, before = state
    destination = Path(destination).resolve()
    require(destination != root and not destination.is_relative_to(root),
            "Historical reconstruction must be outside the checkout")
    require(not destination.exists() or
            (destination.is_dir() and not any(destination.iterdir())),
            "Historical reconstruction needs an empty destination")
    destination.mkdir(parents=True, exist_ok=True)
    for name in baseline["files"]:
        raw = before[name].encode("utf-8") if name in changes else read_file(root, name)
        target = destination / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(raw)
    return destination


@contextmanager
def historical_checkpoint(root=ROOT):
    """Use the old checker and mutation tests in their unchanged commit scope."""
    state = validate_state(root)
    with tempfile.TemporaryDirectory(prefix="measurement-reader-history-") as tmp:
        yield restore_checkpoint(state, Path(tmp) / "checkpoint")


def check(root=ROOT):
    state = validate_state(root)
    with tempfile.TemporaryDirectory(prefix="measurement-reader-history-") as tmp:
        historical = restore_checkpoint(state, Path(tmp) / "checkpoint")
        spec = importlib.util.spec_from_file_location(
            "historical_integrated_preservation", historical / HISTORICAL_CHECKER)
        checker = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(checker)
        previous = checker.check(historical)
    return {
        "passed": True,
        "scope": "Offline exact reader-status changes and historical integration replay; no scientific recomputation or live repository query",
        "starting_commit": START,
        "starting_tree": TREE,
        "starting_files_checked": len(state[1]["files"]),
        "starting_files_byte_unchanged": len(state[1]["files"]) - len(state[2]),
        "recorded_stage_changes": sorted(state[2]),
        "historical_integration_check": previous,
        "historical_checkers_and_evidence_unchanged": True,
        "current_manifest_changes": ["README.md", "STATUS.md"],
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
