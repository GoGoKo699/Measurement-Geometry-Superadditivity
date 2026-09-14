"""Check TeX survival through the actual GFM parser before math rendering.

Disabling Pandoc's math extensions deliberately exposes CommonMark's handling
of unprotected math. Protected inline code and math fences must carry the exact
source TeX through this stage. This is a Markdown transport check, not a claim
to reproduce every GitHub MathJax error or to validate the proof.
"""
from __future__ import annotations

from functools import lru_cache
import json
from pathlib import Path
import shutil
import subprocess
import sys

import pytest


REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "website"))
from markdown_math import math_spans, to_github_math


@lru_cache(maxsize=None)
def transport_reader(pandoc):
    """Disable every available math parser while retaining GFM structure."""
    result = subprocess.run(
        [pandoc, "--list-extensions=gfm"],
        text=True, capture_output=True, check=True,
    )
    available = {line.lstrip("+-") for line in result.stdout.splitlines()}
    assert "tex_math_dollars" in available
    # Since 3.1.9, the separate tex_math_gfm postprocessor turns math fences
    # into Math nodes even if tex_math_dollars is disabled. Older versions do
    # not recognize that extension, so query support rather than guessing it.
    return "gfm" + "".join(
        "-" + extension
        for extension in ("tex_math_dollars", "tex_math_gfm")
        if extension in available
    )


@lru_cache(maxsize=None)
def parse_gfm(source):
    """Run the real GFM parser with its TeX processing explicitly disabled."""
    pandoc = shutil.which("pandoc")
    if pandoc is None:
        pytest.skip("Pandoc is required for the GFM transport check")
    result = subprocess.run(
        [pandoc, "--from=" + transport_reader(pandoc), "--to=json"],
        input=source, text=True, capture_output=True, check=True,
    )
    assert not result.stderr.strip(), result.stderr
    return json.loads(result.stdout)["blocks"]


def recover_math(node):
    """Recover (display, TeX) in document order, including nested table cells.

    Code without the two adjacent dollar delimiters, and code blocks without
    the math language, are ordinary examples and are intentionally excluded.
    Recursion follows Pandoc's AST rather than scraping its rendered HTML.
    """
    if isinstance(node, dict):
        if node.get("t") == "CodeBlock":
            attributes, body = node["c"]
            if "math" in attributes[1]:
                yield True, body
        elif node.get("t") != "Code":
            yield from recover_math(node.get("c"))
    elif isinstance(node, list):
        for index, item in enumerate(node):
            if isinstance(item, dict) and item.get("t") == "Code":
                before = node[index - 1] if index else None
                after = node[index + 1] if index + 1 < len(node) else None
                if (isinstance(before, dict) and before.get("t") == "Str"
                        and before["c"].endswith("$")
                        and isinstance(after, dict) and after.get("t") == "Str"
                        and after["c"].startswith("$")):
                    yield False, item["c"][1]
            else:
                yield from recover_math(item)


def node_types(node):
    if isinstance(node, dict):
        if "t" in node:
            yield node["t"]
        yield from node_types(node.get("c"))
    elif isinstance(node, list):
        for child in node:
            yield from node_types(child)


def migration_paths():
    """Use only the explicitly reviewed migration inventory."""
    inventory = json.loads(
        (REPO / "website/tests/math_source_baseline.json").read_text()
    )
    return sorted(inventory)


@pytest.mark.parametrize("path", migration_paths())
def test_reader_math_survives_real_gfm_without_tex_dollar_extension(path):
    source = (REPO / path).read_text()
    spans = math_spans(source)
    assert spans, f"Migration inventory unexpectedly contains no math: {path}"
    assert all(span.protected for span in spans), path
    expected = [(span.display, span.tex) for span in spans]
    ast = parse_gfm(source)
    assert "Math" not in set(node_types(ast)), "Pandoc math processing was not disabled"
    assert list(recover_math(ast)) == expected, path


def test_protected_math_is_recovered_from_nested_prose_and_tables():
    source = r"""The threshold $`c_*:=2^{-28}`$ and $`x_*`$ preserve the stars.

> Nested $`\{x\}`$ with `literal $not_math$`.
>
> - A list item contains **the value $`a_{j}`$**.

| Quantity | Meaning |
| --- | --- |
| $`t\in[0,1/2]`$ | term $`c_*`$ |

```math
\left\{x_*:\frac{1}{2}<x_*\right\}
```

```python
text = "$not_math$"
```
"""
    expected = [
        (False, r"c_*:=2^{-28}"),
        (False, r"x_*"),
        (False, r"\{x\}"),
        (False, r"a_{j}"),
        (False, r"t\in[0,1/2]"),
        (False, r"c_*"),
        (True, r"\left\{x_*:\frac{1}{2}<x_*\right\}"),
    ]
    ast = parse_gfm(source)
    assert {"BlockQuote", "BulletList", "Strong", "Table"} <= set(node_types(ast))
    assert list(recover_math(ast)) == expected
    assert [(span.display, span.tex) for span in math_spans(source)] == expected


def test_raw_dollar_control_exposes_star_consumption_by_commonmark():
    raw = r"The threshold $c_*:=2^{-28}$ and $x_*$ are positive."
    ast = parse_gfm(raw)
    assert "Emph" in set(node_types(ast))
    protected_ast = parse_gfm(to_github_math(raw))
    assert "Emph" not in set(node_types(protected_ast))
    assert list(recover_math(protected_ast)) == [
        (False, r"c_*:=2^{-28}"), (False, r"x_*"),
    ]


def test_raw_dollar_control_exposes_loss_of_escaped_literal_braces():
    raw = r"$\{x\}$"
    ast = parse_gfm(raw)
    # CommonMark consumes the escapes before a later math renderer sees them.
    assert ast == [{"t": "Para", "c": [{"t": "Str", "c": "${x}$"}]}]
    assert list(recover_math(parse_gfm(to_github_math(raw)))) == [
        (False, r"\{x\}"),
    ]


def test_raw_table_pipe_is_not_protected_by_an_inline_code_span():
    # GFM splits table cells before interpreting their code spans. The corpus
    # comparison above must therefore keep catching raw pipes in math cells.
    raw_pipe = "| Value | Meaning |\n| --- | --- |\n| $`|x|`$ | norm |\n"
    assert "Table" in set(node_types(parse_gfm(raw_pipe)))
    assert list(recover_math(parse_gfm(raw_pipe))) != [(False, "|x|")]
    safe = raw_pipe.replace("|x|", r"\vert x\vert")
    assert list(recover_math(parse_gfm(safe))) == [(False, r"\vert x\vert")]
