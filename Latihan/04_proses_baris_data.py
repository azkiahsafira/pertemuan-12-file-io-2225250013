
# ============================================================
# PERTEMUAN 12 - FILE I/O DAN ERROR HANDLING
# Latihan 04: Memproses Baris Data
# ============================================================
# Deskripsi:
# Membaca data nilai, memisahkan NIM dan nilai, lalu
# mengonversi nilai menjadi tipe numerik.
# ============================================================

from pathlib import Path

FILE_INPUT = Path("data/nilai.txt")


def proses_data():
    """Membaca dan memproses data nilai mahasiswa."""
    daftar_nilai = []

    try:
        with open(FILE_INPUT, "r", encoding="utf-8") as file:
            for nomor, baris in enumerate(file, start=1):
                baris = baris.strip()

                if not baris:
                    continue

                try:
                    nim, teks_nilai = baris.split(",")
                    nilai = float(teks_nilai)
                    daftar_nilai.append(nilai)

                    print(f"{nomor:>2}. {nim.strip():<12} {nilai:>7.2f}")

                except ValueError:
                    print(f"{nomor:>2}. Data tidak valid: {baris}")

        print("=" * 45)
        print("            HASIL PENGOLAHAN")
        print("=" * 45)

        if daftar_nilai:
            rata_rata = sum(daftar_nilai) / len(daftar_nilai)
            print(f"Jumlah data : {len(daftar_nilai)}")
            print(f"Rata-rata   : {rata_rata:.2f}")
        else:
            print("Tidak ada data valid untuk diproses.")

        print("=" * 45)

    except FileNotFoundError:
        print(f"File tidak ditemukan: {FILE_INPUT}")


if __name__ == "__main__":
    print("=" * 45)
    print("           PEMROSESAN DATA NILAI")
    print("=" * 45)
    proses_data()
