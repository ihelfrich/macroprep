# Macro Prep

An interactive intermediate-macroeconomics reference with **live data from FRED**, **drill problems**, **interactive tools**, and a **30-question full exam**. Built with Quarto, deployed to GitHub Pages.

🌐 **Live site:** [ihelfrich.github.io/macroprep](https://ihelfrich.github.io/macroprep/)

## What's here

- **10 chapters** covering CPI/unemployment, the Keynesian cross, multipliers, fiscal policy, money & banking, the money market, bonds, AS/AD, foreign exchange, monetary policy regimes.
- **5 interactive tools** with Observable-JS sliders that compute equilibrium output, the multiplier table, money creation, bond pricing, and PPP exchange rates in real time.
- **6 live-data dashboards** pulling from FRED for inflation (CPI, core CPI, PCE), labor markets (unemployment, LFPR, payrolls), money & rates (M2, fed funds, term spread), output (real GDP, recession bands), exchange rates (DXY, broad real index), and a news feed of recent FOMC / BLS / BEA / Treasury releases.
- **120+ practice questions** organized by topic and difficulty, plus a 30-question full-exam simulator with detailed solutions.
- **Reference** material: formula sheet, glossary, common-screw-up list, source bibliography.

## Local development

Requires [Quarto](https://quarto.org) and Python 3.9+.

```bash
# Render once
quarto render

# Live preview with auto-reload
quarto preview

# Refresh cached macro data from FRED + RSS sources
python3 scripts/fetch_macro_data.py
python3 scripts/fetch_feeds.py
```

## Continuous data refresh

GitHub Actions runs `.github/workflows/refresh-data.yml` on a daily cron, re-fetches FRED time series and RSS feeds, and commits any updates back to `main`. The site rebuild kicks off automatically.

## Repo layout

```
macroprep/
├── _quarto.yml                    book config
├── index.qmd                      landing page
├── chapters/                      10 chapter QMDs
├── interactive/                   5 OJS-driven tool QMDs
├── dashboards/                    6 live-data dashboards
├── practice/                      decision tree, quick quiz, full exam, 120-Q bank
├── reference/                     formulas, glossary, traps, sources
├── data/
│   ├── fred/*.json                cached FRED time series
│   └── feeds/*.json               cached RSS feeds
├── scripts/
│   ├── fetch_macro_data.py        FRED CSV → JSON
│   └── fetch_feeds.py             RSS/Atom → JSON
├── .github/workflows/
│   ├── publish-site.yml           Quarto render + GH Pages deploy
│   └── refresh-data.yml           daily data refresh
├── assets/                        theme.scss + styles.css
└── docs/                          build output (served by GH Pages)
```

## Citation

If you use these materials, please cite:

> Helfrich, I. T. (2026). *Macro Prep — Interactive Intermediate-Macroeconomics Reference.* https://ihelfrich.github.io/macroprep/

## License

Code and prose under CC-BY-SA 4.0. FRED, BLS, BEA, Treasury, and other source data is in the U.S. public domain or under the source's own terms.
