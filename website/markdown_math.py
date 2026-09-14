"""Protect TeX from Markdown parsing without changing the TeX payload.

GitHub supports dollar/backtick inline math and fenced ``math`` blocks.
Pandoc consumes the equivalent dollar wrappers via ``to_dollar_math``.
Offsets in ``MathSpan`` include wrappers; ``tex`` excludes wrappers and the
single framing newline before a math fence's closing delimiter. Code spans,
ordinary code fences, and HTML comments are never interpreted as math.
"""
from __future__ import annotations

from dataclasses import dataclass
import re


@dataclass(frozen=True)
class MathSpan:
    start: int
    end: int
    tex: str
    display: bool
    protected: bool
    kind: str


_FENCE_OPEN = re.compile(r"( {0,3})(`{3,}|~{3,})([^\r\n]*)(\r?\n)")


def _escaped(text: str, index: int) -> bool:
    previous = index - 1
    while previous >= 0 and text[previous] == "\\":
        previous -= 1
    return (index - previous - 1) % 2 == 1


def _dollar_end(text: str, start: int, display: bool) -> int | None:
    delimiter = "$$" if display else "$"
    end = start
    while True:
        end = text.find(delimiter, end)
        if end == -1 or (not display and "\n" in text[start:end]):
            return None
        if not _escaped(text, end) and (display or (
            (end == 0 or text[end - 1] != "$")
            and (end + 1 == len(text) or text[end + 1] != "$")
        )):
            return end
        end += len(delimiter)


def math_spans(text: str) -> list[MathSpan]:
    """Find dollar and protected math, leaving ordinary Markdown code alone."""
    spans: list[MathSpan] = []
    index = 0
    while index < len(text):
        if text.startswith("<!--", index):
            end = text.find("-->", index + 4)
            index = len(text) if end == -1 else end + 3
            continue
        if index == 0 or text[index - 1] == "\n":
            opening = _FENCE_OPEN.match(text, index)
            if opening:
                indent, marker, info, newline = opening.groups()
                closing = re.compile(
                    r"(?m)^ {0,3}" + re.escape(marker[0])
                    + "{" + str(len(marker)) + r",}[ \t]*(?=\r?\n|\Z)"
                ).search(text, opening.end())
                if closing is None:
                    if info.strip() == "math":
                        raise ValueError(f"Unclosed math fence at offset {index}")
                    break
                if info.strip() == "math":
                    tex = text[opening.end():closing.start()]
                    # Generated fences add this newline outside the TeX body.
                    if tex.endswith(newline):
                        tex = tex[:-len(newline)]
                    elif tex.endswith("\n"):
                        tex = tex[:-1]
                    spans.append(MathSpan(index + len(indent), closing.end(),
                                          tex, True, True, "math-fence"))
                index = closing.end()
                continue
        if text[index] == "`" and not _escaped(text, index):
            run = re.match(r"`+", text[index:]).group()
            closing = re.compile(r"(?<!`)" + re.escape(run) + r"(?!`)").search(
                text, index + len(run)
            )
            index = closing.end() if closing else index + len(run)
            continue
        if text[index] != "$" or _escaped(text, index):
            index += 1
            continue
        if text.startswith("$`", index):
            end = text.find("`$", index + 2)
            if end == -1:
                raise ValueError(f"Unclosed protected inline math at offset {index}")
            spans.append(MathSpan(index, end + 2, text[index + 2:end],
                                  False, True, "protected-inline"))
            index = end + 2
            continue
        display = text.startswith("$$", index)
        width = 2 if display else 1
        end = _dollar_end(text, index + width, display)
        if end is None:
            index += width
            continue
        spans.append(MathSpan(index, end + width, text[index + width:end],
                              display, False,
                              "dollar-display" if display else "dollar-inline"))
        index = end + width
    return spans


def _replace(text: str, protected: bool) -> str:
    pieces: list[str] = []
    cursor = 0
    for span in math_spans(text):
        if "`" in span.tex:
            raise ValueError(f"Backtick inside math at offset {span.start}")
        pieces.append(text[cursor:span.start])
        if span.protected == protected:
            pieces.append(text[span.start:span.end])
        elif protected:
            if span.display:
                line_start = text.rfind("\n", 0, span.start) + 1
                line_end = text.find("\n", span.end)
                if line_end == -1:
                    line_end = len(text)
                if text[line_start:span.start].strip() or text[span.end:line_end].strip():
                    raise ValueError(f"Display math must occupy its own line at offset {span.start}")
                pieces.append("```math\n" + span.tex + "\n```")
            else:
                pieces.append("$`" + span.tex + "`$")
        else:
            delimiter = "$$" if span.display else "$"
            pieces.append(delimiter + span.tex + delimiter)
        cursor = span.end
    pieces.append(text[cursor:])
    return "".join(pieces)


def to_github_math(text: str) -> str:
    """Protect math wrappers; preserve every TeX payload byte-for-byte."""
    return _replace(text, protected=True)


def to_dollar_math(text: str) -> str:
    """Normalize protected wrappers for Pandoc and source-preservation checks."""
    return _replace(text, protected=False)


def html_safe_math(text: str) -> str:
    """Use equivalent TeX relations that cannot start HTML tags.

    Protected Markdown wrappers do not prevent later HTML parsing of the TeX
    payload. In particular, ``0<t`` can swallow a closing brace or silently
    truncate an expression. A space terminates each replacement control word.
    Ordinary prose, HTML, code and all math wrappers retain their exact bytes.
    """
    for span in reversed(math_spans(text)):
        original = text[span.start:span.end]
        safe = original.replace("<", r"\lt ").replace(">", r"\gt ")
        text = text[:span.start] + safe + text[span.end:]
    return text
