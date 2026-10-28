
# ============================================================
# PERTEMUAN 12 - FILE I/O DAN ERROR HANDLING
# Latihan 03: Menambahkan Data ke File
# ============================================================
# Deskripsi:
# Menambahkan teks menggunakan mode "a" tanpa menghapus
# data yang sudah tersimpan sebelumnya.
# ============================================================

from pathlib import Path

FILE_OUTPUT = Path("data/hasil_latihan.txt")


def tambah_data():
    """Menambahkan baris baru ke dalam file."""
    FILE_OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    with open(FILE_OUTPUT, "a", encoding="utf-8") as file:
        file.write("Data tambahan berhasil disimpan.\n")

    print("=" * 45)
    print("             MENAMBAHKAN DATA")
    print("=" * 45)
    print(f"File keluaran : {FILE_OUTPUT}")
    print("Mode          : Append (a)")
    print("Status        : Berhasil")
    print("=" * 45)


if __name__ == "__main__":
    tambah_data()
