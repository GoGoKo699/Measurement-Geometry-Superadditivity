#!/usr/bin/env python3
"""Generate the topic edition without changing protected scientific sources.

All 23 model/proof units have one topic owner. Unit bodies undergo only
Markdown-link transport; their TeX, labels, numbers and prose remain exact.
The existing scientific inventory and source ledger are checked first.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import tempfile
from urllib.parse import unquote, urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "website"))

from baseline_tools import segment
from integrity.check_scientific import check as check_scientific
from learning_bridge import expand_background, load_bridge
from markdown_math import html_safe_math, math_spans, to_github_math

CONFIG = "website/furnishing.json"
RECORD = "website/furnishing-map.json"
UNIT_IDS = {f"M{i:02}" for i in range(1, 9)} | {f"P{i:02}" for i in range(1, 16)}
LINK = re.compile(r"(!?\[[^\]\n]*\]\()([^\s)]+)(\))")
EXPLICIT_ANCHOR = re.compile(r'<a (?:id|name)="([^"]+)"></a>')
LABEL = re.compile(r"\*\*\((P\d+\.\d+)\)\*\*")
COPY_OUTPUTS = {
    "science/physical-picture.md", "science/proof-strategy.md",
    "science/notation.md", "learning/preskill-bridge.md",
    "references/README.md", "verification/README.md",
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def read_json(path):
    def unique(pairs):
        value = {}
        for key, item in pairs:
            require(key not in value, "Duplicate JSON key: " + key)
            value[key] = item
        return value
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique)


def math_sequence(text):
    return [(span.display, span.tex) for span in math_spans(text)]


def validate_config(config, ledger):
    require(config["schema_version"] == 1, "Unknown furnishing schema")
    counts = Counter(unit for page in config["topics"] for unit in page["units"])
    require(set(counts) == UNIT_IDS and all(n == 1 for n in counts.values()),
            "Every canonical unit must have exactly one topic owner")
    require(set(ledger) == UNIT_IDS, "Canonical ledger coverage changed")
    paths = [page["path"] for page in config["topics"] + config["copies"]]
    require(len(paths) == len(set(paths)), "Duplicate topic output")
    require({page["path"] for page in config["copies"]} == COPY_OUTPUTS,
            "Copy output coverage changed")
    for path in paths:
        p = Path(path)
        require(not p.is_absolute() and ".." not in p.parts and p.suffix == ".md"
                and p.as_posix() == path and "\\" not in path,
                "Invalid topic output: " + path)
        require(path.startswith("science/") or path in COPY_OUTPUTS,
                "Output outside the topic edition: " + path)


def routes(config, ledger, bodies):
    owners = {}
    defaults = {
        "docs/MODEL_AND_CLAIMS.md": ("science/model.md", ""),
        "docs/COMPLETE_PROOF.md": ("science/README.md", "proof-route"),
        "website/pages/index.md": ("science/README.md", ""),
        "reader/README.md": ("science/README.md", ""),
        "website/pages/figures.md": ("reader/figures.md", ""),
        "website/pages/limits.md": ("science/limiting-geometries.md", ""),
        "website/pages/verification.md": ("verification/README.md", ""),
        "website/pages/materials.md": ("reader/materials.md", ""),
        "website/pages/visual-design.md": ("reader/visual-design.md", ""),
    }
    for page in config["topics"]:
        for unit in page["units"]:
            source = ledger[unit]["canonical_file"]
            for anchor in EXPLICIT_ANCHOR.findall(bodies[unit]):
                key = (source, anchor)
                require(key not in owners, "Duplicate scientific anchor: " + str(key))
                owners[key] = (page["path"], anchor)
    for page in config["copies"]:
        defaults[page["source"]] = (page["path"], "")
    # Reader pages and their editorial sources are equivalent entry routes.
    for name, source in (
        ("channel", "website/pages/channel.md"),
        ("proof-guide", "website/pages/proof-guide.md"),
        ("background", "website/pages/background.md"),
    ):
        defaults["reader/" + name + ".md"] = defaults[source]
    for source in ("website/pages/limits.md", "reader/limits.md"):
        for old, new in (("coplanar-control", "p11"),
                         ("noise-endpoints", "p11"), ("cone-domain", "p12")):
            owners[(source, old)] = ("science/limiting-geometries.md", new)
    for source in ("website/pages/verification.md", "reader/verification.md"):
        owners[(source, "verification-roles")] = (
            "verification/README.md", "choose-the-verification-scope")
    return owners, defaults


def relative(target, origin):
    return os.path.relpath(ROOT / target, (ROOT / origin).parent).replace(os.sep, "/")


def transport(text, source, destination, owners, defaults):
    def replace(match):
        ref = match.group(2)
        parsed = urlsplit(ref)
        if parsed.scheme or parsed.netloc:
            return match.group()
        target = ((ROOT / source).parent / unquote(parsed.path)).resolve() if parsed.path else ROOT / source
        require(target.is_relative_to(ROOT), "Link leaves the repository: " + ref)
        original = target.relative_to(ROOT).as_posix()
        fragment = unquote(parsed.fragment)
        owner = owners.get((original, fragment))
        if owner is not None:
            output, fragment = owner
        else:
            output, default_fragment = defaults.get(original, (original, ""))
            if not fragment:
                fragment = default_fragment
        path = "" if output == destination else relative(output, destination)
        result = urlunsplit(("", "", path, parsed.query, fragment))
        return match.group(1) + result + match.group(3)
    changed = LINK.sub(replace, text)
    require(math_sequence(changed) == math_sequence(text),
            "Link transport changed mathematics: " + source)
    require(LABEL.findall(changed) == LABEL.findall(text),
            "Link transport changed equation labels: " + source)
    return changed


def navigation(origin):
    targets = (
        ("Science", "science/README.md"),
        ("Learning", "learning/README.md"),
        ("References", "references/README.md"),
        ("Verification", "verification/README.md"),
    )
    return " · ".join(f"[{label}]({relative(target, origin)})" for label, target in targets)


def expected_files():
    integrity = check_scientific()
    config = read_json(ROOT / CONFIG)
    ledger = {row["canonical_id"]: row for row in
              read_json(ROOT / "provenance/SECTION_LEDGER.json")["units"]}
    validate_config(config, ledger)
    bodies = {}
    for unit, row in ledger.items():
        start, end, raw = segment(ROOT / row["canonical_file"], row["canonical_anchor"])
        require((start, end) == (row["canonical_line_start"], row["canonical_line_end"]),
                "Unit line range changed: " + unit)
        require(sha(raw) == row["canonical_fragment_sha256"],
                "Unit source identity changed: " + unit)
        bodies[unit] = raw.decode("utf-8")
    owners, defaults = routes(config, ledger, bodies)
    outputs, records, source_hashes = {}, [], {}
    for page in config["topics"]:
        destination = page["path"]
        parts = [
            "# " + page["title"] + "\n\n",
            navigation(destination) + "\n\n",
            page["introduction"] + "\n\n",
        ]
        for unit in page["units"]:
            row = ledger[unit]
            source = row["canonical_file"]
            source_hashes[source] = sha((ROOT / source).read_bytes())
            body = transport(bodies[unit], source, destination, owners, defaults)
            parts.extend((f"<!-- BEGIN canonical-unit {unit} -->\n", body,
                          f"<!-- END canonical-unit {unit} -->\n\n"))
            expressions = math_sequence(body)
            records.append({
                "unit": unit,
                "source": source,
                "source_lines": [row["canonical_line_start"], row["canonical_line_end"]],
                "source_sha256": row["canonical_fragment_sha256"],
                "destination": destination + "#" + row["canonical_anchor"],
                "transported_sha256": sha(body.encode()),
                "math_expressions": len(expressions),
                "displayed_expressions": sum(display for display, _ in expressions),
                "equation_labels": LABEL.findall(body),
            })
        sources = sorted({ledger[unit]["canonical_file"] for unit in page["units"]})
        footer = " · ".join(f"[{Path(source).name}]({relative(source, destination)})" for source in sources)
        parts.extend((
            "## Where this leads\n\n", page["continuation"] + "\n\n---\n\n",
            "Scientific editing sources: " + footer + ". ",
            f"[Section map]({relative(RECORD, destination)}).\n",
        ))
        outputs[destination] = "".join(parts).encode()

    bridge = load_bridge()
    source_hashes["website/learning_bridge.json"] = sha((ROOT / "website/learning_bridge.json").read_bytes())
    copies = []
    for page in config["copies"]:
        source, destination = page["source"], page["path"]
        raw = (ROOT / source).read_bytes()
        source_hashes[source] = sha(raw)
        body = raw.decode("utf-8")
        if page.get("expand_background"):
            body = expand_background(body, source, bridge)
        body = transport(body, source, destination, owners, defaults)
        # Whole-document companions keep their original title and body.
        title, separator, rest = body.partition("\n")
        require(separator and title.startswith("# "), "Missing source title: " + source)
        result = (title + "\n\n" + navigation(destination) + "\n\n"
                  + page["introduction"] + "\n" + rest
                  + "\n\n---\n\n"
                  + f"Editing source: [{source}]({relative(source, destination)}). "
                  + f"[Section map]({relative(RECORD, destination)}).\n")
        outputs[destination] = html_safe_math(to_github_math(result)).encode()
        require(math_sequence(outputs[destination].decode()) == math_sequence(body),
                "Companion generation changed source mathematics: " + source)
        copies.append({"source": source, "destination": destination,
                       "source_sha256": sha(raw),
                       "expanded_background": bool(page.get("expand_background"))})

    record = {
        "schema_version": 1,
        "source_commit": config["source_commit"],
        "scope": "Deterministic topic presentation of retained sources; not a new scientific proof or approval.",
        "allowed_unit_transformations": ["relative Markdown link transport"],
        "scientific_editing_authority": ["docs/MODEL_AND_CLAIMS.md", "docs/COMPLETE_PROOF.md"],
        "canonical_units": len(records),
        "canonical_displayed_expressions": sum(r["displayed_expressions"] for r in records),
        "canonical_math_expressions": sum(r["math_expressions"] for r in records),
        "protected_scientific_files": integrity["protected_files"],
        "unit_projection": sorted(records, key=lambda row: row["unit"]),
        "companion_projection": copies,
        "source_hashes": dict(sorted(source_hashes.items())),
        "generated_files": {path: sha(raw) for path, raw in sorted(outputs.items())},
        "generate_command": "python website/furnish.py --write",
        "check_command": "python website/furnish.py --check",
    }
    outputs[RECORD] = (json.dumps(record, indent=2, ensure_ascii=False) + "\n").encode()
    return outputs, record


def output_path(root, relative_path):
    root = Path(root)
    require(root.is_dir() and not root.is_symlink(), "Invalid edition root")
    parts = Path(relative_path)
    require(not parts.is_absolute() and ".." not in parts.parts
            and parts.as_posix() == relative_path and "\\" not in relative_path,
            "Invalid output path: " + relative_path)
    path = root
    for part in parts.parts:
        path = path / part
        require(not path.is_symlink(), "Symlink in topic output path: " + relative_path)
    require(path.resolve().is_relative_to(root.resolve()),
            "Topic output leaves the repository: " + relative_path)
    return path


def check_outputs(outputs, root=ROOT):
    for name, raw in outputs.items():
        path = output_path(root, name)
        require(path.is_file() and path.read_bytes() == raw,
                "Stale or changed topic output: " + name)


def write_outputs(outputs, root=ROOT):
    # Validate every destination before writing. Replacing a new inode also
    # keeps an existing hard-linked output from altering its other link.
    destinations = {name: output_path(root, name) for name in outputs}
    for name, raw in outputs.items():
        path = destinations[name]
        path.parent.mkdir(parents=True, exist_ok=True)
        temporary = None
        try:
            with tempfile.NamedTemporaryFile(dir=path.parent, prefix=".furnish-",
                                             delete=False) as handle:
                temporary = Path(handle.name)
                handle.write(raw)
            temporary.chmod(0o644)
            os.replace(temporary, path)
        finally:
            if temporary is not None:
                temporary.unlink(missing_ok=True)


def anchors(text):
    result = set(EXPLICIT_ANCHOR.findall(text))
    used = Counter()
    for heading in re.findall(r"(?m)^#{1,6}\s+(.+?)\s*#*\s*$", text):
        heading = re.sub(r"<[^>]*>", "", heading).lower()
        heading = re.sub(r"[^\w\- ]", "", heading, flags=re.UNICODE).replace(" ", "-")
        if heading:
            index = used[heading]
            result.add(heading + (f"-{index}" if index else ""))
            used[heading] += 1
    return result


def check_navigation(root=ROOT):
    paths = [root / name for name in ("README.md", "CONTRIBUTING.md", "WEBSITE.md", "llms.txt")]
    for folder in ("science", "learning", "references"):
        paths.extend(sorted((root / folder).glob("*.md")))
    paths.append(root / "verification/README.md")
    checked = 0
    cache = {}
    for path in paths:
        require(path.is_file(), "Missing reading route: " + str(path))
        for match in LINK.finditer(path.read_text(encoding="utf-8")):
            ref = match.group(2)
            parsed = urlsplit(ref)
            if parsed.scheme or parsed.netloc:
                continue
            target = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            require(target.is_relative_to(root) and target.exists(),
                    f"Broken topic link: {path.relative_to(root)} -> {ref}")
            if parsed.fragment and target.suffix == ".md":
                if target not in cache:
                    cache[target] = anchors(target.read_text(encoding="utf-8"))
                require(unquote(parsed.fragment) in cache[target],
                        f"Missing topic anchor: {path.relative_to(root)} -> {ref}")
            checked += 1
    return checked


def check_learning(root=ROOT):
    source = (root / "learning/milestones.md").read_text(encoding="utf-8")
    headings = list(re.finditer(r"(?m)^### M(\d{2})\. ", source))
    require([int(m.group(1)) for m in headings] == list(range(1, 31)),
            "Learning route must contain ordered M01 through M30")
    for i, heading in enumerate(headings):
        end = headings[i + 1].start() if i + 1 < len(headings) else len(source)
        body = source[heading.start():end]
        for field in ("Central question", "Understanding target", "Dependencies", "Connection", "Sources"):
            require("**" + field + ":**" in body, "Missing milestone field: " + field)
        dep = re.search(r"\*\*Dependencies:\*\*(.*?)\*\*Connection:\*\*", body, re.S)
        require(dep is not None, "Missing dependency declaration")
        require(all(int(n) < i + 1 for n in re.findall(r"\[M(\d{2})\]", dep.group(1))),
                "Forward or cyclic milestone dependency")
    source_id = load_bridge(root)["source"]["version"]
    require(source_id == "1604.07450v5", "Selected educational anchor changed")
    phase_two = source.index("## Phase II:")
    background = sum(heading.start() < phase_two for heading in headings)
    require(background == 12 and headings[12].start() > phase_two,
            "Milestone phase allocation changed")
    return {"milestones": 30, "background": background,
            "narrative": len(headings) - background, "anchor": source_id}


def run(check=False):
    outputs, record = expected_files()
    if check:
        check_outputs(outputs)
    else:
        write_outputs(outputs)
    links = check_navigation()
    learning = check_learning()
    print(json.dumps({
        "passed": True, "mode": "check" if check else "write",
        "generated_files": len(outputs), "canonical_units": record["canonical_units"],
        "canonical_displayed_expressions": record["canonical_displayed_expressions"],
        "canonical_math_expressions": record["canonical_math_expressions"],
        "protected_scientific_files": record["protected_scientific_files"],
        "local_links": links, **learning,
    }, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    run(parser.parse_args().check)
