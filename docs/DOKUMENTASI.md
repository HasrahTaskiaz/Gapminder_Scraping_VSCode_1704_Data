# DOKUMENTASI PENGAMBILAN DATA GAPMINDER

## A. Identitas pekerjaan

- **Judul:** Pengambilan Data Ekonomi dan Kesehatan Global melalui Ekstraksi CSV Web Menggunakan Python.
- **Topik:** Analisis deskriptif hubungan PDB per kapita dan angka harapan hidup.
- **Sumber:** https://github.com/plotly/datasets/blob/master/gapminderDataFiveYear.csv
- **Data:** 1.704 observasi; 142 negara; tahun 1952–2007; periode lima tahunan.
- **Format:** CSV (comma separated values).
- **Perangkat:** Visual Studio Code; Python; `requests`; `pandas`.

## B. Tujuan

Mengumpulkan dan menyiapkan lebih dari 1.000 baris data dari sumber web publik dalam satu tema, sambil menuliskan skrip Python yang dapat dijalankan ulang dan mendokumentasikan proses, kualitas data, serta sumbernya.

## C. Variabel

| Kolom | Tipe | Arti |
| --- | --- | --- |
| `country` | Teks | Nama negara |
| `year` | Bilangan bulat | Tahun pengamatan |
| `pop` | Bilangan bulat | Perkiraan jumlah penduduk |
| `continent` | Teks | Benua |
| `lifeExp` | Bilangan desimal | Angka harapan hidup dalam tahun |
| `gdpPercap` | Bilangan desimal | PDB per kapita dalam satuan mata uang dolar pada dataset sumber |

> Catatan: Kolom `gdpPercap` historis tidak otomatis setara dengan indikator nominal USD terkini. Periksa definisi perhitungan historis sumber sebelum melakukan perbandingan ekonomi lintas negara atau dengan angka terbaru.

## D. Tahapan kerja

1. Menetapkan satu tema dan memilih data terstruktur publik yang mencakup lebih dari 1.000 observasi.
2. Menyediakan tautan CSV mentah dari repositori Plotly.
3. Mengambil data menggunakan permintaan HTTP GET dari modul `requests` dengan *timeout* dan pemeriksaan kode respons.
4. Memasukkan hasil unduhan ke DataFrame `pandas` melalui parser CSV.
5. Memeriksa keberadaan enam kolom wajib: `country`, `year`, `pop`, `continent`, `lifeExp`, dan `gdpPercap`.
6. Menstandarkan teks, memastikan tipe numerik, membuang baris kosong, duplikat pasangan negara–tahun, dan nilai tidak masuk akal.
7. Mengurutkan hasil berdasarkan negara dan tahun.
8. Menolak hasil bila kurang dari 1.000 baris, lalu mengekspor hasil ke `data/gapminder_1704.csv`.
9. Menguji jumlah baris, kolom, negara, nilai kosong dan duplikat melalui `tests/test_data.py`.

## E. Bukti hasil dan pemeriksaan

Dataset yang **sudah disertakan dalam paket proyek** memiliki:

- **1.704 baris data** di luar header.
- **6 kolom**.
- **142 nama negara** unik.
- **12 titik tahun** (1952, 1957, ..., 2007).
- Unit observasi **negara–tahun**; bukan 1.704 negara berbeda.

Jalankan `python tests/test_data.py` untuk mengulangi pemeriksaan dasar. Proyek juga menyediakan mode `--offline` untuk memvalidasi data terlampir tanpa perlu mengunduh ulang.

## F. Batasan

Dataset adalah **historis** (berakhir 2007), tidak mewakili tahun 2026. Data bukan hasil scraping HTML; tekniknya ekstraksi dari berkas CSV berbasis web. Jumlah catatan bisa berubah bila pemilik repositori mengubah file sumber; skrip akan memeriksa paling sedikit 1.000 baris. Korelasi antara pendapatan dan harapan hidup tidak otomatis membuktikan hubungan sebab akibat.

## G. Etika dan atribusi

Hanya mengambil berkas data yang dipublikasikan secara terbuka. Tidak mengambil informasi pribadi, tidak melewati autentikasi, dan tidak mengirim permintaan berulang dalam loop. Cantumkan tautan ke berkas sumber dan lisensi/ketentuan redistribusi yang berlaku. Untuk dataset Gapminder secara umum, lihat https://www.gapminder.org/data/ .

## H. Contoh narasi untuk laporan

"Penelitian mini ini menggunakan data sekunder Gapminder yang tersedia pada repositori dataset Plotly. Pengumpulan dilakukan melalui ekstraksi file CSV publik menggunakan pustaka requests pada Python, kemudian pandas digunakan untuk pembacaan dan pembersihan data. Dataset akhir terdiri dari 1.704 baris yang mencatat karakteristik kependudukan, PDB per kapita, dan angka harapan hidup dari 142 negara pada periode 1952–2007. Pengujian data meliputi jumlah baris minimal 1.000, kelengkapan kolom, nilai kosong, serta duplikasi pasangan negara dan tahun."
