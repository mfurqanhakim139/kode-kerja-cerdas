# Contoh lingkup variabel (scope) lokal vs global

skor_global = 100 # Variabel Global

def fungsi_satu():
    skor_lokal_1 = 10 # Variabel Lokal hanya untuk fungsi_satu
    print(f"Di dalam fungsi_satu:")
    print(f"  - skor_lokal_1 = {skor_lokal_1}")
    print(f"  - membaca skor_global = {skor_global}")
    # Baris berikut akan error jika di-uncomment:
    # print(f"  - mencoba akses skor_lokal_2 = {skor_lokal_2}") 

def fungsi_dua():
    skor_lokal_2 = 20 # Variabel Lokal hanya untuk fungsi_dua
    nama_global = "Python" # Contoh shadowing (ada var global dgn nama sama)
    print(f"Di dalam fungsi_dua:")
    print(f"  - skor_lokal_2 = {skor_lokal_2}")
    print(f"  - membaca skor_global = {skor_global}")
    print(f"  - nama_global (lokal) = {nama_global}") # Mengakses var lokal

# Variabel global lain
nama_global = "Dunia"

print("Memanggil fungsi...")
fungsi_satu()
print("-" * 20)
fungsi_dua()
print("-" * 20)

print(f"Di scope global:")
print(f"  - skor_global = {skor_global}")
print(f"  - nama_global = {nama_global}") # Mengakses var global

# Baris berikut akan error jika di-uncomment:
# print(f"  - mencoba akses skor_lokal_1 = {skor_lokal_1}") 
# print(f"  - mencoba akses skor_lokal_2 = {skor_lokal_2}")
