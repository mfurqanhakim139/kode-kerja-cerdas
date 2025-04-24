# Contoh memodifikasi list (mutable)

warna = ["merah", "kuning", "hijau"]
print(f"List warna awal: {warna}")

# 1. Mengubah item berdasarkan indeks
warna[1] = "BIRU" # Ganti item di indeks 1
print(f"Setelah ubah indeks 1: {warna}") # -> ['merah', 'BIRU', 'hijau']

print("-" * 20)

# 2. Menggabungkan list (+)
list1 = [1, 2]
list2 = [3, 4]
list_gabungan = list1 + list2
print(f"List 1: {list1}")
print(f"List 2: {list2}")
print(f"Hasil gabungan (+): {list_gabungan}") # -> [1, 2, 3, 4]
# Perhatikan list1 dan list2 tidak berubah
print(f"List 1 setelah gabung: {list1}") 

print("-" * 20)

# 3. Mereplikasi list (*)
list_a = ["A", "B"]
list_ulang = list_a * 3 # Ulangi item list_a 3 kali
print(f"List A: {list_a}")
print(f"Hasil replikasi (* 3): {list_ulang}") # -> ['A', 'B', 'A', 'B', 'A', 'B']

print("-" * 20)

# 4. Menghapus item (del)
angka_hapus = [10, 20, 30, 40, 50]
print(f"List angka sebelum dihapus: {angka_hapus}")
del angka_hapus[2] # Hapus item di indeks 2 (yaitu angka 30)
print(f"Setelah hapus indeks 2: {angka_hapus}") # -> [10, 20, 40, 50]

# Hapus slice (misal hapus 2 item terakhir)
# del angka_hapus[-2:] 
# print(f"Setelah hapus 2 item terakhir: {angka_hapus}")
