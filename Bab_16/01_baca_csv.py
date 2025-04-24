import csv
from pathlib import Path

# Persiapan: Buat file CSV contoh jika belum ada
nama_file_csv = 'data_produk.csv'
file_csv = Path(nama_file_csv)
if not file_csv.exists():
    try:
        header = ['ID Produk', 'Nama Produk', 'Harga']
        data = [
            ['P001', 'Laptop ABC', '12000000'],
            ['P002', 'Keyboard, Mekanik', '850000'], # Contoh data dengan koma
            ['P003', 'Mouse Gaming', '450000']
        ]
        with open(file_csv, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(header) # Tulis header
            writer.writerows(data)  # Tulis beberapa baris data
        print(f"File '{nama_file_csv}' berhasil dibuat untuk demo.")
    except Exception as e:
        print(f"Gagal membuat file CSV demo: {e}")


# --- Membaca dengan csv.reader ---
print("\n--- Membaca dengan csv.reader ---")
try:
    with open(file_csv, mode='r', newline='', encoding='utf-8') as f_csv:
        reader = csv.reader(f_csv)
        header = next(reader) # Baca baris pertama sebagai header
        print(f"Header: {header}")
        print("Data:")
        for row_list in reader:
            # row_list adalah list of strings
            id_produk = row_list[0]
            nama = row_list[1]
            harga = row_list[2] # Masih string
            print(f" - ID: {id_produk}, Nama: {nama}, Harga: {harga}")
except FileNotFoundError:
    print(f"Error: File '{nama_file_csv}' tidak ditemukan.")
except Exception as e:
    print(f"Error saat membaca CSV: {e}")

# --- Membaca dengan csv.DictReader ---
print("\n--- Membaca dengan csv.DictReader ---")
try:
    with open(file_csv, mode='r', newline='', encoding='utf-8') as f_csv:
        dict_reader = csv.DictReader(f_csv)
        print("Data (sebagai Dictionary):")
        for row_dict in dict_reader:
            # row_dict adalah dictionary
            print(f" - ID: {row_dict['ID Produk']}, Nama: {row_dict['Nama Produk']}, Harga: {row_dict['Harga']}")
except FileNotFoundError:
    print(f"Error: File '{nama_file_csv}' tidak ditemukan.")
except Exception as e:
    print(f"Error saat membaca CSV dengan DictReader: {e}")
