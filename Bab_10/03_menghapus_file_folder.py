import shutil
from pathlib import Path
import send2trash # Pastikan sudah diinstal: pip install send2trash

# Persiapan
Path('hapus_file_aman.txt').write_text('File untuk dikirim ke trash.')
Path('hapus_folder_aman').mkdir(exist_ok=True)
Path('hapus_folder_aman/dummy.txt').touch() # Buat file dummy di dalam folder

# 1. Menggunakan send2trash (Cara Aman)
try:
    print("Mengirim 'hapus_file_aman.txt' ke Trash...")
    send2trash.send2trash('hapus_file_aman.txt')
    print("Mengirim 'hapus_folder_aman' ke Trash...")
    send2trash.send2trash('hapus_folder_aman')
    print("Berhasil mengirim ke Trash (cek Recycle Bin/Trash Anda).")
except Exception as e:
    print(f"Gagal mengirim ke Trash: {e}")

# 2. Contoh Hapus Permanen (Aksi di-komen untuk keamanan)
file_hapus_permanen = Path('file_hapus_permanen.txt')
file_hapus_permanen.touch()
folder_kosong_hapus = Path('folder_kosong_hapus')
folder_kosong_hapus.mkdir(exist_ok=True)
folder_isi_hapus = Path('folder_isi_hapus')
folder_isi_hapus.mkdir(exist_ok=True)
(folder_isi_hapus / 'isi.txt').touch()

file_hapus_permanen.unlink() # Hapus file permanen
print(f"File {file_hapus_permanen} akan dihapus permanen (aksi di-komen).")
folder_kosong_hapus.rmdir() # Hapus folder kosong permanen
print(f"Folder {folder_kosong_hapus} akan dihapus permanen (aksi di-komen).")
shutil.rmtree(folder_isi_hapus) # Hapus folder dan isi permanen (BERBAHAYA!)
print(f"Folder {folder_isi_hapus} akan dihapus permanen (aksi di-komen).")

