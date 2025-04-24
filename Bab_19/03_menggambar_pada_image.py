from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

# Buat gambar kanvas putih baru
lebar_kanvas, tinggi_kanvas = 300, 200
img = Image.new('RGB', (lebar_kanvas, tinggi_kanvas), 'white')

# Buat objek Draw
draw = ImageDraw.Draw(img)

# Gambar garis diagonal merah
draw.line([(0, 0), (lebar_kanvas - 1, tinggi_kanvas - 1)], fill='red', width=3)
# Gambar kotak biru tanpa isi
draw.rectangle((50, 50, 150, 100), outline='blue', width=2)
# Gambar lingkaran hijau terisi
draw.ellipse((200, 100, 280, 180), fill='lightgreen', outline='black')

# Menulis teks (perlu file font .ttf)
try:
    # Ganti 'arial.ttf' dengan path ke file font valid di sistem Anda
    # Jika tidak punya, cari dan unduh font .ttf (misal: DejaVuSans)
    font_path = 'AB.ttf' # Ganti jika perlu
    if not Path(font_path).exists():
         # Fallback ke font default Pillow jika ttf tidak ada (mungkin kurang bagus)
         print("File font tidak ditemukan, menggunakan font default.")
         font_path = None # atau coba path font sistem jika tahu
         ukuran_font = 20
         font_obj = ImageFont.load_default() # Font default bitmap
         # Jika font default, sesuaikan posisi Y agar pas
         pos_y_text = tinggi_kanvas // 2 - 10
    else:
         ukuran_font = 30
         font_obj = ImageFont.truetype(font_path, ukuran_font)
         pos_y_text = tinggi_kanvas // 2 - (ukuran_font // 2) # Tengah vertikal

    teks = "Halo Pillow!"
    # Dapatkan ukuran teks untuk penempatan tengah horizontal (perkiraan)
    # text_width, text_height = draw.textlength(teks, font=font_obj) # textlength lebih akurat
    # Atau cara lama: text_bbox = draw.textbbox((0,0), teks, font=font_obj) -> (left,top,right,bottom)
    # text_width = text_bbox[2] - text_bbox[0]
    # text_height = text_bbox[3] - text_bbox[1]
    # Posisi x agak manual karena textlength mungkin belum ada di semua versi / font default
    pos_x_text = 10 #lebar_kanvas // 2 - text_width // 2


    draw.text((pos_x_text, pos_y_text), teks, fill='black', font=font_obj)

except IOError:
    print(f"Error: Tidak bisa memuat file font '{font_path}'. Menggambar tanpa teks.")
except Exception as e:
    print(f"Error saat menulis teks: {e}. Menggambar tanpa teks.")


# Simpan hasil
img.save('gambar_hasil_draw.png')
print("Gambar hasil drawing disimpan.")
