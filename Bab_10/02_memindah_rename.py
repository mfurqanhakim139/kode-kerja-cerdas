import shutil
from pathlib import Path

# Persiapan
Path('untuk_dipindah').mkdir(exist_ok=True)
Path('untuk_dipindah/file_pindah.txt').write_text('File ini akan dipindah.')
Path('folder_tujuan_pindah').mkdir(exist_ok=True)

# 1. Memindahkan file ke folder lain
try:
    hasil_pindah = shutil.move('untuk_dipindah/file_pindah.txt', 'folder_tujuan_pindah')
    print(f"File dipindah ke: {hasil_pindah}") # Nama file tetap sama di folder tujuan
except Exception as e:
    print(f"Gagal memindahkan: {e}")

# 2. Mengganti nama file (memindahkan ke nama baru di lokasi sama/berbeda)
try:
    Path('file_rename_lama.txt').write_text('File untuk rename.')
    hasil_rename = shutil.move('file_rename_lama.txt', 'file_rename_BARU.txt')
    print(f"File direname menjadi: {hasil_rename}")
except Exception as e:
    print(f"Gagal rename: {e}")

# 3. Memindahkan folder
try:
    hasil_pindah_folder = shutil.move('untuk_dipindah', 'folder_tujuan_pindah/folder_hasil_pindah')
    print(f"Folder dipindah ke: {hasil_pindah_folder}")
except Exception as e:
    print(f"Gagal memindahkan folder: {e}")
