import csv
from pathlib import Path

nama_file_output = 'output_produk.csv'
nama_file_dict_output = 'output_produk_dict.csv'

# Data untuk ditulis (list of lists)
data_list = [
    ['SKU', 'Item', 'Stok'],
    ['L001', 'Laptop', 15],
    ['K005', 'Keyboard', 35],
    ['M012', 'Mouse', 50]
]

# Data untuk ditulis (list of dictionaries)
data_dict = [
    {'ID': 'A01', 'Nama': 'Buku Tulis', 'Kategori': 'ATK', 'Harga': 5000},
    {'ID': 'B02', 'Nama': 'Pensil 2B', 'Kategori': 'ATK', 'Harga': 2000},
    {'ID': 'C03', 'Nama': 'Stapler', 'Kategori': 'ATK', 'Harga': 15000}
]
header_dict = ['ID', 'Nama', 'Kategori', 'Harga'] # Urutan header penting untuk DictWriter

# --- Menulis dengan csv.writer ---
print(f"--- Menulis ke '{nama_file_output}' dengan csv.writer ---")
try:
    with open(nama_file_output, 'w', newline='', encoding='utf-8') as f_out:
        writer = csv.writer(f_out)
        writer.writerows(data_list) # Tulis semua baris dari list of lists
    print("Berhasil menulis data list.")
except Exception as e:
    print(f"Gagal menulis data list: {e}")

# --- Menulis dengan csv.DictWriter ---
print(f"\n--- Menulis ke '{nama_file_dict_output}' dengan csv.DictWriter ---")
try:
    with open(nama_file_dict_output, 'w', newline='', encoding='utf-8') as f_out_dict:
        # fieldnames menentukan urutan kolom
        writer = csv.DictWriter(f_out_dict, fieldnames=header_dict)
        writer.writeheader() # Tulis baris header
        writer.writerows(data_dict) # Tulis semua baris dari list of dicts
    print("Berhasil menulis data dictionary.")
except Exception as e:
    print(f"Gagal menulis data dictionary: {e}")

