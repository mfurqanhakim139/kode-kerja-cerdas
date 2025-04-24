from pathlib import Path

# Buat file contoh dulu (jika belum ada)
path_contoh = Path('contoh_baca.txt')
if not path_contoh.exists():
    with open(path_contoh, mode='w', encoding='utf-8') as f:
        f.write("Baris pertama.\n")
        f.write("Ini baris kedua.\n")
        f.write("Baris terakhir, ketiga.\n")
    print(f"File '{path_contoh}' berhasil dibuat.")


# --- Cara Membaca ---
print("\n--- Membaca dengan read() ---")
try:
    with open(path_contoh, mode='r', encoding='utf-8') as file_obj:
        konten_semua = file_obj.read()
        print(konten_semua)
except FileNotFoundError:
    print(f"Error: File {path_contoh} tidak ditemukan.")

print("\n--- Membaca dengan readlines() ---")
try:
    with open(path_contoh, mode='r', encoding='utf-8') as file_obj:
        list_baris = file_obj.readlines()
        print(list_baris) # Output berupa list
        # Mencetak tiap baris dari list:
        # for baris in list_baris:
        #     print(baris.strip()) # strip() untuk hapus newline ekstra
except FileNotFoundError:
    print(f"Error: File {path_contoh} tidak ditemukan.")

print("\n--- Membaca dengan Iterasi Langsung ---")
try:
    with open(path_contoh, mode='r', encoding='utf-8') as file_obj:
        print("Membaca baris per baris:")
        for nomer_baris, baris in enumerate(file_obj, 1):
            print(f"Baris {nomer_baris}: {baris.strip()}") # strip() lebih rapi
except FileNotFoundError:
    print(f"Error: File {path_contoh} tidak ditemukan.")
