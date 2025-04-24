# Asumsikan class Karyawan dari atas sudah didefinisikan
#Contoh Definisi Class Sederhana:
class Karyawan:
    # Konstruktor: dijalankan saat objek Karyawan dibuat
    def __init__(self, input_nama, input_gaji):
        print(f"Membuat objek Karyawan baru untuk {input_nama}...")
        # Membuat atribut instance menggunakan self
        self.nama = input_nama
        self.gaji = input_gaji
        self.email = input_nama.lower() + '@perusahaan.com' # Contoh atribut lain

    # Ini contoh metode instance
    def tampilkan_info(self):
        print(f"--- Info Karyawan ---")
        print(f"Nama: {self.nama}")
        print(f"Gaji: Rp {self.gaji:,.0f}")
        print(f"Email: {self.email}")

    # Contoh metode lain
    def dapatkan_gaji_tahunan(self):
        return self.gaji * 12

# Membuat objek/instance dari class Karyawan
karyawan1 = Karyawan("Budi", 5000000) # '__init__' akan dipanggil dengan self=karyawan1, input_nama="Budi", input_gaji=5000000
karyawan2 = Karyawan("Citra", 6500000) # '__init__' dipanggil lagi untuk objek baru

print("\nObjek berhasil dibuat.")

# karyawan1 dan karyawan2 adalah objek yang berbeda,
# meskipun berasal dari class yang sama.
print(f"Tipe karyawan1: {type(karyawan1)}")
# --- Akses Atribut ---
print(f"\nMengakses atribut karyawan1:")
print(f"Nama Karyawan 1: {karyawan1.nama}")
print(f"Gaji Karyawan 1: {karyawan1.gaji}")
print(f"Email Karyawan 1: {karyawan1.email}")

print(f"\nMengakses atribut karyawan2:")
print(f"Nama Karyawan 2: {karyawan2.nama}")

# Atribut bisa diubah (jika tidak ada proteksi khusus)
# karyawan1.gaji = 5500000
# print(f"Gaji Karyawan 1 setelah diubah: {karyawan1.gaji}")


# --- Memanggil Metode ---
print("\nMemanggil metode tampilkan_info():")
karyawan1.tampilkan_info() # 'self' otomatis merujuk ke karyawan1
print("-" * 20)
karyawan2.tampilkan_info() # 'self' otomatis merujuk ke karyawan2

print("\nMemanggil metode dapatkan_gaji_tahunan():")
gaji_tahunan_k1 = karyawan1.dapatkan_gaji_tahunan()
print(f"Gaji tahunan {karyawan1.nama}: Rp {gaji_tahunan_k1:,.0f}")

gaji_tahunan_k2 = karyawan2.dapatkan_gaji_tahunan()
print(f"Gaji tahunan {karyawan2.nama}: Rp {gaji_tahunan_k2:,.0f}")

