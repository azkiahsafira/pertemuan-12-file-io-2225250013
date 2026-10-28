
# ============================================================
# PERTEMUAN 12 - FILE I/O DAN ERROR HANDLING
# Latihan 02: Membaca File
# ============================================================
# Deskripsi:
# Membaca seluruh isi file menggunakan metode read().
# ============================================================

from pathlib import Path

FILE_INPUT = Path("data/hasil_latihan.txt")


def baca_file():
    """Membaca isi file teks."""
    try:
        with open(FILE_INPUT, "r", encoding="utf-8") as file:
            isi_file = file.read()

        print("=" * 45)
        print("               MEMBACA FILE")
        print("=" * 45)
        print(isi_file)
        print("=" * 45)

    except FileNotFoundError:
        print(f"File tidak ditemukan: {FILE_INPUT}")


if __name__ == "__main__":
    baca_file()
