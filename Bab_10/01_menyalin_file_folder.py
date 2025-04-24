import shutil
from pathlib import Path

# Persiapan: Buat file dan folder sumber (jika belum ada)
Path('sumber').mkdir(exist_ok=True)
Path('sumber/file_asli.txt').write_text('Ini file asli.', encoding='utf-8')
Path('sumber/subfolder').mkdir(exist_ok=True)
Path('sumber/subfolder/file_lain.txt').write_text('File di subfolder.', encoding='utf-8')

# 1. Menyalin satu file
try:
    tujuan_file = Path('tujuan_copy')
    tujuan_file.mkdir(exist_ok=True) # Pastikan folder tujuan ada
    path_hasil_copy = shutil.copy('sumber/file_asli.txt', tujuan_file)
    print(f"File berhasil disalin ke: {path_hasil_copy}")

    # Menyalin dan rename
    path_hasil_rename = shutil.copy('sumber/file_asli.txt', tujuan_file / 'file_salinan_baru.txt')
    print(f"File berhasil disalin dan rename ke: {path_hasil_rename}")

except Exception as e:
    print(f"Gagal menyalin file: {e}")

# 2. Menyalin seluruh folder tree
folder_tujuan_tree = Path('tujuan_copytree')
# Hapus dulu jika sudah ada (untuk demo, hati-hati!)
if folder_tujuan_tree.exists():
    shutil.rmtree(folder_tujuan_tree) # Hapus folder tujuan lama jika ada
try:
    shutil.copytree('sumber', folder_tujuan_tree)
    print(f"Folder 'sumber' berhasil disalin ke '{folder_tujuan_tree}'")
except FileExistsError:
    print(f"Error: Folder tujuan '{folder_tujuan_tree}' sudah ada.")
except Exception as e:
    print(f"Gagal menyalin folder tree: {e}")

