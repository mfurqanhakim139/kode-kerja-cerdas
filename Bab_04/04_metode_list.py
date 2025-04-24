# Contoh penggunaan metode-metode bawaan List

kendaraan = ["motor", "mobil"]
print(f"List awal: {kendaraan}")

# 1. append(): Menambah item ke akhir
kendaraan.append("sepeda")
kendaraan.append("bajaj")
print(f"Setelah append 'sepeda' & 'bajaj': {kendaraan}") 

# 2. insert(): Menyisipkan item pada indeks tertentu
kendaraan.insert(1, "becak") # Sisipkan 'becak' di indeks 1
print(f"Setelah insert 'becak' di indeks 1: {kendaraan}") 

# 3. remove(): Menghapus item berdasarkan nilainya (pertama ditemukan)
try:
    kendaraan.remove("mobil")
    print(f"Setelah remove 'mobil': {kendaraan}") 
    # kendaraan.remove("truk") # Ini akan error karena 'truk' tidak ada
except ValueError as e:
    print(f"Error saat remove: {e}")

print("-" * 20)

# 4. sort(): Mengurutkan list (in-place)
angka_acak = [5, 1, 4, 2, 3, 8, 6]
print(f"Angka acak sebelum sort: {angka_acak}")
angka_acak.sort() # Urutkan dari kecil ke besar
print(f"Setelah sort(): {angka_acak}") 
angka_acak.sort(reverse=True) # Urutkan dari besar ke kecil
print(f"Setelah sort(reverse=True): {angka_acak}")

nama_kota = ["Jakarta", "bandung", "Surabaya", "Medan", "bali"]
print(f"Kota sebelum sort: {nama_kota}")
nama_kota.sort() # Sort berdasarkan alfabet (case-sensitive, huruf besar dulu)
print(f"Setelah sort() default: {nama_kota}") 
nama_kota.sort(key=str.lower) # Sort case-insensitive
print(f"Setelah sort(key=str.lower): {nama_kota}") 

print("-" * 20)

# 5. reverse(): Membalik urutan list (in-place)
angka_urut = [10, 20, 30, 40, 50]
print(f"Angka urut sebelum reverse: {angka_urut}")
angka_urut.reverse()
print(f"Setelah reverse(): {angka_urut}") 

print("-" * 20)

# 6. index(): Mencari indeks item berdasarkan nilai (pertama ditemukan)
cari_indeks = ['a', 'b', 'c', 'd', 'b', 'e']
try:
    indeks_b_pertama = cari_indeks.index('b')
    print(f"Indeks pertama 'b' dalam {cari_indeks}: {indeks_b_pertama}") # -> 1
    # Mencari mulai dari indeks tertentu
    # indeks_b_kedua = cari_indeks.index('b', indeks_b_pertama + 1) 
    # print(f"Indeks 'b' setelah indeks {indeks_b_pertama}: {indeks_b_kedua}") # -> 4

    # Mencari item yang tidak ada akan error
    # indeks_z = cari_indeks.index('z') 
except ValueError as e:
    print(f"Error saat mencari indeks: {e}") # Muncul jika 'z' dicari

# Cek dulu sebelum pakai index jika tidak yakin item ada
if 'd' in cari_indeks:
    print(f"Indeks 'd' adalah: {cari_indeks.index('d')}")
