from PIL import Image
from pathlib import Path

# Pastikan Anda punya file gambar contoh, misal 'kucing.jpg'
# Jika tidak, script ini mungkin error saat Image.open()
nama_file_sumber = 'kucing.jpg' # Ganti dengan nama file gambar Anda
path_gambar = Path(nama_file_sumber)

if path_gambar.exists():
    try:
        # Membuka gambar
        img = Image.open(nama_file_sumber)
        print(f"Berhasil membuka: {img.filename}")

        # Mendapatkan informasi
        lebar, tinggi = img.size
        print(f"Ukuran: {lebar}x{tinggi}")
        print(f"Format: {img.format} ({img.format_description})")

        # Menyimpan dengan nama/format berbeda (contoh: PNG)
        nama_file_baru = 'kucing_output.png'
        img.save(nama_file_baru)
        print(f"Gambar disimpan sebagai: {nama_file_baru}")

        # Membuat gambar baru (misal: kotak merah 100x100)
        img_baru = Image.new('RGBA', (100, 100), 'red')
        img_baru.save('kotak_merah.png')
        print("Gambar kotak merah dibuat.")

    except Exception as e:
        print(f"Terjadi error: {e}")
else:
    print(f"Error: File gambar '{nama_file_sumber}' tidak ditemukan.")

