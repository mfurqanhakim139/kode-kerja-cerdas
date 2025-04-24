from pathlib import Path

path_tulis = Path('hasil_tulisan.txt')
path_tambah = Path('log_tambahan.txt')

# --- Menulis (mode 'w' - Hapus isi lama jika ada) ---
print(f"--- Menulis ke '{path_tulis}' (mode 'w') ---")
try:
    with open(path_tulis, mode='w', encoding='utf-8') as file_tulis:
        file_tulis.write("Ini adalah baris pertama yang ditulis.\n")
        file_tulis.write("Menulis baris kedua.\n")
        angka = 123
        file_tulis.write(f"Menulis angka sebagai string: {angka}\n")
    print(f"Berhasil menulis ke '{path_tulis}'.")
except Exception as e:
    print(f"Gagal menulis file: {e}")

# --- Menambah (mode 'a' - Tambah di akhir) ---
print(f"\n--- Menambah ke '{path_tambah}' (mode 'a') ---")
try:
    with open(path_tambah, mode='a', encoding='utf-8') as file_tambah:
        import datetime
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file_tambah.write(f"Log entry pada {timestamp}: Proses selesai.\n")
    print(f"Berhasil menambah log ke '{path_tambah}'.")

    # Tambah lagi
    with open(path_tambah, mode='a', encoding='utf-8') as file_tambah:
         file_tambah.write("Menambahkan catatan lain.\n")
    print(f"Berhasil menambah log lagi ke '{path_tambah}'.")

except Exception as e:
    print(f"Gagal menambah file: {e}")
