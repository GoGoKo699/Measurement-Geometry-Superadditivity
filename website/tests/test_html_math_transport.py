"""Guard the HTML handoff after the protected Markdown stage.

GitHub's protected code syntax preserves TeX through Markdown, but handing the
recovered payload to an HTML parser can still turn ``<t`` or ``<Q`` into a tag.
The four controls are the exact source expressions reported in screenshots on
2026-09-14. Their stored corrupted payloads also drive MathJax's independent
error checks in mathml_check.cjs; the density-matrix control silently truncates.

See https://docs.mathjax.org/en/v3.2/input/tex/html.html.
This deliberately models the destructive HTML handoff. It does not claim to
reimplement GitHub's private rendering service.
"""
from __future__ import annotations

import json
from pathlib import Path
import sys

from bs4 import BeautifulSoup
import pytest


REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "website"))
from markdown_math import html_safe_math, math_spans

CASES = json.loads(Path(__file__).with_name("html_math_cases.json").read_text())["cases"]
PATHS = sorted(json.loads(Path(__file__).with_name("math_source_baseline.json").read_text()))


def html_payload(tex):
    """Model assigning the recovered TeX as HTML before MathJax sees it."""
    return BeautifulSoup("<div>" + tex + "</div>", "html.parser").get_text()


@pytest.mark.parametrize("case", CASES, ids=lambda case: case["name"])
def test_reported_original_expression_reproduces_html_damage(case):
    assert html_payload(case["original_tex"]) == case["html_payload"]
    assert case["html_payload"] != case["original_tex"]
    # Assert the lost tail explicitly: mere brace balance misses the rho case.
    assert case["html_payload"].endswith("0")


@pytest.mark.parametrize("case", CASES, ids=lambda case: case["name"])
def test_reported_expression_has_exact_safe_equivalent_in_current_source(case):
    source = (REPO / case["source_path"]).read_text()
    matches = [span for span in math_spans(source) if case["selector"] in span.tex]
    assert len(matches) == 1, case["name"]
    current = matches[0]
    expected = case["original_tex"].replace("<", r"\lt ").replace(">", r"\gt ")
    assert current.protected and current.display
    assert current.tex == expected
    assert html_payload(current.tex) == current.tex
    wrapped = "```math\n" + case["original_tex"] + "\n```"
    assert math_spans(html_safe_math(wrapped))[0].tex == expected


@pytest.mark.parametrize("path", PATHS)
def test_every_reader_math_payload_survives_html_handoff(path):
    spans = math_spans((REPO / path).read_text())
    assert spans, path
    for span in spans:
        assert "<" not in span.tex and ">" not in span.tex, (path, span.tex)
        assert html_payload(span.tex) == span.tex, (path, span.tex)
