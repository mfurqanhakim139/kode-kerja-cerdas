from pathlib import Path
import os # Masih berguna untuk hal seperti os.chdir() jika diperlukan

# Membuat objek Path (otomatis sesuai OS)
p1 = Path('data_input/laporan_bulanan.txt')
p2 = Path('C:/Users/Admin/Documents') # Contoh path absolut Windows
p3 = Path('/home/user/data') # Contoh path absolut Linux/macOS

# Menggabungkan path dengan aman
folder_utama = Path('proyek_penting')
path_file = folder_utama / 'hasil' / 'output.txt'
print(f"Path gabungan: {path_file}") # Hasilnya akan sesuai format OS Anda

# Direktori kerja saat ini dan home
cwd = Path.cwd()
home = Path.home()
print(f"Direktori kerja: {cwd}")
print(f"Direktori home: {home}")

# Membuat path absolut dari path relatif
path_absolut_file = path_file.resolve() # Atau .absolute()
print(f"Path absolut: {path_absolut_file}")

# Mendapatkan bagian-bagian path
print(f"Nama file: {path_file.name}")
print(f"Ekstensi: {path_file.suffix}")
print(f"Nama tanpa ekstensi: {path_file.stem}")
print(f"Folder induk: {path_file.parent}")

# Membuat direktori (jika belum ada)
folder_output = Path('hasil_output')
folder_output.mkdir(exist_ok=True) # exist_ok=True agar tidak error jika sudah ada
print(f"Folder '{folder_output}' ada: {folder_output.exists()}")

# (Catatan: Modul 'os' masih berguna, misal os.getcwd(), os.chdir())
# print(f"CWD via os: {os.getcwd()}")
