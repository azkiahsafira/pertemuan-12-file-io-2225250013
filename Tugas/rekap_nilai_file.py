# ============================================================
# PERTEMUAN 12 - FILE I/O DAN ERROR HANDLING
# Praktik: Rekapitulasi Nilai Mahasiswa
# ============================================================
# Deskripsi:
# Membaca data nilai dari file, menghitung statistik,
# dan menampilkan hasil rekapitulasi.
# ============================================================

from pathlib import Path

FILE_INPUT = Path("data/nilai.txt")


def baca_data(nama_file):
    """Membaca dan memvalidasi data dari file."""
    daftar_data = []

    with open(nama_file, "r", encoding="utf-8") as file:
        for nomor, baris in enumerate(file, start=1):
            baris = baris.strip()

            if not baris:
                continue

            try:
                nim, teks_nilai = baris.split(",")
                nilai = float(teks_nilai)

                daftar_data.append({
                    "nim": nim.strip(),
                    "nilai": nilai
                })

            except ValueError:
                print(f"Baris {nomor} dilewati: {baris}")

    return daftar_data


def tampilkan_rekap(daftar_data):
    """Menghitung dan menampilkan statistik nilai."""
    print("\n" + "=" * 48)
    print("              REKAP NILAI MAHASISWA")
    print("=" * 48)

    if not daftar_data:
        print("Tidak ada data valid untuk direkap.")
        print("=" * 48)
        return

    nilai = [data["nilai"] for data in daftar_data]

    print(f"{'Jumlah data':<24}: {len(nilai)}")
    print(f"{'Rata-rata nilai':<24}: {sum(nilai) / len(nilai):.2f}")
    print(f"{'Nilai minimum':<24}: {min(nilai):.2f}")
    print(f"{'Nilai maksimum':<24}: {max(nilai):.2f}")
    print(f"{'Jumlah mahasiswa lulus':<24}: {sum(n >= 60 for n in nilai)}")
    print("=" * 48)


def main():
    try:
        daftar_data = baca_data(FILE_INPUT)
        tampilkan_rekap(daftar_data)

    except FileNotFoundError:
        print(f"File masukan tidak ditemukan: {FILE_INPUT}")


if __name__ == "__main__":
    main()
