import requests
import sys # Digunakan untuk keluar jika error saat import

# Pastikan library requests sudah terinstal
# Jika belum, jalankan: pip install requests

url_target = 'https://github.com/mfurqanhakim139/kode-kerja-cerdas/blob/main/rj.txt' # Contoh URL (teks Romeo & Juliet)
nama_file_output = 'romeo_juliet.txt'

# Header User-Agent umum untuk browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

print(f"Mencoba mengunduh: {url_target}...")
try:
    # Tambahkan headers ke permintaan get
    response = requests.get(url_target, headers=headers, timeout=15) # Timeout sedikit diperpanjang
    
    # Cek jika ada error HTTP (misal 404 Not Found, 500 Server Error)
    # Jika ada error, ini akan membangkitkan exception HTTPError
    response.raise_for_status()

    print("Unduhan berhasil!")

    # Konten ada di response.text (untuk teks)
    # atau response.content (untuk data biner/bytes)
    konten_teks = response.text
    print(f"Panjang konten: {len(konten_teks):,} karakter") # Tambahkan pemisah ribuan

    # Menampilkan beberapa karakter pertama sebagai preview
    print("\n--- Preview Konten (500 karakter pertama) ---")
    print(konten_teks[:500])
    print("...\n" + "-"*45)

    # Menyimpan konten teks ke file
    try:
        print(f"\nMenyimpan konten ke file: '{nama_file_output}'...")
        with open(nama_file_output, 'w', encoding='utf-8') as f:
            f.write(konten_teks)
        print("Konten berhasil disimpan.")
    except IOError as e:
        print(f"Error saat menyimpan file: {e}")
    except Exception as e:
        print(f"Terjadi error tak terduga saat menyimpan file: {e}")

except requests.exceptions.Timeout:
    print(f"Gagal mengunduh: Waktu permintaan habis (timeout).")
except requests.exceptions.HTTPError as http_err:
    print(f"Gagal mengunduh: Terjadi error HTTP - {http_err}")
except requests.exceptions.ConnectionError as conn_err:
    print(f"Gagal mengunduh: Terjadi error koneksi - {conn_err}")
except requests.exceptions.RequestException as req_err:
    # Menangkap error lain dari library requests
    print(f"Gagal mengunduh halaman: Error requests - {req_err}")
except Exception as e:
    # Menangkap error umum lainnya
    print(f"Terjadi error lain yang tidak terduga: {e}")

print("\nSkrip selesai.")