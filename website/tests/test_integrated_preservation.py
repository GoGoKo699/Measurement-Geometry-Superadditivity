"""Current integration records cannot authorize scientific or historical edits."""
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil

import pytest

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location(
    "integrated_preservation", ROOT / "publication/integration/check_integrated.py")
CHECKER = importlib.util.module_from_spec(spec)
spec.loader.exec_module(CHECKER)
PROOF = "docs/COMPLETE_PROOF.md"
INPUT = "data/figures/figure1_original_witness140.json"
HISTORY = "publication/check_followup.py"


def dump(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")


@pytest.fixture
def checkout(tmp_path):
    inventory = json.loads((ROOT / CHECKER.INVENTORY_PATH).read_text())
    for name in set(inventory["files"]) | {CHECKER.INVENTORY_PATH, CHECKER.EDITS_PATH}:
        target = tmp_path / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / name, target)
    return tmp_path


def record_current_change(root, name):
    inventory = json.loads((root / CHECKER.INVENTORY_PATH).read_text())
    record = json.loads((root / CHECKER.EDITS_PATH).read_text())
    record["files"][name] = {
        "before_sha256": inventory["files"][name],
        "after_sha256": hashlib.sha256((root / name).read_bytes()).hexdigest(),
    }
    dump(root / CHECKER.EDITS_PATH, record)


def test_current_integrated_tree_has_complete_checkpoint_coverage():
    result = CHECKER.check(ROOT)
    inventory = json.loads((ROOT / CHECKER.INVENTORY_PATH).read_text())
    assert result["starting_files_checked"] == len(inventory["files"])
    assert result["starting_files_byte_unchanged"] + len(result["recorded_stage_changes"]) == len(inventory["files"])
    assert result["protected_original_graphics"] == 27
    assert result["accepted_reader_svgs_unchanged"] == 3
    assert not result["live_merge_or_visibility_status_verified"]


@pytest.mark.parametrize("name", [PROOF, INPUT, HISTORY])
def test_missing_scientific_or_historical_file_rejected(checkout, name):
    (checkout / name).unlink()
    with pytest.raises(ValueError, match="Starting file missing"):
        CHECKER.check(checkout)


@pytest.mark.parametrize("name", [PROOF, INPUT, HISTORY])
def test_unrecorded_scientific_or_historical_edit_rejected(checkout, name):
    path = checkout / name
    path.write_bytes(path.read_bytes() + b"\nUnexpected edit\n")
    with pytest.raises(ValueError, match="Unrecorded integrated file change"):
        CHECKER.check(checkout)


@pytest.mark.parametrize("name", [PROOF, INPUT, HISTORY])
def test_declaring_protected_edit_still_cannot_authorize_it(checkout, name):
    path = checkout / name
    path.write_bytes(path.read_bytes() + b"\nUnexpected edit\n")
    record_current_change(checkout, name)
    with pytest.raises(ValueError, match="Unauthorized integrated edit path"):
        CHECKER.check(checkout)


def test_extra_edit_path_rejected(checkout):
    record = json.loads((checkout / CHECKER.EDITS_PATH).read_text())
    record["files"]["new-unapproved-source.py"] = {"before_sha256": "0" * 64, "after_sha256": "1" * 64}
    dump(checkout / CHECKER.EDITS_PATH, record)
    with pytest.raises(ValueError, match="Unauthorized integrated edit path"):
        CHECKER.check(checkout)


def test_modified_starting_inventory_cannot_approve_an_edit(checkout):
    inventory = json.loads((checkout / CHECKER.INVENTORY_PATH).read_text())
    inventory["files"][PROOF] = "0" * 64
    dump(checkout / CHECKER.INVENTORY_PATH, inventory)
    with pytest.raises(ValueError, match="starting inventory changed"):
        CHECKER.check(checkout)


@pytest.mark.parametrize("case", ["before", "after", "extra_field", "no_op", "status", "commit", "missing_record"])
def test_malformed_stage_record_rejected(checkout, case):
    path = checkout / "STATUS.md"
    path.write_bytes(path.read_bytes() + b"\nStage note\n")
    record_current_change(checkout, "STATUS.md")
    record_path = checkout / CHECKER.EDITS_PATH
    record = json.loads(record_path.read_text())
    entry = record["files"]["STATUS.md"]
    if case == "before":
        entry["before_sha256"] = "0" * 64
    elif case == "after":
        entry["after_sha256"] = "invalid"
    elif case == "extra_field":
        entry["permit_anything"] = True
    elif case == "no_op":
        entry["after_sha256"] = entry["before_sha256"]
    elif case == "status":
        record["status"] = "unapproved"
    elif case == "commit":
        record["starting_commit"] = "0" * 40
    elif case == "missing_record":
        record_path.unlink()
    if case != "missing_record":
        dump(record_path, record)
    with pytest.raises(ValueError):
        CHECKER.check(checkout)


def test_unrelated_manifest_edit_rejected_even_if_recorded(checkout):
    path = checkout / "BASELINE_MANIFEST.json"
    manifest = json.loads(path.read_text())
    manifest["files"][INPUT] = "0" * 64
    dump(path, manifest)
    record_current_change(checkout, "BASELINE_MANIFEST.json")
    with pytest.raises(ValueError, match="Manifest changes extend beyond"):
        CHECKER.check(checkout)


@pytest.mark.parametrize("name", ["README.md", "STATUS.md"])
def test_stale_root_document_manifest_identity_rejected(checkout, name):
    path = checkout / name
    path.write_bytes(path.read_bytes() + b"\nUnindexed stage note\n")
    record_current_change(checkout, name)
    with pytest.raises(ValueError, match="Current manifest does not identify"):
        CHECKER.check(checkout)


def test_symlink_cannot_replace_protected_file(checkout, tmp_path):
    path = checkout / PROOF
    outside = tmp_path.parent / (tmp_path.name + "-proof-copy.md")
    outside.write_bytes(path.read_bytes())
    path.unlink()
    path.symlink_to(outside)
    with pytest.raises(ValueError, match="Starting file missing, symlinked or outside"):
        CHECKER.check(checkout)


def test_result_output_never_overwrites_previous_evidence(tmp_path):
    target = tmp_path / "result.json"
    CHECKER.write_result(target, {"passed": True})
    before = target.read_bytes()
    with pytest.raises(ValueError, match="fresh result path"):
        CHECKER.write_result(target, {"passed": False})
    assert target.read_bytes() == before
