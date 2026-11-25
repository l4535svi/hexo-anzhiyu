#!/usr/bin/env python3
"""Convert Firefly-format Blogger export to Hexo posts.

Source: ~/workspace/your_files/blogger-firefly-posts.zip
  Each .md has Firefly frontmatter:
    title, published (YYYY-MM-DD), description, tags: [...],
    category: "...", image, slug, comment
Output: <site>/source/_posts/<slug>.md with Hexo frontmatter:
    title, date (from published), tags, categories, description
Body is kept verbatim. Duplicate slugs get a -2 / -3 suffix.
_index.csv is skipped (it is an index, not a post).
Written fresh for the hexo-anzhiyu-blog migration (2026-11-25).
"""
import re
import sys
import zipfile
from pathlib import Path

import yaml

SITE = Path(__file__).resolve().parent
ZIP_PATH = Path.home() / "workspace" / "your_files" / "blogger-firefly-posts.zip"
OUT_DIR = SITE / "source" / "_posts"

FM_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.S)


def as_list(v):
    if v is None:
        return []
    if isinstance(v, list):
        return [str(x) for x in v if str(x).strip()]
    s = str(v).strip()
    return [s] if s else []


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(ZIP_PATH) as zf:
        names = sorted(n for n in zf.namelist() if n.endswith(".md"))

    seen = {}
    written = 0
    dup_renamed = []
    no_category = 0
    errors = []

    for name in names:
        with zipfile.ZipFile(ZIP_PATH) as zf:
            text = zf.read(name).decode("utf-8")
        m = FM_RE.match(text)
        if not m:
            errors.append(f"{name}: no frontmatter")
            continue
        try:
            fm = yaml.safe_load(m.group(1)) or {}
        except Exception as e:  # noqa: BLE001
            errors.append(f"{name}: frontmatter YAML error: {e}")
            continue
        body = m.group(2)
        title = str(fm.get("title") or Path(name).stem)
        published = fm.get("published")
        date = str(published)[:10] if published else "1970-01-01"
        tags = as_list(fm.get("tags"))
        category = str(fm.get("category") or "").strip()
        if not category:
            no_category += 1
        slug = str(fm.get("slug") or Path(name).stem).strip()
        slug = re.sub(r"[^A-Za-z0-9\-_]+", "-", slug).strip("-") or Path(name).stem

        base, n = slug, 2
        while slug in seen:
            slug = f"{base}-{n}"
            n += 1
        if slug != str(fm.get("slug") or ""):
            dup_renamed.append((name, slug))
        seen[slug] = name

        out_fm = {"title": title, "date": f"{date} 12:00:00"}
        if tags:
            out_fm["tags"] = tags
        if category:
            out_fm["categories"] = [category]
        if str(fm.get("description") or "").strip():
            out_fm["description"] = str(fm.get("description"))
        # Fixups for posts whose body contains template syntax that Hexo's
        # Nunjucks parser would otherwise try to execute:
        # - shopify.md: Shopify Liquid {% render %}/{% if %} examples
        #   -> disable Nunjucks for the whole post (it uses no Hexo tags).
        # - shopify-edm-klaviyo.md: Klaviyo {{ first_name|... }} example
        #   -> wrap just that fragment in {% raw %}...{% endraw %}.
        if slug == "shopify":
            out_fm["disableNunjucks"] = True
        if slug == "shopify-edm-klaviyo":
            body = body.replace(
                "{{ first_name|default:'there' }}",
                "{% raw %}{{ first_name|default:'there' }}{% endraw %}",
            )
        out_text = (
            "---\n"
            + yaml.safe_dump(out_fm, allow_unicode=True, sort_keys=False, width=100000)
            + "---\n"
            + body
        )
        (OUT_DIR / f"{slug}.md").write_text(out_text, encoding="utf-8")
        written += 1

    print(f"source .md files: {len(names)}")
    print(f"written to {OUT_DIR}: {written}")
    print(f"duplicate slugs renamed: {len(dup_renamed)} {dup_renamed}")
    print(f"posts without category: {no_category}")
    print(f"errors: {len(errors)}")
    for e in errors:
        print("  ERROR", e)
    return 0 if not errors and written == len(names) else 1


if __name__ == "__main__":
    sys.exit(main())
