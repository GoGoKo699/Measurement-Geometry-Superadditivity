"""Current protection rejects changed artifacts and forged identity metadata."""
from __future__ import annotations

import hashlib
import importlib.util
import json
import shutil
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "current_scientific_integrity", ROOT / "integrity/check_scientific.py")
CHECKER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECKER)


def write_json(path, value):
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


@pytest.fixture
def checkout(tmp_path):
    entries = CHECKER.load_inventory(ROOT)
    for relative in set(entries) | {CHECKER.INVENTORY, "BASELINE_MANIFEST.json"}:
        target = tmp_path / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / relative, target)
    return tmp_path


def test_current_protection_and_scientific_dependencies():
    result = CHECKER.check()
    assert result["passed"]
    assert result["protected_files"] == 174
    assert result["current_manifest_scientific_entries"] == 164
    assert result["approved_graphical_artifacts_unchanged"] == 27
    assert result["accepted_reader_svgs_unchanged"] == 3
    assert result["scientific_provenance"] == {
        "source_identities": 44,
        "canonical_units": 23,
        "source_fragments": 125,
        "claims": 7,
        "proof_graph_acyclic": True,
    }
    assert result["independent_verifier_boundaries"]
    assert "not mathematical proof verification" in result["scope"]


@pytest.mark.parametrize("relative", [
    "docs/MODEL_AND_CLAIMS.md",
    "docs/COMPLETE_PROOF.md",
    "certificates/common_noise_compact_certificate.json",
    "verification/integer/certify_all_noise.py",
    "verification/mpmath/cross_backend.py",
    "verification/decimal/verify_certificate.py",
    "data/figures/figure1_original_witness140.json",
    "evidence/reference/integer224.json",
    "figures/CAPTIONS.md",
    "figures/approved/figure_01_channel_and_witness.svg",
    "reader/assets/figure_01_channel_and_witness.svg",
    "website/learning_bridge.json",
    "website/palette.json",
    "LICENSES/MIT.txt",
    "CITATION.cff",
])
def test_changed_protected_bytes_fail(checkout, relative):
    path = checkout / relative
    path.write_bytes(path.read_bytes() + b"\n")
    with pytest.raises(ValueError, match="Protected scientific artifact changed"):
        CHECKER.check(checkout)


def test_missing_scientific_file_fails(checkout):
    (checkout / "verification/decimal/decimal_interval.py").unlink()
    with pytest.raises(ValueError, match="Missing protected file"):
        CHECKER.check(checkout)


def test_protected_directory_is_not_a_file(checkout):
    path = checkout / "CITATION.cff"
    path.unlink()
    path.mkdir()
    with pytest.raises(ValueError, match="Missing protected file"):
        CHECKER.check(checkout)


def test_missing_inventory_member_fails(checkout):
    path = checkout / CHECKER.INVENTORY
    record = json.loads(path.read_text())
    record["files"].pop("docs/COMPLETE_PROOF.md")
    write_json(path, record)
    with pytest.raises(ValueError, match="Scientific inventory path coverage changed"):
        CHECKER.check(checkout)


def test_extra_inventory_member_fails(checkout):
    path = checkout / CHECKER.INVENTORY
    record = json.loads(path.read_text())
    record["files"]["unapproved.py"] = "0" * 64
    write_json(path, record)
    with pytest.raises(ValueError, match="Scientific inventory path coverage changed"):
        CHECKER.check(checkout)


def test_rehashing_changed_science_in_inventory_fails(checkout):
    relative = "docs/COMPLETE_PROOF.md"
    source = checkout / relative
    source.write_bytes(source.read_bytes() + b"Changed claim.\n")
    path = checkout / CHECKER.INVENTORY
    record = json.loads(path.read_text())
    record["files"][relative] = hashlib.sha256(source.read_bytes()).hexdigest()
    write_json(path, record)
    with pytest.raises(ValueError, match="Scientific inventory identity mismatch"):
        CHECKER.check(checkout)


def test_malformed_inventory_digest_fails(checkout):
    path = checkout / CHECKER.INVENTORY
    record = json.loads(path.read_text())
    record["files"]["docs/COMPLETE_PROOF.md"] = "not a digest"
    write_json(path, record)
    with pytest.raises(ValueError, match="Malformed protected digest"):
        CHECKER.check(checkout)


@pytest.mark.parametrize("relative", [
    "../outside.md", "/tmp/outside.md", "docs//proof.md",
    "docs/./proof.md", "docs\\proof.md", ".", "",
])
def test_malformed_inventory_paths_fail_before_opening_members(checkout, relative):
    path = checkout / CHECKER.INVENTORY
    record = json.loads(path.read_text())
    record["files"][relative] = record["files"].pop("docs/COMPLETE_PROOF.md")
    write_json(path, record)
    with pytest.raises(ValueError, match="Malformed protected path"):
        CHECKER.check(checkout)


def test_duplicate_inventory_json_key_fails(checkout):
    path = checkout / CHECKER.INVENTORY
    text = path.read_text().replace('"schema_version": 1,',
                                    '"schema_version": 1, "schema_version": 1,', 1)
    path.write_text(text)
    with pytest.raises(ValueError, match="Duplicate JSON key"):
        CHECKER.check(checkout)


@pytest.mark.parametrize("change", ["unknown_field", "boolean_version", "changed_scope"])
def test_inventory_schema_and_identity_cannot_be_redeclared(checkout, change):
    path = checkout / CHECKER.INVENTORY
    record = json.loads(path.read_text())
    if change == "unknown_field":
        record["approval"] = True
    elif change == "boolean_version":
        record["schema_version"] = True
    else:
        record["scope"] = "New approval"
    write_json(path, record)
    with pytest.raises(ValueError):
        CHECKER.check(checkout)


def test_current_manifest_scientific_hash_cannot_be_refreshed(checkout):
    path = checkout / "BASELINE_MANIFEST.json"
    record = json.loads(path.read_text())
    record["files"]["docs/COMPLETE_PROOF.md"] = "0" * 64
    write_json(path, record)
    with pytest.raises(ValueError, match="Current manifest scientific identity changed"):
        CHECKER.check(checkout)


def test_changed_science_and_refreshed_current_manifest_still_fail(checkout):
    relative = "data/figures/figure1_comparison.csv"
    source = checkout / relative
    source.write_bytes(source.read_bytes() + b"\n")
    path = checkout / "BASELINE_MANIFEST.json"
    record = json.loads(path.read_text())
    record["files"][relative] = hashlib.sha256(source.read_bytes()).hexdigest()
    write_json(path, record)
    with pytest.raises(ValueError, match="Protected scientific artifact changed"):
        CHECKER.check(checkout)


def test_current_manifest_cannot_drop_science(checkout):
    path = checkout / "BASELINE_MANIFEST.json"
    record = json.loads(path.read_text())
    record["files"].pop("verification/mpmath/cross_backend.py")
    write_json(path, record)
    with pytest.raises(ValueError, match="Current manifest path coverage changed"):
        CHECKER.check(checkout)


@pytest.mark.parametrize("relative", [CHECKER.INVENTORY, "BASELINE_MANIFEST.json", "docs/COMPLETE_PROOF.md"])
def test_symlinked_protected_file_fails_even_with_identical_bytes(checkout, relative):
    path = checkout / relative
    original = path.with_name(path.name + ".target")
    path.rename(original)
    path.symlink_to(original.name)
    with pytest.raises(ValueError, match="Symlink in protected path"):
        CHECKER.check(checkout)


def test_symlinked_parent_directory_fails(checkout):
    path = checkout / "verification"
    original = checkout / "verification-target"
    path.rename(original)
    path.symlink_to(original.name, target_is_directory=True)
    with pytest.raises(ValueError, match="Symlink in protected path"):
        CHECKER.check(checkout)


def test_current_editorial_identity_has_no_historical_value_dependency(checkout):
    path = checkout / "BASELINE_MANIFEST.json"
    record = json.loads(path.read_text())
    for relative in ("README.md", "STATUS.md"):
        current = checkout / relative
        current.write_text("Current editorial account.\n")
        record["files"][relative] = hashlib.sha256(current.read_bytes()).hexdigest()
    write_json(path, record)
    assert CHECKER.check(checkout)["passed"]


@pytest.mark.parametrize("kind", ["existing", "dangling_symlink"])
def test_report_requires_a_fresh_regular_destination(tmp_path, monkeypatch, kind):
    output = tmp_path / "report.json"
    if kind == "existing":
        output.write_text("Keep this report.\n")
    else:
        output.symlink_to("absent-target.json")
    monkeypatch.setattr(sys, "argv", ["check_scientific.py", "--output", str(output)])
    with pytest.raises(ValueError, match="fresh integrity output path"):
        CHECKER.main()
    if kind == "existing":
        assert output.read_text() == "Keep this report.\n"
    else:
        assert output.is_symlink() and not (tmp_path / "absent-target.json").exists()


def test_report_creation_race_cannot_overwrite_another_file(tmp_path, monkeypatch):
    output = tmp_path / "report.json"

    def intervening_result():
        output.write_text("Another process created this.\n")
        return {"passed": True}

    monkeypatch.setattr(CHECKER, "check", intervening_result)
    monkeypatch.setattr(sys, "argv", ["check_scientific.py", "--output", str(output)])
    with pytest.raises(FileExistsError):
        CHECKER.main()
    assert output.read_text() == "Another process created this.\n"
