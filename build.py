#!/usr/bin/env python3
"""Builds index.html (English) and vi/index.html (Vietnamese) from src/.

src/template.html holds the page; {{key}} comes from src/<lang>.json and
{{icon:name}} inlines src/icons/<name>.svg (Lucide, ISC). Run it after any
change and commit the output: GitHub Pages serves the files as they are.
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent
SRC = ROOT / "src"
LANGS = {"en": ("index.html", ""), "vi": ("vi/index.html", "../")}
# Absolute URL for canonical links and the link preview image. Change it to
# the custom domain (and add a CNAME file) once the domain is set up.
SITE_URL = "https://guardspec.io"


def icon(name):
    svg = (SRC / "icons" / f"{name}.svg").read_text()
    svg = re.sub(r"<!--.*?-->", "", svg, flags=re.S)
    svg = re.sub(r'\s*class="[^"]*"', "", svg)
    svg = svg.replace("<svg", '<svg class="ic" aria-hidden="true"', 1)
    return " ".join(svg.split())


def build():
    template = (SRC / "template.html").read_text()
    strings = {lang: json.loads((SRC / f"{lang}.json").read_text()) for lang in LANGS}
    keys = set(re.findall(r"\{\{([a-z0-9_]+)\}\}", template))
    for lang, s in strings.items():
        extra = {"lang", "root", "lang_path", "en_active", "vi_active", "site_url"}
        missing = keys - set(s) - extra
        if missing:
            sys.exit(f"{lang}.json is missing: {', '.join(sorted(missing))}")
    for lang, (out, root) in LANGS.items():
        values = dict(strings[lang], lang=lang, root=root, site_url=SITE_URL,
                      lang_path="" if lang == "en" else "vi/",
                      en_active="on" if lang == "en" else "",
                      vi_active="on" if lang == "vi" else "")
        html = re.sub(r"\{\{icon:([a-z0-9-]+)\}\}", lambda m: icon(m.group(1)), template)
        html = re.sub(r"\{\{([a-z0-9_]+)\}\}", lambda m: values[m.group(1)], html)
        path = ROOT / out
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(html)
        print(f"wrote {out}")


if __name__ == "__main__":
    build()
