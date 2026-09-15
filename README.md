# Cape Cellar 2026

Two browser tools over the 1,805 South African wines Tim Atkin MW scored in the
*South Africa 2026 Special Report* — with price, drinking window, full tasting note, and a value
reading that compares each bottle with what its quality normally costs.

Static site, no build step on the server.

**Live:** https://drgallan.github.io/Cape-Town-Cellar/
&nbsp;·&nbsp; [Desk](https://drgallan.github.io/Cape-Town-Cellar/desk/)

| | |
|---|---|
| `index.html` | **Pocket** — the phone app. Self-contained: data, fonts, map and React are inlined. |
| `desk/index.html` | **Desk** — sortable table, filter rail, docked detail panel, score-vs-price scatter. Keyboard: `/` search, `↑`/`↓` rows, `Enter` open, `S` shortlist, `Esc` close. |

Both work offline once loaded and make no network request until you tap Satellite.

## Layout

```
index.html          the phone app (built — do not edit by hand)
desk/index.html     the desktop app (built — do not edit by hand)
src/                sources + build.py; edit here, then rebuild
docs/               what was audited, what was wrong, what was fixed
wines.js            the dataset as window.WINES, kept in step with the apps
regions.js          district grouping (window.REGION_GROUPS / REGION_OF)
wards.js            sub-appellation coordinates
map.html            standalone D3 winelands map (not currently linked from either app)
manifest.json  icon.svg  sw.js      home-screen install + offline cache
og.png              social preview
.github/workflows/static.yml        deploys the repo root to Pages on push to main
```

## Rebuild

```sh
python3 src/build.py     # rewrites index.html and desk/index.html
```

No dependencies beyond Python 3. Edit `src/`, rerun, commit source and built pages together.

**Whenever the data changes**, bump the cache name in `sw.js` (`cc-v3` → `cc-v4`) so installed
home-screen copies pick it up instead of serving the old page from cache.

## The data

Each record: `n` `v` name and vintage (`NV` for non-vintage) · `r` region as printed · `st` style ·
`s` `p` score out of 100 and price in rand · `f` `t` drink-from and drink-to (null where the report
gives no window) · `vr` value ratio · `fr` on the per-style price/score frontier · `d` `pr` `id`
tasting note, producer, and the stable id used by share links.

`wines.json` was reconciled wine-by-wine against the report's A–Z table. Scores, prices and styles
matched on 1,800 of the 1,801 first extracted; the extraction bugs found after that check — truncated
notes, wines carrying a sibling's note, four wines dropped entirely — are listed in
[docs/data-audit-2026-09-12.md](docs/data-audit-2026-09-12.md).

The 26 Cape Winemakers Guild auction lots in the report carry no retail price and are not included,
so 1,805 of the 1,830 scored wines are listed here.

Data © Tim Atkin MW, South Africa 2026 Special Report. Prices as supplied by producers.

## Privacy

Shortlists live in `localStorage` under `cc_shortlist_v1` and never leave the browser. **Share list**
encodes the selection into the URL hash, so a shared link carries the wines and nothing else. No
analytics, no cookies, no third-party requests — except Google Maps, and only on Satellite.
