# Perlu install: pip install -U selenium
# Perlu install: pip install pyinputplus (jika tidak pakai argumen cmd)

from selenium import webdriver
# from selenium.webdriver.chrome.service import Service # Tidak wajib diimpor jika tidak dipakai
from selenium.common.exceptions import WebDriverException
import sys
import urllib.parse
import time

# Pastikan PyInputPlus terinstal jika perlu
try:
    import pyinputplus as pyip
except ImportError:
    print("Warning: Module 'pyinputplus' tidak ditemukan. Script hanya akan berfungsi dengan argumen command line.")
    pass # Lanjut saja

# Contoh sederhana: Buka Google Maps untuk alamat tertentu

# Coba dapatkan alamat dari argumen command line
alamat = None
if len(sys.argv) > 1:
    alamat = ' '.join(sys.argv[1:])
    print(f"Alamat dari argumen: {alamat}")
else:
    try:
        alamat = pyip.inputStr("Masukkan alamat atau nama tempat: ")
    except NameError:
        print("Error: pyinputplus tidak terimpor/terinstal, dan tidak ada argumen command line.")
        sys.exit()
    except pyip.RetryLimitException:
        print("Batas percobaan input terlampaui.")
        sys.exit()
    except Exception as e:
        print(f"Terjadi error saat meminta input: {e}")
        sys.exit()

driver = None # Inisialisasi driver di luar try
if alamat:
    # Encode alamat untuk URL
    alamat_encoded = urllib.parse.quote_plus(alamat)
    url_maps = 'https://www.google.com/maps/search/' + alamat_encoded

    print(f"Membuka Google Maps untuk: {alamat}...")
    print(f"URL yang akan dibuka: {url_maps}")
    try:
        # Inisialisasi WebDriver Chrome TANPA path eksplisit
        print("Memulai instance Chrome (menggunakan Selenium Manager jika perlu)...")
        options = webdriver.ChromeOptions()
        # Tambahkan opsi jika perlu
        # options.add_argument('--headless')

        # Selenium Manager (>=4.6.0) akan menangani driver secara otomatis
        driver = webdriver.Chrome(options=options)

        # Buka URL
        driver.get(url_maps)

        print("Browser Chrome seharusnya sudah terbuka.")
        print("Skrip akan menunggu 10 detik sebelum menutup browser...")
        time.sleep(10) # Beri waktu untuk melihat hasilnya

    except WebDriverException as e:
        print(f"\nError WebDriver Selenium:")
        print(e)
        print("\nPastikan:")
        print("1. Google Chrome terinstal dengan benar.")
        print("2. Versi Selenium Anda >= 4.6.0.")
        print("3. Koneksi internet tersedia untuk mengunduh driver jika diperlukan.")
    except Exception as e:
        print(f"Terjadi error lain saat menggunakan Selenium: {e}")
    finally:
        # Selalu tutup browser setelah selesai
        if driver:
            print("Menutup browser...")
            driver.quit()
else:
    print("Tidak ada alamat yang diberikan.")

print("Skrip selesai.")