import re

# 1. Compile pola: mencari nomor telepon format XXX-XXX-XXXX
#    Gunakan raw string r'...'
pola_telepon = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # \d artinya digit

# Teks target
teks = "Silakan hubungi 123-456-7890 atau 987-654-3210 untuk informasi."

# 2. Cari kecocokan pertama (search)
hasil_search = pola_telepon.search(teks)

# 3. Gunakan hasil search
if hasil_search:
    # Metode group() mengembalikan teks yang cocok
    nomor_ditemukan = hasil_search.group()
    print(f"Nomor telepon pertama ditemukan: {nomor_ditemukan}")
else:
    print("Tidak ditemukan nomor telepon dengan format tersebut.")

# 2. Cari semua kecocokan (findall)
hasil_findall = pola_telepon.findall(teks)

# 3. Gunakan hasil findall (berupa list of strings)
print(f"Semua nomor telepon yang ditemukan: {hasil_findall}")
