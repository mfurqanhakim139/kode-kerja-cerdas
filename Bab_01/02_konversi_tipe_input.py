# Konversi input umur ke integer
input_umur = input("Masukkan umur Anda: ")
# Masukkan umur Anda: 25 (pengguna mengetik 25)
print(f"Tipe input_umur: {type(input_umur)}") # -> <class 'str'>

umur_angka = int(input_umur)
print(f"Tipe umur_angka: {type(umur_angka)}") # -> <class 'int'>
print("Tahun depan umur Anda:", umur_angka + 1) # -> Tahun depan umur Anda: 26

# Konversi string desimal ke float
nilai_string = "99.5"
nilai_float = float(nilai_string)
print(nilai_float) # -> 99.5

# Konversi angka ke string
angka = 100
teks_angka = str(angka)
# String hanya bisa digabung (+) dengan string lain
