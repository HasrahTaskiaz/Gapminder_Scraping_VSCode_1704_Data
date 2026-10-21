"""Pengambilan dan pembersihan data Gapminder dari CSV publik di web.

Catatan: ini scraping/ekstraksi CSV web, bukan parsing HTML.
Sumber: https://github.com/plotly/datasets/blob/master/gapminderDataFiveYear.csv
"""

import argparse
import io
from pathlib import Path
import sys
import pandas as pd
import requests

URL = "https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv"
COLUMNS = ["country", "year", "pop", "continent", "lifeExp", "gdpPercap"]
ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"


def download_csv(url: str = URL) -> pd.DataFrame:
    """Unduh CSV dengan user-agent, timeout dan pemeriksaan respons HTTP."""
    headers = {"User-Agent": "EducationalGapminderDataProject/1.0 (non-commercial)"}
    response = requests.get(url, headers=headers, timeout=30)
    response.raise_for_status()
    return pd.read_csv(io.BytesIO(response.content))


def clean_and_validate(df: pd.DataFrame) -> pd.DataFrame:
    """Standarisasi jenis data, buang duplikasi, validasi 1000+ observasi."""
    missing = set(COLUMNS) - set(df.columns)
    if missing:
        raise ValueError(f"Kolom sumber tidak lengkap: {sorted(missing)}")
    cleaned = df[COLUMNS].copy()
    cleaned["country"] = cleaned["country"].astype("string").str.strip()
    cleaned["continent"] = cleaned["continent"].astype("string").str.strip()
    for col in ("year", "pop", "lifeExp", "gdpPercap"):
        cleaned[col] = pd.to_numeric(cleaned[col], errors="coerce")
    cleaned = cleaned.dropna(subset=COLUMNS)
    cleaned = cleaned.drop_duplicates(subset=["country", "year"])
    cleaned = cleaned[(cleaned["year"] >= 1900) & (cleaned["year"] <= 2100)]
    cleaned = cleaned[(cleaned["pop"] > 0) & cleaned["lifeExp"].between(0, 120) & (cleaned["gdpPercap"] > 0)]
    cleaned["year"] = cleaned["year"].astype(int)
    cleaned["pop"] = cleaned["pop"].astype("int64")
    cleaned = cleaned.sort_values(["country", "year"]).reset_index(drop=True)
    if len(cleaned) < 1000:
        raise ValueError(f"Data valid hanya {len(cleaned)} baris (<1000).")
    return cleaned


def main() -> None:
    parser = argparse.ArgumentParser(description="Scraper dataset Gapminder (minimal 1000 baris)")
    parser.add_argument("--offline", action="store_true", help="Validasi ulang dataset yang sudah disertakan tanpa internet")
    args = parser.parse_args()
    output = DATA_DIR / "gapminder_1704.csv"
    try:
        if args.offline:
            if not output.is_file():
                raise FileNotFoundError(f"Tidak ada file: {output}")
            print("Mode offline: memakai salinan dataset di folder data/.")
            source = pd.read_csv(output)
        else:
            print(f"Mengambil dataset dari: {URL}")
            source = download_csv()
        result = clean_and_validate(source)
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        result.to_csv(output, index=False, encoding="utf-8")
        print(f"SUKSES: {len(result):,} baris; {len(result.columns)} kolom")
        print(f"Negara: {result['country'].nunique()} | Tahun: {result['year'].min()}–{result['year'].max()}")
        print(f"File tersimpan: {output}")
    except (requests.RequestException, ValueError, OSError, pd.errors.ParserError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
