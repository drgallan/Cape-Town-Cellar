# Data audit — 12 September 2026

How `src/wines.json` was built, and what was wrong with the first pass.

The dataset was extracted from *Tim Atkin MW, South Africa 2026 Special Report* and reconciled
wine-by-wine against the report's own A–Z summary table.

## Verified correct

- **Scores, prices and styles: 1,800 of 1,801 wines matched the A–Z table exactly — zero mismatches.**
- `fr` (Frontier) is the exact per-style Pareto frontier of score against price.
- `vr` (× value) is K(score, style) ÷ price, where K is the typical price for that score within that style.

## Corrected in this dataset

1. **All 1,365 tasting notes were truncated at ~190 characters**, 275 of them mid-sentence
   (some down to two words). Now complete — 1,390 notes.
2. **Twelve wines carried a sibling's note and drink window.** Producers who make the same wine in
   several districts — Momento Grenache ×3, Damascene Syrah ×2, Damascene Chenin, Boekenhoutskloof
   Cabernet, Corney Chenin, Natte Valleij Cinsault, Observatory Grenache, Rall Syrah, Bellingham
   Bernard OVP Chenin — were matched on name alone, so the wrong note attached. Matched on name +
   region now.
3. **Twenty-one wines had no note or drink window at all**, because their names contain a year
   (Kaapzicht The 1947, Roodekrantz 1975/1977/1984, Rietvallei 1908, Boplaas 1956/1932) or wrap onto
   two lines in the PDF (Kershaw Deconstructed…, Old Road…, Durbanville Hills Collectors'…). Recovered.
4. **Four priced wines had been dropped entirely** by PDF-parse glitches: Boekenhoutskloof The
   Chocolate Block 2025 (93 / R295), Catherine Marshall Pinot Noir on Sandstone 2024 (94 / R315),
   Hasher Family Pinot Noir 2025 (92 / R250), Trizanne Pinot Noir 2025 (91 / R486). Total is now 1,805.
5. **Two wines had lost their producer** and displayed as bare varietals — "Cabernet Sauvignon 2024"
   and "Chenin Blanc 2025". Restored to Durbanville Hills Collectors' Reserve The Castle of Good Hope
   Cabernet Sauvignon and Perdeberg OVP The Dry Land Collection Courageous Barrel Fermented Chenin
   Blanc. "De Trafford Chenin Banc" → Chenin Blanc.
6. **Report typos carried through**: Leeuwenkuil Rosé and Waterford Rose-Mary were styled Red;
   "Welington" on three wines. Corrected. (Van Wyk Rachel Rose is correctly White — a skin-contact white.)

## Known limits of the source

- **26 Cape Winemakers Guild auction lots carry no retail price** and are not included. The report
  scored 1,830 wines; these pages list the 1,805 that have a price.
- **The report disagrees with its own summary table by one point on five wines** — Idiom Sauvignon
  Blanc 2024, Louisvale Cabernet 2024, Lourensford Viognier 2025, Rainbow's End Cabernet Franc 2024,
  Tanzanite Blanc de Blancs NV. These pages use the table figure.
- **Four wines scoring 90+ have no tasting note in the report at all**: Groot Parys Die Tweede Droom
  Chenin 2024, Paul Clüver Riesling 2026, Paul Clüver Sauvignon Blanc 2026, Restless River Klein
  Hemel Chardonnay 2025.
