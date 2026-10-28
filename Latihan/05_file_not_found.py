
# ============================================================
# PERTEMUAN 12 - FILE I/O DAN ERROR HANDLING
# Latihan 05: FileNotFoundError
# ============================================================
# Deskripsi:
# Menangani kesalahan ketika file yang ingin dibaca
# tidak ditemukan.
# ============================================================

from pathlib import Path

FILE_INPUT = Path("data/file_tidak_ada.txt")


def periksa_file():
    """Memeriksa keberadaan file melalui proses pembacaan."""
    print("=" * 45)
    print("           PEMERIKSAAN FILE")
    print("=" * 45)

    try:
        with open(FILE_INPUT, "r", encoding="utf-8") as file:
            print(file.read())

    except FileNotFoundError:
        print("Status : File tidak ditemukan.")
        print(f"Lokasi : {FILE_INPUT}")

    else:
        print("Status : File berhasil dibaca.")

    finally:
        print("-" * 45)
        print("Pemeriksaan selesai.")
        print("=" * 45)


if __name__ == "__main__":
    periksa_file()
