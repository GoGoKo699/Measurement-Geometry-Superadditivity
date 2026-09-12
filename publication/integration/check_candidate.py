"""Verify the exact offline documentary integration; no numerical evaluation.

Earlier reader, correction and adoption checkers remain scoped to their own
commits. This check composes their preserved state with the recorded candidate.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
START = "234e86439f44d7387134648ff088cf480ee1cd12"
BASELINE_SHA256 = "45ea1482a7e08bcc6ea2c086069e23b0dfbbec69836989258813a9639f608b5e"
CORRECTION_SHA256 = "3e3207a166379b4f8714e711e73b9e4a1ec25d299abdc248e5c0a9815c4e56d8"
ANCILLARY = {
    "BASELINE_MANIFEST.json", "STATUS.md", "WEBSITE.md",
    "reader/PREVIEW_MANIFEST.json", "reader/status.md", "website/build.py",
    "website/pages/status.md", "website/tests/test_default_style.py",
    "website/tests/test_learning_bridge.py",
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check(root=ROOT):
    starting_path = root / "publication/integration/CANDIDATE_STARTING_FILES.json"
    require(digest(starting_path) == BASELINE_SHA256, "Candidate starting inventory changed")
    baseline = json.loads(starting_path.read_text())
    require(baseline["commit"] == START, "Unexpected candidate comparison commit")
    correction_path = root / "provenance/EDITORIAL_CORRECTIONS.json"
    require(digest(correction_path) == CORRECTION_SHA256, "Existing correction record changed")
    corrections = json.loads(correction_path.read_text())["files"]
    edits = json.loads((root / "publication/integration/CANDIDATE_EDITS.json").read_text())
    require(edits["starting_commit"] == START, "Candidate edit basis changed")
    require(edits["status"] == "offline_candidate_not_applied_to_release", "Candidate status differs")
    require(set(edits["files"]) == set(corrections) | ANCILLARY,
            "Candidate changes extend beyond the exact integration set")
    unchanged = []
    for name, before in baseline["files"].items():
        require((root / name).is_file(), "Starting file missing: " + name)
        expected = before
        if name in edits["files"]:
            entry = edits["files"][name]
            require(set(entry) == {"before_sha256", "after_sha256"}, "Malformed candidate edit: " + name)
            require(entry["before_sha256"] == before, "Candidate edit starting hash differs: " + name)
            expected = entry["after_sha256"]
            require(isinstance(expected, str) and re.fullmatch(r"[0-9a-f]{64}", expected),
                    "Malformed candidate after hash: " + name)
            if name in corrections:
                require(before == corrections[name]["before_sha256"] and
                        expected == corrections[name]["after_sha256"],
                        "Core correction differs from the previously recorded payload: " + name)
        else:
            unchanged.append(name)
        require(digest(root / name) == expected, "Unrecorded candidate change: " + name)

    sys.path.insert(0, str(root / "website"))
    spec = importlib.util.spec_from_file_location("candidate_preservation_builder", root / "website/build.py")
    builder = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(builder)
    preservation = builder.verify_baseline()
    require(preservation["baseline_members_with_verified_editorial_corrections"] == 9,
            "Nine exact documentary/identity corrections are required")
    require(preservation["approved_graphical_artifacts_unchanged"] == 27,
            "Protected graphical inventory differs")

    manifest = json.loads((root / "BASELINE_MANIFEST.json").read_text())
    for name, entry in corrections.items():
        require(manifest["files"][name] == digest(root / name), "Current core identity differs: " + name)
        manifest["files"][name] = entry["before_sha256"]
    require(manifest["files"].pop("provenance/EDITORIAL_CORRECTIONS.json") == CORRECTION_SHA256,
            "Current correction-record identity differs")
    require(manifest["files"]["STATUS.md"] == digest(root / "STATUS.md"), "Current status identity differs")
    manifest["files"]["STATUS.md"] = baseline["files"]["STATUS.md"]
    restored = (json.dumps(manifest, indent=2, ensure_ascii=False) + "\n").encode()
    require(hashlib.sha256(restored).hexdigest() == baseline["files"]["BASELINE_MANIFEST.json"],
            "Current manifest changes extend beyond the explicit documentary identities")

    for prefix in ("verification/", "numerics/", "certificates/", "evidence/", "figures/approved/",
                   "reader/assets/", "website/review/", "publication/evidence/", "publication/proposed/"):
        require(all(name in unchanged for name in baseline["files"] if name.startswith(prefix)),
                "Protected scientific or historical material changed: " + prefix)
    for name in ("publication/check_preparation.py", "publication/ADOPTION_EDITS.json",
                 "publication/ADOPTION_STARTING_FILES.json", "publication/LICENSE_ADOPTION.json",
                 "publication/LICENSE_ADOPTION_REPORT.md", "LICENSE.md", "CITATION.cff"):
        require(name in unchanged, "Completed adoption record or operative terms changed: " + name)
    return {
        "passed": True,
        "scope": "Exact documentary integration and preservation, not public clearance or a scientific proof check",
        "starting_commit": START,
        "starting_files_checked": len(baseline["files"]),
        "starting_files_byte_unchanged": len(unchanged),
        "recorded_existing_file_changes": len(edits["files"]),
        "exact_core_documentary_and_identity_changes": len(corrections),
        "ancillary_reader_and_preservation_changes": len(ANCILLARY),
        "protected_original_graphics": preservation["approved_graphical_artifacts_unchanged"],
        "accepted_reader_svgs_unchanged": len([p for p in unchanged if p.startswith("reader/assets/")]),
        "historical_adoption_and_reader_records_unchanged": True,
        "full_science_recomputed": False,
        "release_sources_modified": False,
        "merge_performed": False,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = check()
    if args.output:
        require(not args.output.exists(), "Use a fresh candidate result path")
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
