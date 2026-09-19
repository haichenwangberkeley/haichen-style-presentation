#!/usr/bin/env python3
"""Audit observable Beamer build invariants without modifying the deck."""

import argparse
from pathlib import Path
import re
import subprocess
import sys
from typing import List, Optional


FRAME_RE = re.compile(r"\\begin\{frame\}")
INCLUDE_RE = re.compile(r"\\includegraphics(?:\[[^]]*\])?\{([^}]+)\}")
PRIVATE_PATH_RE = re.compile(r"(?:/global/|/home/|\.codex/|file://)")
FRAME_BLOCK_RE = re.compile(r"\\begin\{frame\}(.*?)\\end\{frame\}", re.DOTALL)
STATEMENT_RE = re.compile(r"\\(slideopening|slideclosing)\b")
PROHIBITED_VISIBLE_RE = (
    # Ghostscript maps some TeX math punctuation to semicolons in extracted
    # text. Restrict this check to prose-like semicolons with a following word.
    (re.compile(r"[A-Za-z0-9)\]]\s*;\s+[A-Za-z0-9(]"), "semicolon"),
    (re.compile(r"\u2014"), "em dash"),
    (re.compile(r"\bfixes\b", re.IGNORECASE), "the verb 'fixes'"),
    (re.compile(r"\breleased\s+(?:data\s+)?sidebands?\b", re.IGNORECASE), "the phrase 'released sidebands'"),
    (re.compile(r"\bgates?\b", re.IGNORECASE), "the generic term 'gate'"),
    (re.compile(r"\bexposure\b", re.IGNORECASE), "the generic term 'exposure'"),
    (re.compile(r"\bsignal\s+interval\b", re.IGNORECASE), "the phrase 'signal interval'"),
    (re.compile(r"\b[A-Za-z]+-rich\b", re.IGNORECASE), "an '-rich' sample label"),
    (re.compile(r"\bqualif(?:y|ies|ied)\s+(?:the\s+)?support\b", re.IGNORECASE), "the phrase 'qualifies the support'"),
    (re.compile(r"\badmits?\s+(?:a|the)\s+family\b", re.IGNORECASE), "the phrase 'admits a family'"),
    (re.compile(r"\bchecks?\s+support(?:\s+limits?)?\b", re.IGNORECASE), "the phrase 'checks support limits'"),
    (re.compile(r"\btemplate\s+replicas?\s+fluctuat", re.IGNORECASE), "agentive template-replica wording"),
    (re.compile(r"\bsix\s+frozen\s+limits?\b", re.IGNORECASE), "the phrase 'six frozen limits'"),
    (re.compile(r"\bHiggs-shaped\s+yield\b", re.IGNORECASE), "the phrase 'Higgs-shaped yield'"),
)


def strip_comments(text: str) -> str:
    """Remove ordinary TeX comments while retaining line numbers and escaped %."""
    return re.sub(r"(?<!\\)((?:\\\\)*)%[^\n]*", r"\1", text)


def braced_argument(text: str, start: int) -> Optional[str]:
    while start < len(text) and text[start].isspace():
        start += 1
    if start == len(text) or text[start] != "{":
        return None
    depth = 1
    position = start + 1
    while position < len(text):
        char = text[position]
        if char == "\\":
            position += 2
            continue
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return text[start + 1:position]
        position += 1
    return None


def statement_errors(text: str) -> List[str]:
    """Check explicit frame statements; rendered visibility still needs review."""
    clean = strip_comments(text)
    document = clean.split(r"\begin{document}", 1)[-1]
    document = document.split(r"\end{document}", 1)[0]
    errors = []  # type: List[str]
    if re.search(r"\\(?:input|include|againframe|frame)\b", document):
        errors.append(
            "document uses external or non-environment frame content; supply an "
            "assembled source with explicit frame environments for full statement coverage"
        )
    blocks = list(FRAME_BLOCK_RE.finditer(document))
    if len(blocks) != len(FRAME_RE.findall(document)):
        errors.append("unmatched frame environments prevent full statement coverage")
    for index, frame in enumerate(blocks, 1):
        body = frame.group(1)
        calls = list(STATEMENT_RE.finditer(body))
        for name in ("slideopening", "slideclosing"):
            matching = [call for call in calls if call.group(1) == name]
            if len(matching) != 1:
                errors.append(
                    "frame {}: expected exactly one \\{} call; found {}".format(
                        index, name, len(matching)
                    )
                )
                continue
            argument = braced_argument(body, matching[0].end())
            if argument is None:
                errors.append("frame {}: \\{} needs a braced argument".format(index, name))
            elif not re.search(r"[A-Za-z0-9\u0080-\uffff]", re.sub(r"\\[A-Za-z]+|[{}]", "", argument)):
                errors.append("frame {}: \\{} statement is empty".format(index, name))
        if len(calls) == 2 and [call.group(1) for call in calls] == ["slideclosing", "slideopening"]:
            errors.append("frame {}: closing statement precedes opening statement".format(index))
    return errors


def document_frames(text: str):
    clean = strip_comments(text)
    document = clean.split(r"\begin{document}", 1)[-1]
    document = document.split(r"\end{document}", 1)[0]
    return list(FRAME_BLOCK_RE.finditer(document))


def frame_title(frame_body: str) -> Optional[str]:
    position = 0
    while position < len(frame_body) and frame_body[position].isspace():
        position += 1
    if position < len(frame_body) and frame_body[position] == "[":
        end = frame_body.find("]", position + 1)
        if end < 0:
            return None
        position = end + 1
    return braced_argument(frame_body, position)


def structure_errors(text: str) -> List[str]:
    """Check talk-level structure that can be established from explicit frames."""
    frames = document_frames(text)
    errors = []  # type: List[str]
    if len(frames) - 1 > 5:
        if len(frames) < 2 or frame_title(frames[1].group(1)) != "Outline":
            errors.append(
                "talk has more than five slides after the title, so frame 2 must be titled Outline"
            )
    return errors


def visible_text_errors(text: str) -> List[str]:
    errors = []  # type: List[str]
    for pattern, label in PROHIBITED_VISIBLE_RE:
        if pattern.search(text):
            errors.append("compiled PDF text contains prohibited {}".format(label))
    return errors


def pdf_page_count(path: Path) -> Optional[int]:
    postscript_path = (
        str(path).replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")
    )
    command = [
        "gs", "-q", "-dNODISPLAY", "-dNOSAFER", "-c",
        f"({postscript_path}) (r) file runpdfbegin pdfpagecount = quit",
    ]
    try:
        result = subprocess.run(
            command,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            timeout=30,
        )
    except (FileNotFoundError, subprocess.CalledProcessError, subprocess.TimeoutExpired):
        return None
    try:
        return int(result.stdout.strip())
    except ValueError:
        return None


def pdf_text(path: Path) -> Optional[str]:
    command = [
        "gs", "-q", "-dSAFER", "-dBATCH", "-dNOPAUSE",
        "-sDEVICE=txtwrite", "-sOutputFile=-", str(path),
    ]
    try:
        result = subprocess.run(
            command,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=30,
        )
    except (FileNotFoundError, subprocess.CalledProcessError, subprocess.TimeoutExpired):
        return None
    return result.stdout.decode("utf-8", errors="replace")


def resolve_graphic(source_dir: Path, value: str) -> Optional[Path]:
    candidate = source_dir / value
    if candidate.suffix:
        return candidate if candidate.exists() else None
    for suffix in (".pdf", ".png", ".jpg", ".jpeg"):
        with_suffix = candidate.with_suffix(suffix)
        if with_suffix.exists():
            return with_suffix
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="Beamer TeX source")
    parser.add_argument("--log", type=Path, help="TeX log; defaults beside source")
    parser.add_argument("--pdf", type=Path, help="PDF; defaults beside source")
    args = parser.parse_args()

    source = args.source.resolve()
    log = (args.log or source.with_suffix(".log")).resolve()
    pdf = (args.pdf or source.with_suffix(".pdf")).resolve()
    errors = []  # type: List[str]
    warnings = []  # type: List[str]

    if not source.is_file():
        print(f"ERROR: source not found: {source}")
        return 2
    text = source.read_text(errors="replace")
    frame_count = len(FRAME_RE.findall(strip_comments(text).split(r"\begin{document}", 1)[-1].split(r"\end{document}", 1)[0]))
    if frame_count == 0:
        errors.append("no Beamer frames found")
    errors.extend(statement_errors(text))
    errors.extend(structure_errors(text))

    if r"\tiny" in text:
        warnings.append("source uses \\tiny; inspect every occurrence for readability")
    if r"\scriptsize" in text:
        warnings.append("source uses \\scriptsize; keep it to sources, citations, or annotations")
    if PRIVATE_PATH_RE.search(text):
        warnings.append("source contains a path-like private location; check visible slide text")

    newest_input = source.stat().st_mtime
    for value in INCLUDE_RE.findall(text):
        graphic = resolve_graphic(source.parent, value)
        if graphic is None:
            warnings.append(f"included graphic not resolved locally: {value}")
        else:
            newest_input = max(newest_input, graphic.stat().st_mtime)

    if not log.is_file():
        errors.append(f"build log not found: {log}")
    else:
        log_text = log.read_text(errors="replace")
        tex_errors = [line for line in log_text.splitlines() if line.startswith("!")]
        if tex_errors:
            errors.append(f"TeX log contains {len(tex_errors)} error line(s)")
        overfull = re.findall(r"Overfull \\[hv]box", log_text)
        if overfull:
            errors.append(f"TeX log contains {len(overfull)} overfull box warning(s)")
        underfull = re.findall(r"Underfull \\[hv]box", log_text)
        if underfull:
            warnings.append(f"TeX log contains {len(underfull)} underfull box warning(s)")

    pages = None
    if not pdf.is_file():
        errors.append(f"PDF not found: {pdf}")
    else:
        if pdf.stat().st_mtime + 1 < newest_input:
            errors.append("PDF is older than the source or an included graphic")
        pages = pdf_page_count(pdf)
        if pages is None:
            warnings.append("PDF page count unavailable; Ghostscript was not usable")
        elif pages < frame_count:
            errors.append(f"PDF has {pages} pages for {frame_count} frames")
        extracted = pdf_text(pdf)
        if extracted is None:
            warnings.append("PDF text unavailable; visible punctuation and wording were not audited")
        else:
            errors.extend(visible_text_errors(extracted))

    print(f"source: {source}")
    print(f"frames: {frame_count}")
    print(f"pdf pages: {pages if pages is not None else 'unknown'}")
    print("Manual review required: verify that each opening previews its slide body and that")
    print("openings and closings are visible, meaningful, and readable throughout overlays.")
    for item in warnings:
        print(f"WARNING: {item}")
    for item in errors:
        print(f"ERROR: {item}")
    if errors:
        print(f"FAIL: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1
    print(f"PASS: 0 errors, {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
