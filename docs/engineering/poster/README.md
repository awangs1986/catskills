# Vibe workflow poster

Two one-page pictures of [the vibe handbook](../../../skills/engineering/vibe/WORKFLOW.md): setup, the four lanes, the `implement` chain, the three session-seam moves (`refocus`, `handoff`, `takeover`), the context rules and the "three times wrong" stop rule.

- `../vibe-workflow-poster.png`, drawn by `build_poster.py` (English, linked from the top-level `README.md`).
- `../vibe-workflow-poster.zh-CN.png`, drawn by `build_poster_zh.py` (Chinese, linked from `README.zh-CN.md`). Its Chinese strings are readable source on purpose; `scripts/check-skills.mjs` allows CJK in exactly that path (see `CLAUDE.md`).

The layout is drawn with Pillow, so the text is exact; only the six cat mascots in `cats/` are AI-generated. To re-render after editing the handbook:

```
pip install pillow
# Noto Sans SC 400 and 700 as full TTFs, e.g. built from @fontsource/noto-sans-sc with fontTools
POSTER_FONTS=/path/to/fonts python3 build_poster.py
POSTER_FONTS=/path/to/fonts python3 build_poster_zh.py
```

`POSTER_FONTS` must contain `NotoSansSC-400-full.ttf` and `NotoSansSC-700-full.ttf`; `POSTER_MONO` overrides the monospace font (default: DejaVu Sans Mono Bold). The fonts are not committed (the `fonts/` directory is gitignored).

To build the full TTFs from the fontsource subsets:

```
npm pack @fontsource/noto-sans-sc && tar -xzf fontsource-noto-sans-sc-*.tgz
pip install fonttools brotli
python3 -c "
from fontTools.merge import Merger
import glob
for weight, out in [('400', 'NotoSansSC-400-full.ttf'), ('700', 'NotoSansSC-700-full.ttf')]:
    files = sorted(glob.glob(f'package/files/noto-sans-sc-*-{weight}-normal.woff2'))
    Merger().merge(files).save(out)
"
```
