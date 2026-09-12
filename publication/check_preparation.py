"""Check this pending publication package, without licensing or publishing it."""
import argparse
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
START = "1107ac899d2e267c6cf03509168623c13db4038c"
FONT_HASHES = {
    "LICENSES/DejaVu.txt": "d75938dec098f06f0ac3c00853065d94f020be1c3c62ef1dc2975ba15b4d9b0e",
    "LICENSES/STIX.txt": "bab3d31dfef07f483624f2f65f2711e76065b8e7273278b1c071ede1041c9959",
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def check():
    baseline = json.loads((ROOT / "publication/STARTING_FILES.json").read_text())
    require(baseline["commit"] == START, "Unexpected starting commit")
    for name, expected in baseline["files"].items():
        path = ROOT / name
        require(path.is_file(), "Starting file missing: " + name)
        require(hashlib.sha256(path.read_bytes()).hexdigest() == expected,
                "Starting file changed: " + name)
    for name, expected in FONT_HASHES.items():
        require(hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == expected,
                "Upstream font notice changed: " + name)
    state = json.loads((ROOT / "publication/READINESS.json").read_text())
    require(state["starting_commit"] == START, "State starting commit differs")
    for flag in ("license_active", "public_visibility_changed", "merge_performed"):
        require(state[flag] is False, "This package records preparation only: " + flag)
    for name in ("LICENSE", "LICENSE.md", "LICENSE.txt", "CITATION.cff"):
        require(not (ROOT / name).exists(), "Owner adoption requires a separate recorded change: " + name)
    citation = json.loads((ROOT / "publication/proposed/CITATION.cff").read_text())
    require(citation["cff-version"] == "1.2.0", "Unexpected CFF version")
    require(citation["type"] == "software", "Repository citation must not invent a paper")
    require(citation["authors"] == [{"family-names": "Lin", "given-names": "Ruge"}],
            "Update the proposed identity and owner decision together")
    require(not set(citation).intersection({"doi", "date-released", "version", "license",
                                           "preferred-citation", "contact"}),
            "Unconfirmed release, license or contact metadata")
    pages = [ROOT / name for name in ("PUBLICATION.md", "CONTRIBUTING.md", "THIRD_PARTY_NOTICES.md")]
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
        "scope": "Pending editorial package, notice identities and starting-file preservation; not public clearance or a scientific proof check.",
        "starting_commit": START,
        "starting_files_unchanged": len(baseline["files"]),
        "font_notices_exact": len(FONT_HASHES),
        "local_document_links_checked": links,
        "candidate_citation_syntax": "JSON, a YAML 1.2 subset; full CFF schema validation recorded separately",
        "license_active": False,
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
