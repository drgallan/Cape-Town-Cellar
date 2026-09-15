# Mobile build audit — 14 September 2026

Same treatment as the desktop build, run on an iPhone 13 viewport with touch emulation.
Five issues found; all fixed in `src/mobile.dc.html`.

1. **"Group by Region" was fragmented and wrong.** Rows were ordered by the raw sub-region string
   (Agter-Paarl, Bamboes Bay, Banghoek…) while the sticky headers showed the *grouped* district.
   The result was 41 headers for 15 districts in the first 650 rows — Stellenbosch appeared four
   separate times, each labelled "556". Fix: order by the district key, then the sub-region.
2. **"Vintage, oldest" led with 49 non-vintage wines** — NV was scored as year 0, so every NV Cap
   Classique and fortified came before the 1996 Boplaas. NV now sorts last in that mode.
3. **Changing the list left you deep inside it.** Style chips, the sort select, all three sliders, the
   region select and search did not return to the top: after scrolling ~25,000px, switching to White
   left you at 24,695px inside a different set of 759 wines. Every list-changing control now returns
   to the top.
4. **The page scrolled behind an open detail sheet** — scrolling a tasting note moved the list
   underneath. Now locked (`html` + `body` overflow and `touch-action`) while a sheet, the compare
   view or a surprise pick is open, and restored on close.
5. **Tap targets below the 44px guideline** — style chips, hearts, sort select and Surprise me at
   36px, Filters at 42px. All raised to 44px.

## Verified working

All 12 sort modes checked against the data (score, points-per-rand, price both ways,
longest-to-cellar, ready-soonest, vintage both ways, and the three group-bys); filters and
combinations; reset; search; lazy loading, 60 rows per pull, all 1,805 reachable; the detail sheet and
its drill-throughs; shortlist heart, persistence across reload, share link and `#list=` import; the
explore carousel, all four lenses, region cards and producer pin; charts and the cellar-timeline
click-through. No console errors, 490ms to interactive, and no network requests at all.

## Known, not changed

Adding a fourth wine to Compare silently drops the first (cap of three, no message).

## A note on shortlists

Both pages use the localStorage key `cc_shortlist_v1`, which is per-origin. Served from the same
GitHub Pages site they share one shortlist; a locally-opened copy keeps its own. The **Share list**
link is the reliable way to move a shortlist between devices.
