import os
from pathlib import Path

# Persiapan: Buat struktur folder contoh
Path('folder_utama').mkdir(exist_ok=True)
Path('folder_utama/file_utama.txt').touch()
Path('folder_utama/sub1').mkdir(exist_ok=True)
Path('folder_utama/sub1/file_sub1.txt').touch()
Path('folder_utama/sub2').mkdir(exist_ok=True)
Path('folder_utama/sub2/file_sub2a.txt').touch()
Path('folder_utama/sub2/file_sub2b.log').touch()

print("Menjelajahi 'folder_utama' dengan os.walk():")
for nama_folder, list_subfolder, list_file in os.walk('folder_utama'):
    print(f"\nSedang berada di folder: {nama_folder}")
    print(f"  Subfolder di dalamnya: {list_subfolder}")
    print(f"  File di dalamnya: {list_file}")

    # Contoh aksi: Rename file .txt menjadi .bak di setiap folder
    for nama_file in list_file:
           if nama_file.endswith('.txt'):
            path_lama = Path(nama_folder) / nama_file
            path_baru = path_lama.with_suffix('.bak')
            print(f"    -> Merename {path_lama} menjadi {path_baru} (aksi di-komen)")
            os.rename(path_lama, path_baru) # Hati-hati saat mencoba rename!
