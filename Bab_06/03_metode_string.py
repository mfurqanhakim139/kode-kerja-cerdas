# Contoh penggunaan metode-metode string umum

teks = "   Python itu Seru dan Mudah Dipelajari!   "
print(f"String Original: '{teks}'")

# 1. Kasus Huruf
print(f"Upper Case: '{teks.upper()}'")
print(f"Lower Case: '{teks.lower()}'")
print(f"Title Case: '{teks.title()}'") # Setiap kata diawali kapital
print(f"Capitalize: '{teks.strip().capitalize()}'") # Hanya huruf pertama jadi kapital

print("\n--- Pengecekan Karakter ---")
kata1 = "PYTHON"
kata2 = "python123"
kata3 = "12345"
kata4 = "   "
print(f"'{kata1}'.isupper()? {kata1.isupper()}") # True
print(f"'{kata1}'.islower()? {kata1.islower()}") # False
print(f"'Python'.isalpha()? {'Python'.isalpha()}") # True
print(f"'{kata2}'.isalnum()? {kata2.isalnum()}") # True (huruf atau angka)
print(f"'{kata2}'.isalpha()? {kata2.isalpha()}") # False (karena ada angka)
print(f"'{kata3}'.isdecimal()? {kata3.isdecimal()}") # True
print(f"'-123'.isdecimal()? {'-123'.isdecimal()}") # False (karena ada '-')
print(f"'{kata4}'.isspace()? {kata4.isspace()}") # True
print(f"'Judul Buku'.istitle()? {'Judul Buku'.istitle()}") # True

print("\n--- Pengecekan Awal/Akhir & Whitespace ---")
teks_bersih = teks.strip() # Hapus spasi awal/akhir
print(f"Strip: '{teks_bersih}'")
print(f"'{teks_bersih}'.startswith('Python')? {teks_bersih.startswith('Python')}") # True
print(f"'{teks_bersih}'.endswith('Dipahami')? {teks_bersih.endswith('Dipahami')}") # False
print(f"'{teks}'.lstrip(): '{teks.lstrip()}'") # Hapus spasi kiri
print(f"'{teks}'.rstrip(): '{teks.rstrip()}'") # Hapus spasi kanan

print("\n--- Menggabungkan (join) dan Memisah (split) ---")
list_kata = ["Belajar", "Python", "Untuk", "Otomatisasi"]
pemisah_spasi = " "
kalimat_spasi = pemisah_spasi.join(list_kata)
print(f"Join dengan spasi: '{kalimat_spasi}'") 

pemisah_strip = "-"
kalimat_strip = pemisah_strip.join(list_kata)
print(f"Join dengan '-': '{kalimat_strip}'") 

data_csv_like = "ID,Nama,Kota,Umur"
kolom = data_csv_like.split(',') # Pisah berdasarkan koma
print(f"Split '{data_csv_like}' berdasarkan ',': {kolom}")

kalimat_panjang = "Ini adalah contoh kalimat yang cukup panjang."
kata_kata = kalimat_panjang.split() # Split berdasarkan whitespace (default)
print(f"Split kalimat panjang: {kata_kata}")

print("\n--- Mencari (find) dan Mengganti (replace) ---")
kalimat_cari = "Python adalah bahasa yang populer, Python mudah."
posisi_python_1 = kalimat_cari.find('Python') # -> 0 (indeks pertama)
posisi_python_2 = kalimat_cari.find('Python', posisi_python_1 + 1) # Cari setelah yg pertama -> 33
posisi_java = kalimat_cari.find('Java') # -> -1 (tidak ditemukan)
print(f"Posisi 'Python' pertama: {posisi_python_1}")
print(f"Posisi 'Python' kedua: {posisi_python_2}")
print(f"Posisi 'Java': {posisi_java}")

kalimat_ganti = kalimat_cari.replace('Python', 'PYTHON_KEREN') # Ganti semua kemunculan
print(f"Setelah replace: '{kalimat_ganti}'")
kalimat_ganti_sekali = kalimat_cari.replace('Python', 'PYTHON_KEREN', 1) # Ganti 1x saja
print(f"Setelah replace (1x): '{kalimat_ganti_sekali}'")

print("\n--- Nilai Numerik Karakter (ord/chr) ---")
print(f"Nilai ord('A'): {ord('A')}") # -> 65
print(f"Nilai ord('a'): {ord('a')}") # -> 97
print(f"Nilai chr(66): '{chr(66)}'") # -> B
print(f"Nilai chr(90): '{chr(90)}'") # -> Z
