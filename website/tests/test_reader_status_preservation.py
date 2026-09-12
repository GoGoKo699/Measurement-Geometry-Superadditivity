"""The presentation stage cannot rewrite scientific or historical artifacts."""
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil

import pytest

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location(
    "current_reader_status", ROOT / "publication/reader-status/check_reader_status.py")
CHECKER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECKER)
PROTECTED = [
    "docs/COMPLETE_PROOF.md",
    "verification/integer/certify_all_noise.py",
    "data/figures/figure1_original_witness140.json",
    "figures/CAPTIONS.md",
    "reader/assets/figure_02_guaranteed_region.svg",
    "publication/integration/check_integrated.py",
    "publication/integration/INTEGRATED_EDITS.json",
]


def dump(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")


@pytest.fixture
def checkout(tmp_path):
    inventory = json.loads((ROOT / CHECKER.INVENTORY_PATH).read_text())
    for name in set(inventory["files"]) | {
            CHECKER.INVENTORY_PATH, CHECKER.EDITS_PATH, CHECKER.BEFORE_PATH}:
        target = tmp_path / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / name, target)
    return tmp_path


def record_changed_bytes(root, name):
    record = json.loads((root / CHECKER.EDITS_PATH).read_text())
    record["files"][name]["after_sha256"] = hashlib.sha256((root / name).read_bytes()).hexdigest()
    dump(root / CHECKER.EDITS_PATH, record)


def test_current_stage_covers_the_start_and_replays_the_historical_check():
    result = CHECKER.check(ROOT)
    inventory = json.loads((ROOT / CHECKER.INVENTORY_PATH).read_text())
    assert result["starting_files_checked"] == len(inventory["files"])
    assert result["starting_files_byte_unchanged"] + len(result["recorded_stage_changes"]) == len(inventory["files"])
    historical = result["historical_integration_check"]
    assert historical["passed"] and historical["starting_commit"] == "deba96a1a2fb3781a357a5d4d2660e6edda638da"
    assert historical["protected_original_graphics"] == 27
    assert historical["accepted_reader_svgs_unchanged"] == 3
    assert not result["live_merge_or_visibility_status_verified"]


@pytest.mark.parametrize("name", PROTECTED)
def test_protected_file_change_cannot_be_declared_an_editorial_edit(checkout, name):
    path = checkout / name
    before = path.read_text()
    path.write_text(before + "\nUnexpected change\n")
    with pytest.raises(ValueError, match="Unrecorded reader-status file change"):
        CHECKER.check(checkout)
    inventory = json.loads((checkout / CHECKER.INVENTORY_PATH).read_text())
    record = json.loads((checkout / CHECKER.EDITS_PATH).read_text())
    record["files"][name] = {
        "before_sha256": inventory["files"][name],
        "after_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    }
    dump(checkout / CHECKER.EDITS_PATH, record)
    with pytest.raises(ValueError, match="Unauthorized reader-status edit path"):
        CHECKER.check(checkout)


def test_snapshot_cannot_silently_change_the_historical_replay(checkout):
    path = checkout / CHECKER.BEFORE_PATH
    before = json.loads(path.read_text())
    before["STATUS.md"] += "\nUnapproved historical wording\n"
    dump(path, before)
    with pytest.raises(ValueError, match="Historical text snapshot differs"):
        CHECKER.check(checkout)


@pytest.mark.parametrize("case", ["missing", "extra"])
def test_snapshots_cover_exactly_the_changed_paths(checkout, case):
    path = checkout / CHECKER.BEFORE_PATH
    before = json.loads(path.read_text())
    if case == "missing":
        del before["STATUS.md"]
    else:
        before["docs/COMPLETE_PROOF.md"] = "Unexpected historical proof"
    dump(path, before)
    with pytest.raises(ValueError, match="cover the exact recorded edits"):
        CHECKER.check(checkout)


def test_modified_starting_inventory_cannot_approve_an_edit(checkout):
    path = checkout / CHECKER.INVENTORY_PATH
    record = json.loads(path.read_text())
    record["files"][PROTECTED[0]] = "0" * 64
    dump(path, record)
    with pytest.raises(ValueError, match="starting inventory changed"):
        CHECKER.check(checkout)


@pytest.mark.parametrize("field,value", [
    ("status", "different_stage"), ("starting_commit", "0" * 40)])
def test_stage_identity_is_required(checkout, field, value):
    path = checkout / CHECKER.EDITS_PATH
    record = json.loads(path.read_text())
    record[field] = value
    dump(path, record)
    with pytest.raises(ValueError, match="edit scope differs"):
        CHECKER.check(checkout)


def test_unrelated_manifest_change_rejected_even_if_recorded(checkout):
    path = checkout / "BASELINE_MANIFEST.json"
    manifest = json.loads(path.read_text())
    manifest["files"][PROTECTED[0]] = "0" * 64
    dump(path, manifest)
    record_changed_bytes(checkout, "BASELINE_MANIFEST.json")
    with pytest.raises(ValueError, match="Manifest changes extend beyond"):
        CHECKER.check(checkout)


def test_visibility_record_cannot_be_changed_by_this_stage(checkout):
    path = checkout / "publication/READINESS.json"
    readiness = json.loads(path.read_text())
    readiness["public_visibility_changed"] = True
    dump(path, readiness)
    record_changed_bytes(checkout, "publication/READINESS.json")
    with pytest.raises(ValueError, match="does not change public visibility"):
        CHECKER.check(checkout)


def test_symlink_cannot_substitute_a_protected_file(checkout, tmp_path):
    path = checkout / PROTECTED[0]
    outside = tmp_path.parent / (tmp_path.name + "-proof.md")
    outside.write_bytes(path.read_bytes())
    path.unlink()
    path.symlink_to(outside)
    with pytest.raises(ValueError, match="missing, symlinked or outside"):
        CHECKER.check(checkout)


def test_historical_reconstruction_cannot_overwrite_a_checkout(checkout):
    state = CHECKER.validate_state(checkout)
    with pytest.raises(ValueError, match="outside the checkout"):
        CHECKER.restore_checkpoint(state, checkout)


def test_result_output_never_overwrites_previous_evidence(tmp_path):
    path = tmp_path / "result.json"
    CHECKER.write_result(path, {"passed": True})
    before = path.read_bytes()
    with pytest.raises(ValueError, match="fresh result path"):
        CHECKER.write_result(path, {"passed": False})
    assert path.read_bytes() == before
