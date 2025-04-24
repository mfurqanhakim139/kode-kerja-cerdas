from PIL import Image
from pathlib import Path

nama_file_sumber = 'kucing.jpg' # Ganti dengan nama file gambar Anda
path_gambar = Path(nama_file_sumber)

if path_gambar.exists():
    try:
        img = Image.open(nama_file_sumber)
        lebar, tinggi = img.size
        print(f"Gambar asli: {img.filename}, Ukuran: {lebar}x{tinggi}")

        # 1. Crop (ambil bagian tengah 100x100, asumsi gambar cukup besar)
        left = (lebar - 100) // 2
        top = (tinggi - 100) // 2
        right = left + 100
        bottom = top + 100
        img_crop = img.crop((left, top, right, bottom))
        img_crop.save('kucing_crop.png')
        print("Gambar hasil crop disimpan.")

        # 2. Copy & Paste (buat kanvas baru, paste hasil crop ke sana)
        img_kanvas = Image.new('RGBA', (200, 150), 'lightblue')
        img_kanvas.paste(img_crop, (50, 25)) # Paste di koordinat (50, 25)
        img_kanvas.save('kucing_paste.png')
        print("Gambar hasil paste disimpan.")

        # 3. Resize (perkecil jadi lebar 300, tinggi proporsional)
        rasio = min(300 / lebar, 300 / tinggi) # Ambil rasio terkecil agar muat
        lebar_baru = int(lebar * rasio)
        tinggi_baru = int(tinggi * rasio)
        img_resize = img.resize((lebar_baru, tinggi_baru))
        img_resize.save('kucing_resize.png')
        print(f"Gambar hasil resize ({lebar_baru}x{tinggi_baru}) disimpan.")

        # 4. Rotate 90 derajat
        img_rotate = img.rotate(90, expand=True) # expand=True agar tidak terpotong
        img_rotate.save('kucing_rotate90.png')
        print("Gambar hasil rotate disimpan.")

        # 5. Flip Horizontal
        img_flip = img.transpose(Image.FLIP_LEFT_RIGHT)
        img_flip.save('kucing_flip_lr.png')
        print("Gambar hasil flip disimpan.")

    except Exception as e:
        print(f"Terjadi error: {e}")
else:
    print(f"Error: File gambar '{nama_file_sumber}' tidak ditemukan.")
