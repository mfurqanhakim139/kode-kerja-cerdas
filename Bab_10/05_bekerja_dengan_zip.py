import zipfile
from pathlib import Path
import os
import shutil # <--- TAMBAHKAN BARIS INI

# Persiapan file untuk di-zip
Path('file_untuk_zip_1.txt').write_text('Isi file 1.')
Path('folder_untuk_zip').mkdir(exist_ok=True)
Path('folder_untuk_zip/file_untuk_zip_2.txt').write_text('Isi file 2 di dalam folder.')

nama_zip = 'arsip_contoh.zip'
folder_ekstrak = Path('hasil_ekstrak')

# 1. Membuat file ZIP baru
try:
    print(f"\nMembuat file ZIP: {nama_zip}")
    # Gunakan mode 'w' untuk membuat zip baru (atau 'a' untuk menambah)
    # compress_type untuk mengaktifkan kompresi
    with zipfile.ZipFile(nama_zip, 'w', compresslevel=9, compression=zipfile.ZIP_DEFLATED) as zip_baru: # Tambah kompresi
        # Menambah file individual
        zip_baru.write('file_untuk_zip_1.txt', compress_type=zipfile.ZIP_DEFLATED)
        # Menambah file lain dengan path berbeda di dalam zip
        zip_baru.write(
            'folder_untuk_zip/file_untuk_zip_2.txt',
            arcname='data/file_penting.txt', # Nama/path di dalam zip
            compress_type=zipfile.ZIP_DEFLATED
        )
    print("File ZIP berhasil dibuat.")
except Exception as e:
    print(f"Gagal membuat ZIP: {e}")

# 2. Membaca isi file ZIP
try:
    print(f"\nMembaca isi file ZIP: {nama_zip}")
    with zipfile.ZipFile(nama_zip, 'r') as zip_baca:
        print("Isi file ZIP:")
        for nama_item in zip_baca.namelist():
            print(f"- {nama_item}")

        # Mengekstrak semua file
        print(f"\nMengekstrak semua ke folder: {folder_ekstrak}")
        # Pastikan folder ekstrak ada atau buat jika perlu
        folder_ekstrak.mkdir(exist_ok=True)
        zip_baca.extractall(folder_ekstrak)
        print("Ekstraksi selesai.")

except FileNotFoundError:
    print(f"Error: File ZIP '{nama_zip}' tidak ditemukan.")
except Exception as e:
    print(f"Gagal membaca/ekstrak ZIP: {e}")

# Cleanup (opsional - bagian ini akan menghapus file yang dibuat)
# Jika Anda ingin melihat hasilnya dulu, beri komentar pada baris-baris di bawah ini
print("\nMelakukan cleanup (menghapus file contoh)...")
try:
    if Path(nama_zip).exists():
        os.remove(nama_zip)
        print(f"- File '{nama_zip}' dihapus.")
    if Path('file_untuk_zip_1.txt').exists():
        Path('file_untuk_zip_1.txt').unlink()
        print("- File 'file_untuk_zip_1.txt' dihapus.")
    if Path('folder_untuk_zip').exists():
        shutil.rmtree('folder_untuk_zip') # Sekarang shutil sudah dikenal
        print("- Folder 'folder_untuk_zip' dihapus.")
    if folder_ekstrak.exists():
        shutil.rmtree(folder_ekstrak) # Sekarang shutil sudah dikenal
        print(f"- Folder '{folder_ekstrak}' dihapus.")
    print("Cleanup selesai.")
except Exception as e:
    print(f"Gagal melakukan cleanup: {e}")