# Pastikan sudah install/update: pip install -U selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
import sys # Untuk keluar jika perlu

# --- Pilihan Browser (Pilih salah satu) ---
# Opsi 1: Gunakan Firefox
# USE_FIREFOX = True
# Opsi 2: Gunakan Chrome (jika USE_FIREFOX = False)
USE_FIREFOX = False
# -----------------------------------------

driver = None # Inisialisasi driver di luar try
try:
    # Inisialisasi WebDriver
    # Selenium Manager (>=4.6.0) akan mencoba mengunduh driver
    # yang sesuai jika tidak ditemukan.
    if USE_FIREFOX:
        print("Memulai instance Firefox...")
        options = webdriver.FirefoxOptions()
        # Tambahkan argumen jika perlu, misal:
        # options.add_argument("--headless") # Jalankan tanpa membuka jendela GUI
        driver = webdriver.Firefox(options=options)
    else:
        print("Memulai instance Chrome...")
        options = webdriver.ChromeOptions()
        # Tambahkan argumen jika perlu, misal:
        # options.add_argument("--headless")
        # options.add_argument("--disable-gpu") # Terkadang dibutuhkan di Windows
        driver = webdriver.Chrome(options=options)

    print("WebDriver berhasil dimulai.")

    # Buka halaman Google
    print("Membuka https://google.com ...")
    driver.get("https://google.com")
    print(f"Judul halaman: {driver.title}")

    # Cari elemen search box (berdasarkan atribut 'name')
    # Tunggu hingga search box muncul dan bisa diklik (best practice)
    print("Mencari search box...")
    wait = WebDriverWait(driver, 10) # Tunggu maksimal 10 detik
    search_box = wait.until(EC.element_to_be_clickable((By.NAME, "q")))
    print("Search box ditemukan.")

    # Ketik query dan tekan Enter
    query = "Python Web Scraping Selenium"
    print(f"Mengetik '{query}' dan menekan Enter...")
    search_box.send_keys(query + Keys.RETURN)

    # Tunggu hingga elemen hasil pencarian muncul (lebih baik dari time.sleep)
    # Kita tunggu elemen div dengan id 'search', yang biasanya ada di halaman hasil
    print("Menunggu hasil pencarian muncul...")
    wait.until(EC.presence_of_element_located((By.ID, "search")))
    print("Hasil pencarian muncul.")
    print("Skrip Selenium berhasil dijalankan.")

except TimeoutException:
    print("Error: Waktu tunggu habis saat mencari elemen (halaman lambat atau elemen tidak ada).")
except WebDriverException as e:
    print(f"\nError WebDriver Selenium:")
    # Pesan error WebDriverException seringkali informatif
    if "net::ERR_NAME_NOT_RESOLVED" in str(e) or "net::ERR_CONNECTION_REFUSED" in str(e):
         print("-> Mungkin tidak ada koneksi internet atau DNS bermasalah.")
    elif "unable to find driver" in str(e).lower() or "not found in PATH" in str(e):
         print("-> WebDriver tidak ditemukan. Pastikan Selenium >= 4.6.0 atau WebDriver ada di PATH.")
    elif "session not created" in str(e).lower() and "version is" in str(e).lower():
         print("-> Versi WebDriver mungkin tidak cocok dengan versi Browser Anda.")
    else:
        print(f"-> Detail: {e}")
    print("\nPastikan browser (Chrome/Firefox) terinstal dan Selenium terupdate.")
except Exception as e:
    print(f"Terjadi error lain yang tidak terduga: {e}")

finally:
    # Selalu tutup browser setelah selesai, bahkan jika error
    if driver:
        print("Menutup browser...")
        driver.quit()

print("Skrip selesai.")