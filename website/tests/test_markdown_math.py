"""Wrapper round trips and TeX transport, independent of scientific claims."""
from pathlib import Path
import sys

import pytest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "website"))
from markdown_math import math_spans, to_dollar_math, to_github_math


@pytest.mark.parametrize("body", [
    r"\boxed{\Gamma\geq\min\{G_{\min},\ell\}.}",
    r"\begin{aligned} a_b&=x_*\\ c&=\frac{1}{2}.\end{aligned}",
    " \n" + r"\frac{a_{b}}{c}\quad x_*" + "\n ",
    "\r\n" + r"\frac{a_{b}}{c}" + "\r\n",
    r"\frac{a}{b}" + "\r",
])
def test_display_roundtrip_preserves_exact_payload(body):
    source = "Before.\n\n$$" + body + "$$\n\nAfter.\n"
    protected = to_github_math(source)
    assert protected == "Before.\n\n```math\n" + body + "\n```\n\nAfter.\n"
    assert to_dollar_math(protected) == source
    assert to_github_math(protected) == protected
    assert math_spans(protected)[0].tex == body


def test_inline_roundtrip_and_source_offsets():
    tex = r"{x}_{a} {y}_{b}+\{x_*\}+\frac{a}{b}"
    source = "Before $" + tex + "$ after."
    protected = to_github_math(source)
    assert protected == "Before $`" + tex + "`$ after."
    assert to_dollar_math(protected) == source
    original, = math_spans(source)
    changed, = math_spans(protected)
    assert source[original.start:original.end] == "$" + tex + "$"
    assert protected[changed.start:changed.end] == "$`" + tex + "`$"
    assert original.tex == changed.tex
    assert not original.display and not changed.display
    assert not original.protected and changed.protected


def test_skip_code_spans_fences_comments_and_escaped_dollars():
    untouched = (
        '`$not_math$` and `` `$also_not$` ``\n'
        '```python\nprint("$code$")\n```\n'
        '~~~~text\n$$not_math$$\n~~~~\n'
        '<!-- $hidden$\n$$also_hidden$$ -->\n'
        r'Literal \$5 and \$10.' + '\n'
    )
    source = untouched + 'Real $x_{i}$ here.\n'
    assert to_github_math(source) == untouched + 'Real $`x_{i}`$ here.\n'
    assert len(math_spans(source)) == 1
    assert to_dollar_math(to_github_math(source)) == source


def test_long_normal_fence_can_contain_short_fences_and_dollars():
    source = '````text\n```math\n$x$\n```\n````\n$y$\n'
    assert to_github_math(source) == source[:-4] + '$`y`$\n'


@pytest.mark.parametrize('source', [
    '$a`b$', '$$a`b$$', '$`a`b`$', '```math\na`b\n```',
])
def test_unsafe_backticks_are_rejected(source):
    with pytest.raises(ValueError, match='Backtick inside math'):
        to_github_math(source)


def test_display_fences_cannot_be_inserted_mid_paragraph():
    with pytest.raises(ValueError, match='own line'):
        to_github_math('Before $$x$$ after.')


def test_existing_crlf_fence_and_surrounding_line_endings():
    source = 'Before.\r\n\r\n```math\r\nx_{a}\r\n```\r\n'
    assert to_dollar_math(source) == 'Before.\r\n\r\n$$x_{a}$$\r\n'


def test_pandoc_receives_normalized_wrappers_and_intact_anchors():
    from build import prepare_markdown
    source = '<a id="example"></a>\n## Example\n\n$`x_{a}`$\n\n```math\n\\frac{a}{b}\n```\n'
    assert prepare_markdown(source) == (
        '<a id="example"></a>\n\n## Example\n\n$x_{a}$\n\n$$\\frac{a}{b}$$\n'
    )
