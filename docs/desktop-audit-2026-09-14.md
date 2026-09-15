# Desktop build audit — 14 September 2026

Every control, sort, filter and keyboard path exercised headlessly, and the numbers checked against
the dataset. Six issues found; all fixed in `src/desk.src.html`.

1. **Critical — the app frame didn't hold its height.** The view `<section>`s weren't flex children
   of `.main`, so the table's scroll container never scrolled. Three symptoms followed from that one
   omission: the whole *page* scrolled instead, taking the top bar, filter rail and detail panel with
   it; the lazy-load listener was bound to a container that never fired a scroll event, so **the table
   was stuck at 120 of 1,805 rows**; and the "show more" fallback sat ~6,500px down the page.
   Fix: `.main > section{flex:1;min-height:0;display:flex;flex-direction:column}`.
2. **Cascade collision introduced by that fix** — the new `display:flex` outranked `[hidden]`, so all
   four views rendered at once at a quarter height each. Fix: `.main > section[hidden]{display:none}`.
3. **Sorting and filtering left the scroll position untouched.** Re-sorting with the full list loaded
   left you 95,000px down, mid-way through a list you had just reordered. Now returns to the top
   whenever the result set or its order changes.
4. **The drink-window sort treated "no window" as year zero**, so ascending opened with 400-odd wines
   that have no window at all. Unknown windows now sort last in both directions.
5. **Accessibility gaps**: no `scope` on column headers, no live region on the result count, no
   accessible name on the table. All added.
6. **Clear shortlist was one destructive click with no undo.** Now two-step, reverting after 4 seconds.

## Verified working

All 7 sort columns in both directions; every filter and combination; reset; multi-word search;
producer and region selects; the three shortcut chips and the shortlisted filter; the detail panel and
its drill-throughs; shortlist add, remove, copy and share; persistence across reload; charts honouring
filters (1,805 → 759 on White, year totals 1,390 → 633); scatter hover and click; bar-chart
click-through; region cards; producer leaderboard; empty state; surprise. No console errors.

Layout checked at 1512 / 1280 / 1100 / 900 / 760 / 430 px: no page scroll, no horizontal body scroll,
the table scrolls in its own container, the top bar stays reachable. Below ~1180px the detail panel
becomes an overlay; below ~900px the filter rail does too, behind the Filters button.

## Design notes

- Fonts are inlined as woff2 data URIs, so the page works offline.
- The chart series palette was re-picked and validated for colourblind separation and contrast:
  Red `#9E2A2B`, White `#0074C8`, Other `#B5822A`. The original gold/slate pairing failed both the
  normal-vision separation floor and the chroma floor.
- **Copy as table** writes TSV to the clipboard rather than offering a download — it pastes straight
  into Excel, and clipboard works in sandboxed hosts where downloads do not.
