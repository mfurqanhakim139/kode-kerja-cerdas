# Contoh validasi manual sederhana untuk usia
while True: # Loop tak terbatas sampai input valid
    print("Masukkan usia Anda:")
    usia_str = input()
    try:
        usia = int(usia_str) # Coba konversi ke integer
        if usia < 0:
            print("Usia tidak boleh negatif. Silakan coba lagi.")
        else:
            break # Input valid (angka dan tidak negatif), keluar loop
    except ValueError:
        print("Input tidak valid. Masukkan hanya angka. Silakan coba lagi.")

print(f"Usia Anda adalah: {usia}")

