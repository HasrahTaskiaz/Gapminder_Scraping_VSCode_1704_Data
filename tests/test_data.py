"""Pengujian sederhana dataset yang dikumpulkan."""
from pathlib import Path
import pandas as pd

csv_path = Path(__file__).resolve().parents[1] / "data" / "gapminder_1704.csv"
df = pd.read_csv(csv_path)
assert len(df) >= 1000, "Jumlah baris kurang dari 1.000"
assert df.shape[1] == 6, "Kolom yang diharapkan ada 6"
assert not df.isna().any().any(), "Terdapat nilai kosong"
assert not df.duplicated(["country", "year"]).any(), "Ada data negara-tahun duplikat"
assert df["country"].nunique() == 142, "Jumlah negara berbeda dari dataset sumber"
print(f"LULUS: {len(df)} baris, {len(df.columns)} kolom, {df['country'].nunique()} negara")
