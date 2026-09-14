"""Presentation regressions and a narrow fingerprint of the unchanged mathematics.

The fingerprints were computed from commit 49c2434e3f5bc04a031fea21b32c0eaf363886d6.
They permit spacing, delimiter sizing, aligned layout and the two stated operator
aliases only. They do not establish the scientific validity of an expression.
Pandoc's GFM test exercises Markdown structure, not GitHub's authenticated renderer.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess

import pytest


REPO = Path(__file__).resolve().parents[2]
MATH = re.compile(r"(?<!\\)\$\$([\s\S]*?)(?<!\\)\$\$|(?<!\\)\$([^\n$]*?)(?<!\\)\$")
DISPLAY = re.compile(r"(?<!\\)\$\$([\s\S]*?)(?<!\\)\$\$")
TOKENS = re.compile(r"\\(?:begin|end)\{[^}]+\}|\\[A-Za-z]+|\\.|[^\s]")
SPACING = {r"\,", r"\;", r"\:", r"\!", "\\ ", r"\quad", r"\qquad",
           r"\enspace", r"\thinspace", r"\medspace", r"\thickspace"}
SIZING = {r"\left", r"\right", r"\big", r"\Big", r"\bigg", r"\Bigg",
          r"\bigl", r"\bigr", r"\Bigl", r"\Bigr", r"\biggl", r"\biggr",
          r"\Biggl", r"\Biggr"}
BASELINE = {
    "docs/COMPLETE_PROOF.md": {"display": 119, "math_count": 373,
                               "math": "917f72307dfba4f4b3a9010fd1e642dcfe41145e21cef8fd081ed0344815178f",
                               "prose": "995d29ffed3a2a5e77ef341506ef72503feae47094763de827563b6b14802910"},
    "docs/MODEL_AND_CLAIMS.md": {"display": 18, "math_count": 108,
                                 "math": "60bf7732a438803716937c95a04b8d2163467cae73575a5b1c1fcbe6002dd3fe",
                                 "prose": "7181f5a3a88446683cb1794fc9f5d7912447205dd5c497af91ca9a2f15ddf437"},
    "website/pages/channel.md": {"display": 4, "math_count": 56,
                                  "math": "04e85684dbd25ac3c24d346b489ee57bca6558fb4d9e7435de73806ff4ecebff",
                                  "prose": "f69342fa76479f4e88207d7cec1a4396e787e1bad1cb7a867a57df372bce9403"},
}


def normalized_math(expression):
    """Drop only authorized presentation tokens, retaining other environments."""
    for name in ("diag", "Tr"):
        expression = expression.replace(r"\operatorname{" + name + "}",
                                        r"\mathrm{" + name + "}")
    output, environments = [], []
    depth = 0
    for token in TOKENS.findall(expression):
        if token.startswith(r"\begin{"):
            name = token[7:-1]
            environments.append((name, depth))
            if name != "aligned":
                output.append(token)
            continue
        if token.startswith(r"\end{"):
            name = token[5:-1]
            if not environments or environments.pop() != (name, depth):
                raise ValueError("Unbalanced mathematical environment")
            if name != "aligned":
                output.append(token)
            continue
        aligned_level = bool(environments and environments[-1] == ("aligned", depth))
        if aligned_level and token in ("&", r"\\"):
            continue
        if token in SPACING or token in SIZING:
            continue
        if token == "{":
            depth += 1
        elif token == "}":
            depth -= 1
            if depth < 0:
                raise ValueError("Unbalanced mathematical braces")
        output.append(token)
    if environments or depth:
        raise ValueError("Unclosed mathematical environment or braces")
    return output


def fingerprint(source):
    spans = list(MATH.finditer(source))
    expressions = [
        ["display" if item.group(1) is not None else "inline",
         normalized_math(item.group(1) if item.group(1) is not None else item.group(2))]
        for item in spans
    ]
    prose = MATH.sub("<PRESERVED-MATH>", source)
    return {
        "display": sum(item.group(1) is not None for item in spans),
        "math_count": len(spans),
        "math": hashlib.sha256(json.dumps(expressions, separators=(",", ":")).encode()).hexdigest(),
        "prose": hashlib.sha256(prose.encode()).hexdigest(),
    }


def display_hazards(source):
    """Find Markdown block starts and paragraph breaks inside display bodies."""
    hazards = []
    if len(re.findall(r"(?<!\\)\$\$", source)) % 2:
        hazards.append((1, "unmatched display delimiter"))
    for display in DISPLAY.finditer(source):
        body = display.group(1)
        line = source[:display.start()].count("\n") + 1
        if re.search(r"\n[ \t]*\n", body.strip()):
            hazards.append((line, "blank line inside display"))
        # The first body line follows $$, so only continuation lines can start
        # a Markdown block. Spaces alone do not make literal > safe in GFM.
        for offset, continuation in enumerate(body.splitlines()[1:], 1):
            if re.match(r"^[ \t]{0,3}(?:>|#{1,6}(?:[ \t]|$)|[-+*][ \t]+|\d+[.)][ \t]+)",
                        continuation):
                hazards.append((line + offset, "Markdown block start inside display"))
    return hazards


def reading_paths():
    site = json.loads((REPO / "website/site.json").read_text())
    paths = {REPO / page["source"] for page in site["pages"]}
    paths.update(REPO.glob("*.md"))
    paths.update((REPO / "docs").glob("*.md"))
    paths.update((REPO / "reader").rglob("*.md"))
    paths.update((REPO / "website/pages").glob("*.md"))
    paths.update((REPO / "figures").glob("*.md"))
    return sorted(paths)


@pytest.mark.parametrize("path", BASELINE)
def test_mathematics_and_surrounding_prose_preserved(path):
    assert fingerprint((REPO / path).read_text()) == BASELINE[path]


def test_all_current_reading_interfaces_have_safe_display_source():
    paths = reading_paths()
    site_sources = {REPO / page["source"] for page in
                    json.loads((REPO / "website/site.json").read_text())["pages"]}
    assert site_sources <= set(paths)
    assert REPO / "reader/channel.md" in paths
    assert not any("text_sources" in path.parts for path in paths)
    errors = []
    for path in paths:
        source = path.read_text()
        relative = path.relative_to(REPO).as_posix()
        if re.search(r"\\operatorname\b", source):
            errors.append((relative, "unsupported operatorname macro"))
        errors.extend((relative, line, reason) for line, reason in display_hazards(source))
    assert not errors, errors


@pytest.mark.parametrize("old,new", [
    (r"\operatorname{diag}(a,b)", r"\mathrm{diag}(a,b)"),
    (r"\operatorname{Tr}(A)", r"\mathrm{Tr}(A)"),
    (r"x=a+b", r"\begin{aligned}x&=a\\&+b\end{aligned}"),
    (r"\left[a+b\right]", r"\Bigl[a+b\Bigr]"),
    (r"\boxed{x=a+b}", r"\boxed{\begin{aligned}x&=a\\&+b\end{aligned}}"),
])
def test_only_authorized_layout_changes_compare_equal(old, new):
    assert normalized_math(old) == normalized_math(new)


@pytest.mark.parametrize("old,new", [
    (r"x=a-b", r"x=a+b"),
    (r"x>y", r"x\geq y"),
    (r"\frac{7a}{40}", r"\frac{7a}{41}"),
    (r"x^2", r"x^3"),
    (r"x\tag{P7.3}", r"x\tag{P7.4}"),
    (r"\operatorname{rank}(T)", r"\mathrm{rank}(T)"),
    (r"\begin{cases}a,&x>0\\b,&x=0\end{cases}",
     r"\begin{cases}a,x>0b,x=0\end{cases}"),
    (r"\begin{array}{cc}a&b\\c&d\end{array}",
     r"\begin{array}{cc}ab cd\end{array}"),
    (r"\begin{aligned}x&=\begin{cases}a,&x>0\\b,&x=0\end{cases}\end{aligned}",
     r"\begin{aligned}x&=\begin{cases}a,x>0b,x=0\end{cases}\end{aligned}"),
    (r"x={a}", r"x=a"),
])
def test_scientific_and_other_structural_mutations_remain_detectable(old, new):
    assert normalized_math(old) != normalized_math(new)


@pytest.mark.parametrize("expression", [
    r"\begin{aligned}x&=a", r"\end{aligned}x=a", r"\begin{cases}x\end{aligned}",
    r"\begin{aligned}{x\end{aligned}}", r"{x", r"x}",
])
def test_malformed_alignment_or_braces_fail(expression):
    with pytest.raises(ValueError):
        normalized_math(expression)


@pytest.mark.parametrize("continuation", [">a", "> a", "- a", "+ a", "* a", "1. a", "2) a", "# a"])
def test_markdown_block_starts_are_rejected(continuation):
    assert display_hazards("$$x\n" + continuation + "$$")


def test_blank_line_inside_math_is_rejected_but_outer_delimiter_lines_are_allowed():
    assert display_hazards("$$x\n\ny$$")
    assert not display_hazards("$$\nx+y\n$$")
    assert not display_hazards(r"$$\begin{aligned}" + "\nx&>a\\\\\n&+b\n" + r"\end{aligned}$$")


def test_unmatched_display_delimiter_is_rejected():
    assert display_hazards("$$x+y")


ORIGINAL_P08 = r"""$$P(a)-\frac{\arcsin\sqrt a}{\sqrt a}
>a\left(\frac1{12}+\frac{7a}{40}-\frac{193a^2}{840}\right)\geq\frac a{35}.$$"""
ORIGINAL_P73 = r"""\mu(c)=(1-c\bar P(c))\left[(1-\delta_{\mathrm{cert}})\ln(1/c)-\delta_{\mathrm{cert}}\ln(1/\delta_{\mathrm{cert}})-(1+c)\delta_{\mathrm{cert}}\right]
-(\bar P(c)-1)\eta\ln\frac{1-\epsilon}{\epsilon}. \tag{P7.3}"""


def proof_expression(fragment):
    matches = [item.group(1) for item in DISPLAY.finditer((REPO / "docs/COMPLETE_PROOF.md").read_text())
               if fragment in item.group(1)]
    assert len(matches) == 1
    return matches[0]


def nonempty_aligned_rows(expression):
    assert expression.count(r"\begin{aligned}") == expression.count(r"\end{aligned}") == 1
    body = expression.split(r"\begin{aligned}", 1)[1].split(r"\end{aligned}", 1)[0]
    rows = body.split(r"\\")
    assert len(rows) > 1
    assert all(normalized_math(row.replace("&", "")) for row in rows)
    return rows


def test_reported_p08_inequality_is_aligned_and_mathematically_unchanged():
    assert display_hazards(ORIGINAL_P08)
    current = proof_expression(r"P(a)-\frac{\arcsin")
    nonempty_aligned_rows(current)
    assert normalized_math(current) == normalized_math(DISPLAY.search(ORIGINAL_P08).group(1))


def test_lower_input_tail_has_real_rows_instead_of_source_newlines_only():
    assert r"\begin{aligned}" not in ORIGINAL_P73 and r"\\" not in ORIGINAL_P73
    current = proof_expression(r"\tag{P7.3}")
    rows = nonempty_aligned_rows(current)
    assert len(rows) >= 3
    assert normalized_math(current) == normalized_math(ORIGINAL_P73)


def test_gfm_block_structure_catches_original_inequality_regression():
    pandoc = shutil.which("pandoc")
    assert pandoc, "Install the recorded website dependency Pandoc before presentation checks"
    current = "$$\n" + proof_expression(r"P(a)-\frac{\arcsin") + "\n$$"

    def blocks(source):
        result = subprocess.run([pandoc, "--from=gfm", "--to=json"],
                                input=source, text=True, capture_output=True, check=True)
        return json.loads(result.stdout)["blocks"]

    def contains_quote(value):
        if isinstance(value, dict):
            return value.get("t") == "BlockQuote" or any(contains_quote(item) for item in value.values())
        return isinstance(value, list) and any(contains_quote(item) for item in value)

    assert contains_quote(blocks(ORIGINAL_P08))
    assert not contains_quote(blocks(current))


@pytest.mark.parametrize("path", BASELINE)
def test_changed_sources_convert_to_mathml_without_tex_fallback(path):
    from bs4 import BeautifulSoup
    pandoc = shutil.which("pandoc")
    assert pandoc, "Install the recorded website dependency Pandoc"
    result = subprocess.run(
        [pandoc, "--from=markdown+tex_math_dollars+raw_html", "--to=html5", "--mathml"],
        input=(REPO / path).read_text(), text=True, capture_output=True, check=True,
    )
    assert not result.stderr.strip(), result.stderr
    soup = BeautifulSoup(result.stdout, "html.parser")
    assert len(soup.find_all("math")) == BASELINE[path]["math_count"]
    assert len(soup.select('math[display="block"]')) == BASELINE[path]["display"]
    if path == "docs/COMPLETE_PROOF.md":
        for marker, rows in [(r"\tag{P7.3}", 4), (r"P(a)-\frac{\arcsin", 2)]:
            matches = [m for m in soup.find_all("math") if marker in m.annotation.get_text()]
            assert len(matches) == 1
            assert len(matches[0].mtable.find_all("mtr", recursive=False)) == rows
