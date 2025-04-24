# Perlu install: pip install ezsheets
# Pastikan juga setup kredensial Google API sudah selesai
# dan file credentials.json/credentials-sheets.json ada di folder ini.

import ezsheets
import sys

# --- Konfigurasi ---
# ID Spreadsheet Anda
ID_atau_URL_atau_Judul = "1GNokDQToXnEmcd8PZ6LJxEb5CbOL5s6ALVHAmaTXpX8"
# --------------------

try:
    print(f"Mencoba mengakses Spreadsheet: {ID_atau_URL_atau_Judul}...")
    ss = ezsheets.Spreadsheet(ID_atau_URL_atau_Judul)
    # Ambil sheet pertama (indeks 0)
    sheet = ss[0]
    print(f"Berhasil terhubung ke Spreadsheet: '{ss.title}'")
    print(f"Membaca dari sheet: '{sheet.title}'")

    # Baca cell A1 (kolom 1, baris 1)
    # ezsheets mengembalikan string, bahkan untuk angka
    nilai_a1 = sheet['A1']
    print(f"\nNilai A1: '{nilai_a1}' (Tipe: {type(nilai_a1)})")

    # Baca cell C2 menggunakan get(kolom, baris)
    # Kolom C adalah kolom ke-3, jadi gunakan indeks 3
    kolom_c_idx = 3
    baris_2_idx = 2
    nilai_c2 = sheet.get(kolom_c_idx, baris_2_idx)
    print(f"Nilai C2 (Kolom {kolom_c_idx}, Baris {baris_2_idx}): '{nilai_c2}'")

    # Baca baris pertama (baris 1)
    baris_1 = sheet.getRow(1)
    print(f"\nNilai Baris 1: {baris_1}")

    # Baca kolom B (kolom 2)
    kolom_b_idx = 2
    kolom_b = sheet.getColumn(kolom_b_idx)
    print(f"\nNilai Kolom B (indeks {kolom_b_idx}), 5 baris pertama: {kolom_b[:5]}")

    # Baca semua data (hati-hati jika sheet besar)
    # print("\nMembaca semua data (getRows)...")
    # semua_data = sheet.getRows()
    # print(f"Total baris data dibaca: {len(semua_data)}")
    # if len(semua_data) > 0:
    #     print(f"Contoh 2 baris data pertama: {semua_data[:2]}")

except ImportError:
    print("Error: Library 'ezsheets' belum terinstal.")
    print("Silakan instal dengan: pip install ezsheets")
except ezsheets.EZSheetsException as ez_err:
    # Menangkap error spesifik dari ezsheets (termasuk autentikasi/tidak ditemukan)
    print(f"\nError ezsheets: {ez_err}")
    print("Pastikan ID/URL/Judul benar, setup API selesai, kredensial valid,")
    print("dan akun Google yang terotentikasi punya akses ke Spreadsheet.")
except Exception as e:
    print(f"\nGagal membaca data. Terjadi error lain: {e}")
    print(f"Tipe error: {type(e)}")

print("\nSkrip selesai.")