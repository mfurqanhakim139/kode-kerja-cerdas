import json
from pathlib import Path

# Contoh data Python (dictionary)
data_py = {
    "nama": "Proyek Alfa",
    "versi": 1.2,
    "aktif": True,
    "anggota": ["Andi", "Budi", "Citra"],
    "konfigurasi": {
        "server": "192.168.1.100",
        "port": 8080,
        "debug_mode": False,
        "opsi_tambahan": None # None di Python jadi null di JSON
    }
}

nama_file_json = 'data_proyek.json'

# --- Menulis Python ke JSON (dump/dumps) ---
print(f"--- Menulis data Python ke file '{nama_file_json}' ---")
try:
    # Menggunakan json.dump() untuk menulis ke file
    with open(nama_file_json, 'w', encoding='utf-8') as f_json:
        json.dump(data_py, f_json, indent=4) # indent=4 untuk pretty print
    print("Berhasil menulis ke file JSON.")

    # Menggunakan json.dumps() untuk mendapatkan string JSON
    # json_string = json.dumps(data_py, indent=4)
    # print("\nString JSON yang dihasilkan:")
    # print(json_string)

except Exception as e:
    print(f"Gagal menulis JSON: {e}")


# --- Membaca JSON ke Python (load/loads) ---
print(f"\n--- Membaca data dari file '{nama_file_json}' ---")
if Path(nama_file_json).exists():
    try:
        # Menggunakan json.load() untuk membaca dari file
        with open(nama_file_json, 'r', encoding='utf-8') as f_json:
            data_dari_json = json.load(f_json)

        print("Berhasil membaca dari file JSON.")
        print("Data Python hasil pembacaan:")
        # Mengakses data seperti dictionary Python biasa
        print(f" - Nama Proyek: {data_dari_json['nama']}")
        print(f" - Anggota pertama: {data_dari_json['anggota'][0]}")
        print(f" - Port Konfigurasi: {data_dari_json['konfigurasi']['port']}")
        print(f" - Tipe data 'aktif': {type(data_dari_json['aktif'])}") # bool
        print(f" - Tipe data 'opsi_tambahan': {type(data_dari_json['konfigurasi']['opsi_tambahan'])}") # NoneType

        # Membaca dari string JSON (jika perlu)
        # string_json_contoh = '{"id": 1, "pesan": "Halo JSON!"}'
        # data_dari_string = json.loads(string_json_contoh)
        # print(f"\nData dari string: {data_dari_string}")

    except json.JSONDecodeError as e_decode:
        print(f"Gagal mem-parsing JSON: Format tidak valid - {e_decode}")
    except Exception as e:
        print(f"Gagal membaca JSON: {e}")
else:
    print(f"File '{nama_file_json}' tidak ditemukan untuk dibaca.")
