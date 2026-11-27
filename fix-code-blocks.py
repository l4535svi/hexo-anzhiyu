#!/usr/bin/env python3
"""Convert Blogger-era [code]...[/code] markers in post bodies to Markdown
fenced code blocks. Handles duplicated orphan [/code] closers (migration
artefacts) by dropping them. Only touches the body, never the front-matter.
"""
import glob
import re
import sys
from pathlib import Path

ROOT = Path.home() / "workspace" / "hexo-anzhiyu-blog"
POSTS = ROOT / "source" / "_posts"


def split_fm(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None, text
    return m.group(0), text[m.end():]


def convert_body(body):
    """State machine: [code] opens a fence, [/code] closes one.
    An orphan [/code] (no open fence) is a duplicated closer: drop it."""
    out = []
    in_fence = False
    for part in re.split(r"(\[code\]|\[/code\])", body):
        if part == "[code]":
            if in_fence:
                out.append(part)  # nested opener: leave literal
            else:
                out.append("\n```\n")
                in_fence = True
        elif part == "[/code]":
            if in_fence:
                out.append("\n```\n")
                in_fence = False
            # else: orphan closer, drop
        else:
            out.append(part)
    if in_fence:
        out.append("\n```\n")
    text = "".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def main():
    changed, skipped, orphans = [], [], {}
    for path in sorted(POSTS.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        fm, body = split_fm(text)
        if fm is None or ("[code]" not in body and "[/code]" not in body):
            continue
        # skip files where a marker sits inside a <pre> block
        pres = [(m.start(), m.end()) for m in
                re.finditer(r"<pre.*?>.*?</pre>", body, re.S | re.I)]
        inside_pre = any(
            s <= m.start() < e
            for m in re.finditer(r"\[/?code\]", body)
            for s, e in pres
        )
        if inside_pre:
            skipped.append(path.name)
            continue
        opens = len(re.findall(r"\[code\]", body))
        closes = len(re.findall(r"\[/code\]", body))
        orphans[path.name] = closes - opens
        new_body = convert_body(body)
        path.write_text(fm + new_body, encoding="utf-8")
        changed.append(path.name)
    print(f"converted: {len(changed)} files")
    print(f"orphan closers dropped: "
          f"{sum(v for v in orphans.values() if v > 0)} "
          f"in {sum(1 for v in orphans.values() if v > 0)} files")
    if skipped:
        print(f"skipped (marker inside <pre>): {skipped}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
