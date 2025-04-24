angka = 0
while angka < 10:
    angka += 1
    if angka % 2 == 0: # Jika angka genap
        continue       # Lewati sisa kode di iterasi ini, lanjut ke iterasi berikutnya
    print("Angka ganjil:", angka) # Hanya akan print angka ganjil
