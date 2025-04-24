# Contoh bekerja dengan list: perulangan for dan operator in/not in

nama_hewan = ["kucing", "anjing", "kelinci", "hamster"]
print(f"List hewan: {nama_hewan}")

# 1. Menggunakan perulangan for untuk iterasi
print("\nDaftar hewan (for loop):")
for hewan in nama_hewan:
    print(f"- {hewan.capitalize()}") # capitalize() membuat huruf awal besar

print("-" * 20)

# 2. Memeriksa keberadaan item dengan 'in'
hewan_dicari = "kelinci"
if hewan_dicari in nama_hewan:
    print(f"'{hewan_dicari}' ditemukan dalam list.")
else:
    print(f"'{hewan_dicari}' tidak ditemukan.")

hewan_lain = "burung"
print(f"Apakah '{hewan_lain}' ada di list? {'burung' in nama_hewan}") # -> False

print("-" * 20)

# 3. Memeriksa ketidakberadaan item dengan 'not in'
if "ular" not in nama_hewan:
    print("'ular' memang tidak ada di dalam list.")

print(f"Apakah 'anjing' tidak ada di list? {'anjing' not in nama_hewan}") # -> False
