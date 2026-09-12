"""Check recorded license adoption and preservation, without publishing anything."""
import argparse
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
START = "1107ac899d2e267c6cf03509168623c13db4038c"
ADOPTION_START = "a0ef38a9ea18145028a4e784242738d995e37e87"
EDITORIAL_CHANGES = {
    "BASELINE_MANIFEST.json", "CONTRIBUTING.md", "PUBLICATION.md", "README.md",
    "STATUS.md", "THIRD_PARTY_NOTICES.md", "WEBSITE.md", "publication/READINESS.json",
    "publication/check_preparation.py", "reader/PREVIEW_MANIFEST.json",
    "reader/materials.md", "reader/status.md", "website/build.py", "website/check.py",
    "website/pages/materials.md", "website/pages/status.md", "website/tests/test_site.py",
}
FONT_HASHES = {
    "LICENSES/DejaVu.txt": "d75938dec098f06f0ac3c00853065d94f020be1c3c62ef1dc2975ba15b4d9b0e",
    "LICENSES/STIX.txt": "bab3d31dfef07f483624f2f65f2711e76065b8e7273278b1c071ede1041c9959",
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def check():
    baseline = json.loads((ROOT / "publication/ADOPTION_STARTING_FILES.json").read_text())
    require(baseline["commit"] == ADOPTION_START, "Unexpected adoption starting commit")
    edits = json.loads((ROOT / "publication/ADOPTION_EDITS.json").read_text())
    require(edits["starting_commit"] == ADOPTION_START, "Edit record starting commit differs")
    require(set(edits["files"]) == EDITORIAL_CHANGES, "Unexpected editorial edit inventory")
    for name, expected in baseline["files"].items():
        path = ROOT / name
        require(path.is_file(), "Starting file missing: " + name)
        if name in EDITORIAL_CHANGES:
            require(edits["files"][name]["before_sha256"] == expected,
                    "Editorial starting hash differs: " + name)
            expected = edits["files"][name]["after_sha256"]
        require(hashlib.sha256(path.read_bytes()).hexdigest() == expected,
                "Unrecorded change to starting file: " + name)
    for name, expected in FONT_HASHES.items():
        require(hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == expected,
                "Upstream font notice changed: " + name)
    state = json.loads((ROOT / "publication/READINESS.json").read_text())
    require(state["starting_commit"] == START, "State starting commit differs")
    require(state["license_active"] is True, "Confirmed licenses must be recorded as active")
    adoption = json.loads((ROOT / "publication/LICENSE_ADOPTION.json").read_text())
    require(adoption["adoption_starting_commit"] == ADOPTION_START, "Adoption starting commit differs")
    require(adoption["license_active"] is True, "Adoption must be active")
    consent = adoption["owner_confirmation"]
    require(consent["status"] == "explicitly_confirmed_in_task" and
            consent["rights_holder"] == "Ruge Lin" and
            consent["authority_to_license_original_material"] is True,
            "Owner confirmation differs from recorded decision")
    require(adoption["licenses_by_material"] == {
        "original_code": "MIT", "original_noncode_content": "CC-BY-4.0",
        "third_party": "unchanged component terms"}, "Confirmed license scope differs")
    for flag in ("public_visibility_changed", "merge_performed"):
        require(state[flag] is False and adoption[flag] is False,
                "License adoption does not authorize this action: " + flag)
    require(set(adoption["files_sha256"]) == {
        "LICENSE.md", "LICENSES/MIT.txt", "LICENSES/CC-BY-4.0.txt", "CITATION.cff"},
        "Operative file inventory differs")
    for name, expected in adoption["files_sha256"].items():
        require(hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == expected,
                "Operative file differs: " + name)
    require((ROOT / "LICENSES/MIT.txt").read_bytes() ==
            (ROOT / "publication/proposed/MIT.txt").read_bytes(), "Approved MIT candidate differs")
    citation = json.loads((ROOT / "CITATION.cff").read_text())
    require(citation["cff-version"] == "1.2.0", "Unexpected CFF version")
    require(citation["type"] == "software", "Repository citation must not invent a paper")
    require(citation["authors"] == [{"family-names": "Lin", "given-names": "Ruge"}],
            "Confirmed citation author differs")
    require(not set(citation).intersection({"doi", "date-released", "version", "license",
                                           "preferred-citation", "contact"}),
            "Unconfirmed release/contact metadata or ambiguous whole-file license declaration")
    pages = [ROOT / name for name in ("LICENSE.md", "PUBLICATION.md", "CONTRIBUTING.md", "THIRD_PARTY_NOTICES.md")]
    pages += list((ROOT / "publication").rglob("*.md"))
    links = 0
    for page in pages:
        text = page.read_text()
        require("\u2014" not in text, "New prose contains an em dash: " + str(page))
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            parsed = urlsplit(target)
            if parsed.scheme or not parsed.path:
                continue
            path = (page.parent / unquote(parsed.path)).resolve()
            require(path.is_relative_to(ROOT), "Local link escapes checkout: " + target)
            require(path.exists(), "Missing local link in " + page.name + ": " + target)
            links += 1
    return {
        "passed": True,
        "scope": "Confirmed license adoption, notice identities and explicitly bounded editorial changes; not public clearance, an ownership determination or a scientific proof check.",
        "starting_commit": ADOPTION_START,
        "starting_files_unchanged": len(baseline["files"]) - len(EDITORIAL_CHANGES),
        "recorded_editorial_changes": len(EDITORIAL_CHANGES),
        "font_notices_exact": len(FONT_HASHES),
        "local_document_links_checked": links,
        "operative_citation_syntax": "JSON, a YAML 1.2 subset; full CFF schema validation recorded separately",
        "license_active": True,
        "public_ready_claimed": False,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = check()
    if args.output:
        require(not args.output.exists(), "Use a fresh output file")
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
