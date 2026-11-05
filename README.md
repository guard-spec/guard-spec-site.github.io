# guard-spec.github.io

The Guard Spec website, served by GitHub Pages. The project itself lives in
[guard-spec/guard-spec](https://github.com/guard-spec/guard-spec).

## Layout

| Path | What it is |
|---|---|
| `src/template.html` | The page. `{{key}}` is replaced from `src/<lang>.json`, `{{icon:name}}` by `src/icons/<name>.svg` |
| `src/en.json`, `src/vi.json` | English and Vietnamese text; both must have every key |
| `src/icons/` | Lucide icons 0.468.0 (ISC), inlined at build time |
| `src/og.html` | Source of the link preview image `assets/og.png` |
| `assets/` | Stylesheet, logo, diagrams and admin UI screenshots |
| `index.html`, `vi/index.html` | Generated; commit them, Pages serves them as they are |

## Editing

```bash
python3 build.py     # regenerate index.html and vi/index.html
./render-og.sh       # only after changing src/og.html
python3 -m http.server 8000   # preview at http://localhost:8000
```

The diagrams and screenshots in `assets/` are copies of `docs/images/` in the
main repository; copy them again when those change.

## Custom domain

The site is served at https://guardspec.io (`CNAME`). `SITE_URL` in
`build.py` must match it. The domain is verified for the `guard-spec`
organization; **Enforce HTTPS** is on.

## License

Apache-2.0, like Guard Spec. Lucide icons are ISC; see [NOTICE](NOTICE).
