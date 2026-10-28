
# Pertemuan 12 - File I/O dan Error Handling
Nama: Azkiah Safira
NIM: 2225250013
Kelas: 3F

## Tujuan

Pertemuan ini bertujuan untuk memahami konsep File Input/Output (File I/O) dalam Python, mulai dari membaca, menulis, hingga menambahkan data ke dalam file. Mahasiswa diharapkan mampu menggunakan fungsi `open()` dan context manager `with` untuk mengelola file dengan baik, serta memahami penggunaan mode file `r`, `w`, dan `a`.

Selain itu, mahasiswa diharapkan mampu menerapkan error handling menggunakan `try-except` untuk menangani kesalahan seperti `FileNotFoundError` dan `ValueError`. Melalui materi ini, mahasiswa juga mempelajari cara mengolah data dari file teks, menggunakan fungsi modular, melakukan pengujian program, serta mengelola hasil pekerjaan menggunakan GitHub.

## Struktur Program

```text
pertemuan 12 file io error handling/
├── README.md
├── .gitignore
├── latihan/
│   ├── 01_menulis_file.py
│   ├── 02_membaca_file.py
│   ├── 03_append_file.py
│   ├── 04_proses_baris_data.py
│   ├── 05_file_not_found.py
│   └── 06_value_error.py
├── praktik/
│   └── rekap_nilai.py
├── tugas/
│   └── tugas_5_rekap_nilai.py
└── data/
    ├── nilai.txt
    └── hasil_rekap.txt
```

Keterangan:

- `README.md`: Dokumentasi tujuan, struktur program, cara menjalankan, algoritma, hasil pengujian, dan refleksi.
- `.gitignore`: Mengatur file atau folder yang tidak perlu dimasukkan ke repositori Git.
- `latihan/`: Berisi enam program latihan tentang menulis file, membaca file, menambahkan data, memproses baris, dan menangani kesalahan.
- `praktik/rekap_nilai.py`: Program praktik untuk membaca dan mengolah data nilai mahasiswa.
- `tugas/tugas_5_rekap_nilai.py`: Program tugas untuk merekap data nilai dari file dan menyimpan hasil pengolahannya.
- `data/nilai.txt`: File masukan yang berisi data NIM dan nilai mahasiswa.
- `data/hasil_rekap.txt`: File keluaran yang menyimpan hasil rekapitulasi nilai.

## Cara Menjalankan

Pastikan Python sudah terpasang dan terminal berada pada folder `pertemuan 12 file io error handling`.

**1. Menjalankan program latihan**

```bash
python latihan/01_menulis_file.py
python latihan/02_membaca_file.py
python latihan/03_append_file.py
python latihan/04_proses_baris_data.py
python latihan/05_file_not_found.py
python latihan/06_value_error.py
```

**2. Menjalankan program praktik**

```bash
python praktik/rekap_nilai.py
```

**3. Menjalankan program tugas**

```bash
python tugas/tugas_5_rekap_nilai.py
```

**4. Memeriksa hasil program**

Buka file `data/hasil_rekap.txt` untuk melihat hasil rekapitulasi nilai yang telah diproses oleh program.

**5. Menyimpan perubahan ke GitHub**

```bash
git add .
git commit -m "Menambahkan latihan File I/O dan Error Handling"
git push
```

## Algoritma Tugas

Program Tugas 5 digunakan untuk membaca data nilai mahasiswa dari file teks, mengolah data yang valid, menghitung statistik nilai, dan menyimpan hasil rekapitulasi ke file keluaran.

1. Menentukan file masukan `data/nilai.txt` dan file keluaran `data/hasil_rekap.txt`.
2. Membuka file masukan menggunakan `with open()` dengan mode baca dan `encoding="utf-8"`.
3. Membaca isi file baris demi baris.
4. Menggunakan `strip()` untuk menghilangkan spasi dan karakter baris yang tidak diperlukan.
5. Melewati baris kosong agar tidak diproses.
6. Memisahkan NIM dan nilai menggunakan `split(",")`.
7. Mengubah nilai menjadi tipe numerik menggunakan `float()`.
8. Menangani kesalahan data menggunakan `try-except`, termasuk `ValueError` dan `FileNotFoundError`.
9. Menghitung jumlah data valid, rata-rata, nilai minimum, nilai maksimum, dan jumlah mahasiswa yang lulus dengan nilai minimal 60.
10. Menulis hasil rekapitulasi ke dalam file `data/hasil_rekap.txt`.

## Test Case

Pengujian dilakukan untuk memastikan program dapat memproses data dengan benar serta menangani kesalahan yang mungkin terjadi saat membaca dan mengolah file.

Contoh isi file `data/nilai.txt`:

```text
A001,85
A002,78
A003,92
A004,67
A005,88
```

| No. | Data/Input | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|
| 1 | File tersedia dan berisi data valid | Program membaca seluruh data dan menghitung rekapitulasi nilai | Diisi setelah pengujian | Belum diuji |
| 2 | File `nilai.txt` tidak ditemukan | Program menangani `FileNotFoundError` | Diisi setelah pengujian | Belum diuji |
| 3 | File berisi baris kosong | Baris kosong dilewati dan tidak mengganggu proses | Diisi setelah pengujian | Belum diuji |
| 4 | Baris data tidak sesuai format NIM dan nilai | Kesalahan format ditangani dan baris bermasalah tidak diproses sebagai data valid | Diisi setelah pengujian | Belum diuji |
| 5 | Nilai berisi karakter nonnumerik, misalnya `A006,abc` | Program menangani `ValueError` | Diisi setelah pengujian | Belum diuji |
| 6 | Data valid berhasil diproses | File keluaran berisi jumlah data valid, rata-rata, nilai minimum, nilai maksimum, dan jumlah mahasiswa lulus | Diisi setelah pengujian | Belum diuji |

## Refleksi

Melalui pertemuan ini, saya mempelajari cara membaca, menulis, dan menambahkan data ke dalam file menggunakan Python. Saya memahami perbedaan mode file `r`, `w`, dan `a`, serta pentingnya menggunakan `with open()` agar file dikelola dengan baik. Saya juga mempelajari penggunaan `strip()`, `split()`, dan konversi tipe data untuk mengolah informasi yang tersimpan dalam file teks.

Selain itu, saya memahami bahwa error handling diperlukan agar program dapat menangani kesalahan secara terstruktur. Penggunaan `try-except` membantu menangani kesalahan seperti file yang tidak ditemukan dan data nilai yang tidak sesuai. Melalui tugas rekapitulasi nilai, saya dapat menerapkan konsep File I/O dan Error Handling dalam program yang lebih terstruktur, sekaligus melatih kemampuan melakukan pengujian dan mengelola perubahan program menggunakan GitHub.