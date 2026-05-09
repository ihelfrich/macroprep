#!/usr/bin/env python3
"""
Fetch macro time series from FRED's public CSV endpoint (no API key) and
write per-series JSON plus a manifest into data/fred/.

Usage:  python3 scripts/fetch_macro_data.py
        python3 scripts/fetch_macro_data.py --years 50
"""
from __future__ import annotations

import argparse
import csv
import io
import json
import logging
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


@dataclass(frozen=True)
class Series:
    id: str
    title: str
    units: str
    freq: str
    source: str
    group: str
    description: str = ""


SERIES: list[Series] = [
    # Prices / Inflation
    Series("CPIAUCSL", "Consumer Price Index, All Urban Consumers",
           "Index 1982-84=100, SA", "M", "BLS", "prices",
           "Headline CPI"),
    Series("CPILFESL", "Core CPI (ex food and energy)",
           "Index 1982-84=100, SA", "M", "BLS", "prices",
           "Core inflation"),
    Series("PCEPI", "PCE Price Index",
           "Index 2017=100, SA", "M", "BEA", "prices",
           "Fed's preferred inflation measure"),
    Series("PCEPILFE", "Core PCE Price Index",
           "Index 2017=100, SA", "M", "BEA", "prices",
           "Core PCE inflation"),
    Series("T5YIE", "5-Year Breakeven Inflation Rate",
           "Percent", "D", "FRB", "prices",
           "Market-implied 5y inflation expectations"),
    # Labor
    Series("UNRATE", "Civilian Unemployment Rate",
           "Percent, SA", "M", "BLS", "labor",
           "Headline U-3"),
    Series("PAYEMS", "Total Nonfarm Payrolls",
           "Thousands of persons, SA", "M", "BLS", "labor",
           "Monthly jobs report headline"),
    Series("CIVPART", "Labor Force Participation Rate",
           "Percent, SA", "M", "BLS", "labor",
           "Share of working-age pop in labor force"),
    Series("ICSA", "Initial Unemployment Claims",
           "Number, SA", "W", "DOL", "labor",
           "Weekly high-frequency labor signal"),
    # Money / Credit
    Series("M2SL", "M2 Money Stock",
           "Billions of Dollars, SA", "M", "FRB", "money",
           "Broad money supply"),
    Series("BAMLH0A0HYM2", "ICE BofA US High Yield Index OAS",
           "Percent", "D", "ICE/BofA", "money",
           "Credit risk premium"),
    # GDP / Output
    Series("GDPC1", "Real Gross Domestic Product",
           "Billions of Chained 2017 Dollars, SAAR", "Q", "BEA", "gdp",
           "Headline real output"),
    Series("GDP", "Nominal Gross Domestic Product",
           "Billions of Dollars, SAAR", "Q", "BEA", "gdp",
           "Nominal output"),
    Series("INDPRO", "Industrial Production Index",
           "Index 2017=100, SA", "M", "FRB", "gdp",
           "Monthly real-economy proxy"),
    Series("RSAFS", "Advance Retail Sales: Retail and Food Services",
           "Millions of Dollars, SA", "M", "Census", "gdp",
           "Consumer spending pulse"),
    # Interest Rates
    Series("DFF", "Federal Funds Effective Rate",
           "Percent", "D", "FRB", "rates",
           "Overnight policy rate"),
    Series("FEDFUNDS", "Federal Funds Effective Rate (monthly)",
           "Percent", "M", "FRB", "rates",
           "Monthly average policy rate"),
    Series("DGS10", "10-Year Treasury Constant Maturity",
           "Percent", "D", "Treasury", "rates",
           "Benchmark long rate"),
    Series("DGS2", "2-Year Treasury Constant Maturity",
           "Percent", "D", "Treasury", "rates",
           "Short-end policy-sensitive yield"),
    Series("T10Y2Y", "10Y minus 2Y Treasury Spread",
           "Percent", "D", "FRB", "rates",
           "Term spread / classic recession indicator"),
    Series("MORTGAGE30US", "30-Year Fixed Mortgage Rate Average",
           "Percent", "W", "Freddie Mac", "rates",
           "Household borrowing cost"),
    # Exchange Rates
    Series("DTWEXBGS", "Nominal Broad USD Index (Goods & Services)",
           "Index Jan 2006=100", "D", "FRB", "fx",
           "Trade-weighted dollar"),
    Series("DEXUSEU", "US Dollar / Euro Exchange Rate",
           "Dollars per Euro", "D", "FRB", "fx",
           "Headline USD/EUR"),
    Series("DEXUSUK", "US Dollar / Pound Exchange Rate",
           "Dollars per Pound", "D", "FRB", "fx",
           "USD/GBP"),
    # Recession / Sentiment
    Series("USREC", "NBER-based Recession Indicator",
           "Binary 0/1", "M", "NBER", "recession",
           "For shading recession bands"),
    Series("UMCSENT", "University of Michigan Consumer Sentiment",
           "Index 1966Q1=100", "M", "UMich", "recession",
           "Consumer confidence"),
]

FRED_CSV = "https://fred.stlouisfed.org/graph/fredgraph.csv?id={sid}"
USER_AGENT = (
    "macroprep-data-fetcher/1.0 "
    "(+https://github.com/ihelfrich/macroprep; contact: ianthelfrich@gmail.com)"
)
log = logging.getLogger("fetch_macro")


def http_get(url: str, timeout: int = 30) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        raw = resp.read()
    return raw.decode("utf-8", errors="replace")


def parse_fred_csv(text: str, cutoff_year: int | None) -> list[dict]:
    reader = csv.reader(io.StringIO(text))
    rows = list(reader)
    if not rows:
        raise ValueError("empty CSV")
    out: list[dict] = []
    for r in rows[1:]:
        if len(r) < 2:
            continue
        date_s, val_s = r[0].strip(), r[1].strip()
        if not date_s or val_s in ("", "."):
            continue
        try:
            d = datetime.strptime(date_s, "%Y-%m-%d").date()
        except ValueError:
            continue
        if cutoff_year is not None and d.year < cutoff_year:
            continue
        try:
            v = float(val_s)
        except ValueError:
            continue
        out.append({"date": d.isoformat(), "value": v})
    return out


def fetch_series(s: Series, years: int | None,
                 retries: int = 3, backoff: float = 2.0) -> list[dict]:
    cutoff = None if years is None else datetime.now(timezone.utc).year - years
    url = FRED_CSV.format(sid=s.id)
    last_err = None
    for attempt in range(1, retries + 1):
        try:
            return parse_fred_csv(http_get(url), cutoff)
        except (urllib.error.URLError, urllib.error.HTTPError, ValueError) as e:
            last_err = e
            log.warning("  attempt %d/%d failed for %s: %s", attempt, retries, s.id, e)
            if attempt < retries:
                time.sleep(backoff ** attempt)
    raise RuntimeError(f"giving up on {s.id}: {last_err}")


def write_series_json(out_dir: Path, s: Series, obs: list[dict]) -> Path:
    payload = {
        "id": s.id, "title": s.title, "units": s.units,
        "freq": s.freq, "source": s.source, "group": s.group,
        "description": s.description,
        "last_updated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "n_observations": len(obs),
        "observations": obs,
    }
    path = out_dir / f"{s.id}.json"
    path.write_text(json.dumps(payload, separators=(",", ":")) + "\n",
                    encoding="utf-8")
    return path


def write_manifest(out_dir: Path, results: list[dict]) -> Path:
    manifest = {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "endpoint": "https://fred.stlouisfed.org/graph/fredgraph.csv",
        "n_series": len(results),
        "series": results,
    }
    path = out_dir / "_manifest.json"
    path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return path


def main(argv=None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--out-dir", default="data/fred")
    p.add_argument("--years", type=int, default=25)
    p.add_argument("--delay", type=float, default=0.8)
    p.add_argument("--only", nargs="*", default=None)
    p.add_argument("-v", "--verbose", action="store_true")
    args = p.parse_args(argv)

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    years = None if args.years == 0 else args.years

    targets = SERIES
    if args.only:
        wanted = set(args.only)
        targets = [s for s in SERIES if s.id in wanted]

    results, n_ok, n_fail = [], 0, 0
    for i, s in enumerate(targets, 1):
        log.info("[%d/%d] %s — %s", i, len(targets), s.id, s.title)
        entry = {"id": s.id, "title": s.title, "units": s.units,
                 "freq": s.freq, "source": s.source, "group": s.group,
                 "description": s.description, "file": f"{s.id}.json"}
        try:
            obs = fetch_series(s, years=years)
            if not obs:
                raise RuntimeError("no observations")
            write_series_json(out_dir, s, obs)
            entry.update(status="ok", n_observations=len(obs),
                         start=obs[0]["date"], end=obs[-1]["date"])
            n_ok += 1
            log.info("  ok: %d obs (%s → %s)", len(obs), obs[0]["date"], obs[-1]["date"])
        except Exception as e:
            entry.update(status="error", error=str(e))
            n_fail += 1
            log.error("  FAILED %s: %s", s.id, e)
        results.append(entry)
        if i < len(targets):
            time.sleep(args.delay)

    write_manifest(out_dir, results)
    log.info("done: %d ok, %d failed", n_ok, n_fail)
    return 0 if n_ok > 0 else 1


if __name__ == "__main__":
    sys.exit(main())
