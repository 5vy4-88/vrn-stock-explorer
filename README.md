# VRN Stock Explorer – October 2026

A single-file, offline dashboard for the westernreg.co.uk October 2026 number-plate stock list
(287 rows: 279 priced + 8 "new stock" banner entries, verified against the PDF).

## Quick start
1. Unzip, then open `vrn_dashboard.html` in any modern browser (Chrome, Edge, Firefox, Safari; desktop, tablet or phone).
2. No install, server or internet connection is needed. There are no external requests.
3. Your shortlist, saved views and theme are stored in the browser's local storage. If storage is blocked the page still works, it just will not remember anything.

## What is inside
| Path | Purpose |
|---|---|
| `vrn_dashboard.html` | The dashboard (data embedded) |
| `data/stock_vrns_verified.csv` / `.xlsx` | The verified table (No., VRN, price, part, VAT, source block, format) |
| `data/stock.pdf` | Original source PDF |
| `tools/extract_vrns.py` | Re-extracts the table from the PDF (pdfplumber) |
| `tests/suite.py`, `tests/data.json`, `tests/test_results.json` | Automated browser test suite and the results of the final run |

## Features
- Search, regex, part, price range, character count, VAT toggle (adds 20% to Part 1), plate-type pills and quick-filter pills
- Name matching: contains / starts / ends / near match / initials / known words, with look-alike digit mapping
- Sorting (15 keys, two-level) and ranking (7 methods plus a weighted composite score), top-N select and shortlist
- Price histogram with click and drag range selection; summary statistics and indicative buying cost
- Bulk select, shortlist, side-by-side comparison of plates
- Pagination (page jump, 10 to All rows), saved views, shareable links, export/import of views
- Export: CSV, Excel (.xlsx, 3 sheets), JSON, copy as TSV/Markdown, print/save as PDF
- Light, dark and auto themes; responsive card layout on phones; keyboard and screen-reader labels

## Notes and assumptions
- Prices are as printed. The PDF says most prices are plus VAT and all are plus an £80 transfer fee; the dashboard assumes Part 1 carries 20% VAT and Part 2 does not. Check with the seller. Physical plates are extra.
- E33 HHH/LLL/PPP/VVV/WWW/YYY and IIG 3/ROI 990 appear twice in the PDF (a "new stock" banner and the main list). Starring or selecting one affects its twin.
- Plate "format" (Current, Prefix, Suffix, Dateless) is a pattern label added by this tool, not part of the PDF.
- The name dictionary (about 263 names and short words) is a guide, not exhaustive.

## Test summary (final build)
1017 of 1017 automated checks passed across 21 device profiles (phones, tablets, desktop, landscape) in Chromium. Checks cover filters, name matching, pills, pagination, sorting, ranking, selection, shortlist, comparison, statistics, histogram, theme, persistence, CSV/JSON/Excel downloads, print output, saved views, links and blocked-storage fallback. Contrast ratios are at least 5.0:1 in all four theme paths. Not tested: Firefox and WebKit engines, real devices, and screen-reader behaviour.

To re-run: `pip install playwright openpyxl && playwright install chromium`, then `python tests/suite.py "iPhone 12" 1 .` (device name, heavy-tests flag, output folder).
