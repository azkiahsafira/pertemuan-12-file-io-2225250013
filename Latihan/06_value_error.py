
# ============================================================
# PERTEMUAN 12 - FILE I/O DAN ERROR HANDLING
# Latihan 06: ValueError
# ============================================================
# Deskripsi:
# Menangani kesalahan ketika teks tidak dapat dikonversi
# menjadi angka.
# ============================================================


def konversi_nilai(teks):
    """Mengonversi teks menjadi angka."""
    try:
        nilai = float(teks)

    except ValueError:
        print(f"Input '{teks}' tidak valid.")
        print("Nilai harus berupa angka.")

    else:
        print(f"Input '{teks}' berhasil dikonversi: {nilai:.2f}")

    finally:
        print("-" * 45)


if __name__ == "__main__":
    print("=" * 45)
    print("             VALIDASI NILAI")
    print("=" * 45)

    konversi_nilai("85")
    konversi_nilai("delapan puluh")

    print("Program selesai.")
    print("=" * 45)
