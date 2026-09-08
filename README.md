# Cape Cellar 2026

Mobile wine explorer for Tim Atkin MW's South Africa 2026 report. Static site — no build step, no server.

## Files
- `index.html` — the app (self-contained; loads the data files below)
- `wines.js` — the 1,801 wines. Replace this file to update scores/prices.
- `regions.js` — region groupings + map centroids
- `wards.js` — sub-appellation coordinates for the producer map
- `map.html` — the Explore data map (loaded in a frame by index.html)
- `manifest.json`, `icon.svg`, `sw.js` — home-screen install + offline cache

## Hosting on GitHub Pages
1. All files above sit at the repository **root** (not in a subfolder).
2. Settings → Pages → Source: **GitHub Actions** (the included `.github/workflows/pages.yml` deploys the files as-is; `.nojekyll` disables Jekyll).
3. Site URL: `https://drgallan.github.io/Cape-Town-Cellar/`

## Updating
Edit or replace files and commit. Pages redeploys in ~1 minute. Bump the cache name in `sw.js` (`cc-v2` → `cc-v3`) whenever `wines.js` changes so installed apps pick up new data.

Data © Tim Atkin MW, South Africa 2026 Special Report.
