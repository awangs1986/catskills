# Vibe workflow poster

`../vibe-workflow-poster.png` is a one-page, Chinese-language picture of [the vibe handbook](../../../skills/engineering/vibe/WORKFLOW.md): setup, the four lanes, the `implement` chain, the three session-seam moves (`refocus`, `handoff`, `takeover`), the context rules and the "three times wrong" stop rule.

The layout is drawn by `build_poster.py` with Pillow, so the text is exact; only the six cat mascots in `cats/` are AI-generated. To re-render after editing the handbook:

```
pip install pillow
# Noto Sans SC 400 and 700 as full TTFs, e.g. built from @fontsource/noto-sans-sc with fontTools
POSTER_FONTS=/path/to/fonts python3 build_poster.py
```

`POSTER_FONTS` must contain `NotoSansSC-400-full.ttf` and `NotoSansSC-700-full.ttf`; `POSTER_MONO` overrides the monospace font (default: DejaVu Sans Mono Bold). The fonts are not committed.
