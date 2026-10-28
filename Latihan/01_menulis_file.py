
# ============================================================
# PERTEMUAN 12 - FILE I/O DAN ERROR HANDLING
# Latihan 01: Menulis File
# ============================================================
# Deskripsi:
# Menulis data teks ke dalam file menggunakan mode "w".
# ============================================================

from pathlib import Path

FILE_OUTPUT = Path("data/hasil_latihan.txt")


def tulis_file():
    """Menulis data ke dalam file teks."""
    FILE_OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    with open(FILE_OUTPUT, "w", encoding="utf-8") as file:
        file.write("PRAKTIK FILE I/O\n")
        file.write("================\n")
        file.write("Belajar menulis data menggunakan Python.\n")
        file.write("Data disimpan ke dalam file teks.\n")

    print("=" * 45)
    print("              MENULIS FILE")
    print("=" * 45)
    print(f"File keluaran : {FILE_OUTPUT}")
    print("Status        : Berhasil")
    print("=" * 45)


if __name__ == "__main__":
    tulis_file()
