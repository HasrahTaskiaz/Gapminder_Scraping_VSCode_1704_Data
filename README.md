# Web Data Extraction: Perkembangan Ekonomi dan Kesehatan Dunia (Gapminder)

Proyek tugas *custom scraping / web data extraction* Python yang siap dibuka di **Visual Studio Code** dan diunggah ke GitHub.

## 1. Topik dan data

**Topik:** Hubungan pendapatan per kapita dengan angka harapan hidup pada berbagai negara di dunia.

Data berisi **1.704 baris dan 6 kolom**, mencakup **142 negara**, setiap 5 tahun dari **1952–2007**. Satu baris merepresentasikan satu negara pada satu tahun pengamatan. Data **historis**, bukan kondisi terbaru tahun 2026.

**Sumber publik:** [Plotly datasets — gapminderDataFiveYear.csv](https://github.com/plotly/datasets/blob/master/gapminderDataFiveYear.csv) (dikenal sebagai data Gapminder).

**Metode:** `requests` mengambil file CSV publik melalui HTTPS, `pandas` membaca dan mengolahnya. Ini *pengambilan data web dari CSV terstruktur*, **bukan** parsing elemen HTML/BeautifulSoup. Jelaskan metode ini secara jujur saat presentasi; bila dosen mewajibkan scraping halaman HTML, diskusikan penyesuaian sumber/metode.

## 2. Struktur proyek

```text
gapminder-scraping-vscode/
├── .vscode/launch.json      # Konfigurasi Run and Debug VS Code
├── data/gapminder_1704.csv # 1.704 baris data asli yang dibersihkan
├── docs/DOKUMENTASI.md     # Metode, kolom, alur, dan etika
├── src/scraper.py          # Kode custom extraction/scraping
├── tests/test_data.py     # Validasi kelengkapan dataset
├── requirements.txt
├── .gitignore
└── README.md
```

## 3. Menjalankan di Visual Studio Code

1. Ekstrak ZIP; pada VS Code pilih **File > Open Folder**, buka `gapminder-scraping-vscode`.
2. Pasang ekstensi **Python** dari Microsoft, lalu buka **Terminal > New Terminal**.
3. Buat virtual environment dan instal library:

   **Windows (PowerShell):**
   ```powershell
   py -m venv .venv
   .\.venv\Scripts\python.exe -m pip install -r requirements.txt
   .\.venv\Scripts\python.exe src/scraper.py
   ```
   **macOS / Linux:**
   ```bash
   python3 -m venv .venv
   .venv/bin/python -m pip install -r requirements.txt
   .venv/bin/python src/scraper.py
   ```
4. Script online akan mengunduh, memvalidasi, dan menulis `data/gapminder_1704.csv`. Hasilnya adalah 1.704 baris bila isi sumber tidak berubah.
5. Untuk menjalankan tanpa internet, ketik `python src/scraper.py --offline` setelah memilih interpreter `.venv` di VS Code, atau jalankan konfigurasi debug **Validasi Dataset Gapminder (offline)**.
6. Untuk cek hasil: `python tests/test_data.py`.

> **Penting:** Data CSV sudah disertakan dalam ZIP, jadi syarat 1.000 baris terpenuhi sebelum script dijalankan. Fitur unduh ulang membutuhkan internet.

## 4. Alur program

**URL CSV publik → HTTP GET (`requests`) → baca CSV (`pandas`) → validasi enam kolom → bersihkan null/duplikat/nilai tidak masuk akal → urutkan → ekspor CSV → hitung baris**.

Saat dijalankan, script memberi error dengan pesan yang jelas jika situs tidak bisa diakses, struktur kolom berubah, atau data valid kurang dari 1.000 baris. Tidak ada data palsu yang dibuat.

## 5. Unggah ke GitHub dan kumpulkan

Di GitHub klik **New repository** → beri nama misalnya `gapminder-data-scraping` → **Create repository**. Di VS Code buka Terminal, ketik:

```bash
git init
git add .
git commit -m "Tambah 1704 data Gapminder, script ekstraksi, dokumentasi"
git branch -M main
git remote add origin https://github.com/USERNAME/gapminder-data-scraping.git
git push -u origin main
```

Ganti `USERNAME` dengan username GitHub sendiri. Bila repositori dibuat dengan README otomatis atau sudah ada commit lain, gunakan opsi unggah file langsung ke repo kosong atau atur riwayat Git sebelum push. **Link repo baru ada setelah kamu mengunggahnya ke akun GitHub**, bukan dari ZIP ini.

## 6. Keterangan akademik

Data proyek adalah data sekunder terbuka dari repositori publik. **Sumber harus dicantumkan**; jangan mengklaim data berasal dari wawancara atau pengumpulan mandiri. Pengambilan file langsung dari raw CSV lebih stabil dibanding menyasar tampilan HTML GitHub.

Lihat [Dokumentasi lengkap](docs/DOKUMENTASI.md).
