"""Topic coverage, source preservation, and safe generated-file replacement."""
from __future__ import annotations

from collections import Counter
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re

import pytest


ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("topic_furnishing", ROOT / "website/furnish.py")
furnish = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(furnish)


@pytest.fixture(scope="module")
def current_edition():
    # The generator must first validate the unchanged scientific inventory.
    return furnish.expected_files()


@pytest.fixture
def configuration():
    config = json.loads((ROOT / "website/furnishing.json").read_text())
    ledger = {
        row["canonical_id"]: row
        for row in json.loads((ROOT / "provenance/SECTION_LEDGER.json").read_text())["units"]
    }
    return config, ledger


def test_current_edition_has_complete_unit_coverage_and_protection(current_edition):
    outputs, record = current_edition
    furnish.check_outputs(outputs)
    expected_ids = {f"M{i:02}" for i in range(1, 9)} | {f"P{i:02}" for i in range(1, 16)}
    counts = Counter(row["unit"] for row in record["unit_projection"])
    assert set(counts) == expected_ids
    assert all(count == 1 for count in counts.values())
    assert record["canonical_units"] == 23
    assert record["canonical_displayed_expressions"] == 146
    assert record["canonical_math_expressions"] == 527
    assert record["protected_scientific_files"] == 174
    assert record["scientific_editing_authority"] == [
        "docs/MODEL_AND_CLAIMS.md", "docs/COMPLETE_PROOF.md",
    ]
    assert set(outputs) == set(record["generated_files"]) | {furnish.RECORD}
    assert "not a new scientific proof or approval" in record["scope"]


def test_every_projected_unit_retains_all_nonlink_bytes(current_edition):
    outputs, record = current_edition
    # Compare complete source bodies, including prose and labels, rather than
    # checking only selected equations or trusting recorded expression counts.
    link_target = re.compile(rb"(?<=\]\()[^\s)]+(?=\))")
    for row in record["unit_projection"]:
        lines = (ROOT / row["source"]).read_bytes().splitlines(keepends=True)
        first, last = row["source_lines"]
        source = b"".join(lines[first - 1:last])
        assert hashlib.sha256(source).hexdigest() == row["source_sha256"]
        page = outputs[row["destination"].split("#")[0]]
        start = f"<!-- BEGIN canonical-unit {row['unit']} -->\n".encode()
        stop = f"<!-- END canonical-unit {row['unit']} -->".encode()
        assert page.count(start) == page.count(stop) == 1
        projected = page.split(start, 1)[1].split(stop, 1)[0]
        assert link_target.sub(b"LINK_TARGET", projected) == link_target.sub(b"LINK_TARGET", source)
        assert furnish.math_sequence(projected.decode()) == furnish.math_sequence(source.decode())


def test_current_navigation_and_selected_learning_route():
    assert furnish.check_navigation() > 0
    assert furnish.check_learning() == {
        "milestones": 30,
        "background": 12,
        "narrative": 18,
        "anchor": "1604.07450v5",
    }


def test_failed_scientific_integrity_stops_generation_before_source_reads(monkeypatch):
    def reject_integrity():
        raise ValueError("Protected scientific artifact changed")

    def unexpected_read(*args, **kwargs):
        pytest.fail("Generation continued after failed scientific integrity")

    monkeypatch.setattr(furnish, "check_scientific", reject_integrity)
    monkeypatch.setattr(furnish, "read_json", unexpected_read)
    with pytest.raises(ValueError, match="Protected scientific artifact changed"):
        furnish.expected_files()


@pytest.mark.parametrize("mutation", ["duplicate", "missing", "unknown"])
def test_invalid_unit_ownership_is_rejected(configuration, mutation):
    config, ledger = configuration
    if mutation == "duplicate":
        config["topics"][1]["units"].append(config["topics"][0]["units"][0])
    elif mutation == "missing":
        config["topics"][0]["units"].pop()
    else:
        config["topics"][0]["units"].append("P99")
    with pytest.raises(ValueError, match="exactly one topic owner"):
        furnish.validate_config(config, ledger)


def test_missing_source_ledger_unit_is_rejected(configuration):
    config, ledger = configuration
    ledger.pop("P08")
    with pytest.raises(ValueError, match="ledger coverage changed"):
        furnish.validate_config(config, ledger)


@pytest.mark.parametrize("invalid", [
    "science//model.md", "science/./model.md", "../outside.md",
    "/tmp/topic-outside.md", "science\\model.md",
])
def test_noncanonical_output_configuration_is_rejected(configuration, invalid):
    config, ledger = configuration
    config["topics"][0]["path"] = invalid
    with pytest.raises(ValueError, match="Invalid topic output"):
        furnish.validate_config(config, ledger)


@pytest.mark.parametrize("mutation", ["mathematics", "prose", "missing"])
def test_changed_or_missing_generated_body_is_rejected(tmp_path, current_edition, mutation):
    outputs, _ = current_edition
    name = "science/geometric-gap.md"
    expected = {name: outputs[name]}
    furnish.write_outputs(expected, tmp_path)
    target = tmp_path / name
    if mutation == "mathematics":
        assert b"3ca" in expected[name]
        target.write_bytes(expected[name].replace(b"3ca", b"4ca", 1))
    elif mutation == "prose":
        target.write_bytes(expected[name] + b"\nAn unsupported scientific claim.\n")
    else:
        target.unlink()
    with pytest.raises(ValueError, match="Stale or changed topic output"):
        furnish.check_outputs(expected, tmp_path)


@pytest.mark.parametrize("kind", ["parent", "leaf", "dangling_leaf"])
def test_symlinked_outputs_are_rejected_before_any_write(tmp_path, kind):
    root = tmp_path / "edition"
    outside = tmp_path / "outside"
    root.mkdir()
    outside.mkdir()
    original = outside / "page.md"
    original.write_bytes(b"Retain the existing source.\n")
    if kind == "parent":
        (root / "science").symlink_to(outside, target_is_directory=True)
    else:
        (root / "science").mkdir()
        target = original if kind == "leaf" else outside / "absent.md"
        (root / "science/page.md").symlink_to(target)
    outputs = {
        "learning/first.md": b"Do not write before checking every path.\n",
        "science/page.md": b"Generated output.\n",
    }
    with pytest.raises(ValueError, match="Symlink"):
        furnish.write_outputs(outputs, root)
    assert original.read_bytes() == b"Retain the existing source.\n"
    assert not (outside / "absent.md").exists()
    assert not (root / "learning/first.md").exists()
    with pytest.raises(ValueError, match="Symlink"):
        furnish.check_outputs({"science/page.md": outputs["science/page.md"]}, root)


@pytest.mark.parametrize("invalid", [
    "science//page.md", "science/./page.md", "../escape.md",
])
def test_writer_rejects_noncanonical_paths_before_any_write(tmp_path, invalid):
    outputs = {"learning/first.md": b"Keep unwritten.\n", invalid: b"Invalid destination.\n"}
    with pytest.raises(ValueError, match="Invalid output path"):
        furnish.write_outputs(outputs, tmp_path)
    assert not (tmp_path / "learning/first.md").exists()


def test_symlinked_edition_root_is_rejected(tmp_path):
    root = tmp_path / "real"
    root.mkdir()
    alias = tmp_path / "alias"
    alias.symlink_to(root, target_is_directory=True)
    with pytest.raises(ValueError, match="Invalid edition root"):
        furnish.write_outputs({"science/page.md": b"Do not follow a root alias.\n"}, alias)
    assert not list(root.iterdir())


def test_atomic_replacement_preserves_a_hard_linked_source(tmp_path):
    source = tmp_path / "docs/protected-source.md"
    target = tmp_path / "science/model.md"
    source.parent.mkdir()
    target.parent.mkdir()
    source.write_bytes(b"Protected scientific source.\n")
    os.link(source, target)
    assert source.samefile(target)
    expected = {"science/model.md": b"Generated topic edition.\n"}
    furnish.write_outputs(expected, tmp_path)
    assert source.read_bytes() == b"Protected scientific source.\n"
    assert target.read_bytes() == expected["science/model.md"]
    assert not source.samefile(target)
    furnish.check_outputs(expected, tmp_path)


def test_selected_anchor_is_checked_in_the_supplied_root(tmp_path):
    (tmp_path / "learning").mkdir()
    (tmp_path / "website").mkdir()
    (tmp_path / "learning/milestones.md").write_bytes((ROOT / "learning/milestones.md").read_bytes())
    bridge = json.loads((ROOT / "website/learning_bridge.json").read_text())
    bridge["source"]["version"] = "1604.07450v4"
    (tmp_path / "website/learning_bridge.json").write_text(json.dumps(bridge))
    with pytest.raises(ValueError, match="selected Preskill v5|Selected educational anchor"):
        furnish.check_learning(tmp_path)
