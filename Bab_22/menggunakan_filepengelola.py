# Contoh Penggunaan Class FilePengelola setelah diimpor
from pathlib import Path
import glob # Untuk pencarian pola sederhana
import os # Diperlukan jika ingin menggunakan os.rename atau fitur os lain
# import shutil # Diperlukan jika menambah metode pindah/hapus folder
# import send2trash # Diperlukan jika menambah metode hapus ke trash

try:
    from definisi_class_filepengelola import FilePengelola
except ImportError:
    print("="*50)
    print("PERINGATAN: Gagal mengimpor 'FilePengelola'.")
    print("Pastikan file 'Bab_22/01_definisi_class_filepengelola.py' ada dan berisi definisi class.")
    print("Contoh penggunaan di bawah ini mungkin tidak akan berjalan.")
    print("="*50)
    # Definisikan class dummy agar contoh tidak langsung error, tapi beri tahu pengguna
    class FilePengelola:
        def __init__(self, path): print(f"Error: Class FilePengelola tidak bisa diimpor. Membuat dummy untuk path {path}.")
        def hitung_item(self, *args, **kwargs): return 0
        def daftar_file(self, *args, **kwargs): return ["(Gagal Import)"]
        def cari_file_pola(self, *args, **kwargs): return ["(Gagal Import)"]
        def buat_subfolder(self, *args, **kwargs): print("(Gagal Import)"); return False
        folder_target = Path("(Gagal Import)") # Atribut dummy


if __name__ == "__main__":
    print("Menjalankan contoh penggunaan FilePengelola...")

    try:
        # Buat objek untuk mengelola folder 'Dokumen_Saya'
        folder_dokumen = 'Dokumen_Saya'
        # Sekarang menggunakan class yang (seharusnya) diimpor
        pengelola_dokumen = FilePengelola(folder_dokumen)

        # Buat objek lain untuk folder 'Gambar_Liburan'
        folder_gambar = 'Gambar_Liburan'
        pengelola_gambar = FilePengelola(folder_gambar)

        # Buat beberapa file dummy untuk pengujian di dalam folder masing-masing
        print("\nMembuat file dummy...")
        (pengelola_dokumen.folder_target / 'laporan.txt').touch(exist_ok=True)
        (pengelola_dokumen.folder_target / 'presentasi.pptx').touch(exist_ok=True)
        (pengelola_gambar.folder_target / 'foto1.jpg').touch(exist_ok=True)
        (pengelola_gambar.folder_target / 'foto2.jpg').touch(exist_ok=True)
        (pengelola_gambar.folder_target / 'catatan.txt').touch(exist_ok=True)
        print("File dummy selesai dibuat.")

        # Gunakan metode dari objek pengelola_dokumen
        print(f"\n--- Operasi pada Folder: {pengelola_dokumen.folder_target} ---")
        print(f"Jumlah file: {pengelola_dokumen.hitung_item()}")
        daftar_dokumen = pengelola_dokumen.daftar_file()
        print(f"Daftar file: {daftar_dokumen if daftar_dokumen else '(Kosong)'}")
        file_txt_dokumen = pengelola_dokumen.cari_file_pola('*.txt')
        print(f"File txt: {file_txt_dokumen if file_txt_dokumen else '(Tidak ada)'}")
        pengelola_dokumen.buat_subfolder('Arsip')

        # Gunakan metode dari objek pengelola_gambar
        print(f"\n--- Operasi pada Folder: {pengelola_gambar.folder_target} ---")
        print(f"Jumlah file: {pengelola_gambar.hitung_item()}")
        file_jpg_gambar = pengelola_gambar.cari_file_pola('*.jpg')
        print(f"File jpg: {file_jpg_gambar if file_jpg_gambar else '(Tidak ada)'}")
        pengelola_gambar.buat_subfolder('Favorit')

    except NameError:
         # Ini akan terjadi jika import gagal dan class dummy tidak terdefinisi
         print("\nError: Class 'FilePengelola' tidak terdefinisi. Pastikan import berhasil.")
    except ValueError as ve:
         print(f"Gagal membuat objek FilePengelola: {ve}")
    except Exception as e:
         print(f"Terjadi error saat menjalankan contoh: {e}")

    print("\nContoh penggunaan selesai.")
