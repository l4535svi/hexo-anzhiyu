#!/usr/bin/env python3
"""Generate Heo-style title poster covers for all Hexo posts.

Design: purple-family gradient + translucent circles + big bold title,
title block vertically centred so it survives the theme's wide cover crop.
Also rewrites each post's `cover:` front-matter to the local poster.
"""
import hashlib
import html
import re
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path.home() / "workspace" / "hexo-anzhiyu-blog"
POSTS = ROOT / "source" / "_posts"
OUT = ROOT / "source" / "img" / "covers"
W, H = 800, 450


def fc_match(pattern):
    r = subprocess.run(["fc-match", "-f", "%{file}:%{index}", pattern],
                       capture_output=True, text=True, check=True)
    f, i = r.stdout.strip().rsplit(":", 1)
    return f, int(i)


BOLD_PATH, BOLD_IDX = fc_match("Noto Sans CJK SC:bold")
REG_PATH, REG_IDX = fc_match("Noto Sans CJK SC")

PALETTES = [
    ((124, 92, 255), (157, 123, 255)),    # violet
    ((139, 92, 246), (192, 132, 252)),    # purple
    ((91, 91, 245), (129, 140, 248)),     # indigo
    ((168, 85, 247), (217, 70, 239)),     # fuchsia
    ((109, 40, 217), (139, 92, 246)),     # deep violet
]

EMOJI_RE = re.compile(r"[\U0001F300-\U0001FAFF\u2600-\u27BF\uFE0F\u200D\u2B00-\u2BFF]")


def clean_title(t):
    t = html.unescape(str(t)).strip()
    t = EMOJI_RE.sub("", t)
    t = re.sub(r"\s+", " ", t)
    return t


def wrap_text(draw, text, font, max_w, max_lines=3):
    """Greedy wrap by measured width; truncate the last line with … if needed."""
    lines, cur, idx = [], "", 0
    n = len(text)
    while idx < n and len(lines) < max_lines:
        ch = text[idx]
        if draw.textlength(cur + ch, font=font) <= max_w:
            cur += ch
            idx += 1
        else:
            if cur:
                lines.append(cur)
                cur = ""
            else:  # single char wider than max_w, force it in
                lines.append(ch)
                idx += 1
    if cur and len(lines) < max_lines:
        lines.append(cur)
    if idx < n:  # text left over: ellipsis on the last line
        last = lines[-1]
        while last and draw.textlength(last + "…", font=font) > max_w:
            last = last[:-1]
        lines[-1] = last + "…"
    return lines


def make_poster(title, slug, footer="码境科技 · Code Realm"):
    seed = int(hashlib.md5(slug.encode()).hexdigest()[:8], 16)
    c1, c2 = PALETTES[seed % len(PALETTES)]

    # vertical gradient via mask composite
    mask = Image.linear_gradient("L").resize((W, H))
    base = Image.composite(Image.new("RGB", (W, H), c1),
                           Image.new("RGB", (W, H), c2), mask)

    # translucent decorative circles
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    od.ellipse([W - 260, -140, W + 120, 240], fill=(255, 255, 255, 26))
    od.ellipse([-120, H - 260, 220, H + 80], fill=(255, 255, 255, 20))
    od.ellipse([W - 420, H - 120, W - 180, H + 120], fill=(255, 255, 255, 16))
    img = Image.alpha_composite(base.convert("RGBA"), overlay).convert("RGB")
    d = ImageDraw.Draw(img)

    title = clean_title(title)
    font = ImageFont.truetype(BOLD_PATH, 54, index=BOLD_IDX)
    max_w = W - 96
    lines = wrap_text(d, title, font, max_w, 3)
    line_h = 72
    block_h = len(lines) * line_h
    footer_font = ImageFont.truetype(REG_PATH, 22, index=REG_IDX)
    start_y = (H - block_h - 58) // 2 + 8

    # accent bar above the title
    d.rounded_rectangle([48, start_y - 26, 48 + 56, start_y - 20], radius=3,
                        fill=(255, 255, 255))
    y = start_y
    for ln in lines:
        d.text((48, y), ln, font=font, fill=(255, 255, 255))
        y += line_h
    d.text((48, y + 8), footer, font=footer_font, fill=(232, 224, 255))
    return img


def parse_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None, None
    return m.group(1), m.group(0)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    try:
        import yaml
    except ImportError:
        yaml = None

    done, failed = 0, []
    for md in sorted(POSTS.glob("*.md")):
        slug = md.stem
        text = md.read_text(encoding="utf-8")
        fm, fm_block = parse_frontmatter(text)
        if fm is None:
            failed.append((slug, "no front-matter"))
            continue
        title = None
        if yaml:
            try:
                data = yaml.safe_load(fm) or {}
                title = data.get("title")
            except Exception:
                title = None
        if title is None:
            m = re.search(r"^title:\s*(.+)$", fm, re.M)
            if not m:
                failed.append((slug, "no title"))
                continue
            title = m.group(1).strip().strip("'\"")
        poster = make_poster(title, slug)
        poster.save(OUT / f"{slug}.jpg", quality=82, optimize=True)
        new_cover = f"cover: /img/covers/{slug}.jpg"
        if re.search(r"^cover:.*$", fm, re.M):
            new_fm = re.sub(r"^cover:.*$", new_cover, fm, flags=re.M)
        else:
            new_fm = re.sub(r"^(title:.*)$", r"\1\n" + new_cover, fm,
                            count=1, flags=re.M)
        md.write_text(text.replace(fm_block, f"---\n{new_fm}\n---\n",
                                   1), encoding="utf-8")
        done += 1

    # generic default cover (config references /img/default_cover.jpg, file was missing)
    default = make_poster("码境科技", "default-cover",
                          footer="分享建站、玩机与 AI 折腾。 · Code Realm")
    default.save(ROOT / "source" / "img" / "default_cover.jpg",
                 quality=82, optimize=True)

    total = sum(p.stat().st_size for p in OUT.glob("*.jpg"))
    print(f"posters: {done} in {OUT} ({total / 1024 / 1024:.1f} MB)")
    print(f"default cover: {ROOT / 'source' / 'img' / 'default_cover.jpg'}")
    if failed:
        print(f"FAILED ({len(failed)}): {failed[:10]}")
    return 0 if not failed else 1


if __name__ == "__main__":
    sys.exit(main())
