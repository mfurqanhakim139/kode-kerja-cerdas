import pyautogui
import time

# --- Pengamanan ---
pyautogui.FAILSAFE = True

print("Mengambil screenshot seluruh layar dalam 3 detik...")
time.sleep(3)

try:
    nama_file_ss = 'screenshot_penuh.png'
    screenshot_img = pyautogui.screenshot()
    screenshot_img.save(nama_file_ss)
    print(f"Screenshot disimpan sebagai '{nama_file_ss}'")

    #Contoh mengambil region (misal: pojok kiri atas 100x100)
    nama_file_region = 'screenshot_region.png'
    region_img = pyautogui.screenshot(region=(0, 0, 100, 100))
    region_img.save(nama_file_region)
    print(f"Screenshot region disimpan sebagai '{nama_file_region}'")

    #Contoh locateOnScreen (perlu file gambar 'tombol_contoh.png' dan 'pip install opencv-python')
    try:
        #Buat file dummy 'tombol_contoh.png' atau gunakan gambar asli
        lokasi_tombol = pyautogui.locateOnScreen('tombol_contoh.png', confidence=0.9)
        if lokasi_tombol:
            print(f"Gambar tombol ditemukan di: {lokasi_tombol}")
            pusat_tombol = pyautogui.center(lokasi_tombol) # atau locateCenterOnScreen
            print(f"Pusat tombol di: {pusat_tombol}")
            # pyautogui.click(pusat_tombol) # Klik tombol jika ditemukan
        else:
            print("Gambar tombol tidak ditemukan di layar.")
    except pyautogui.ImageNotFoundException:
         print("Gambar tombol tidak ditemukan di layar.")
    except ImportError:
         print("Fitur locateOnScreen memerlukan 'opencv-python'. Install dengan 'pip install opencv-python'")


except Exception as e:
    print(f"Terjadi error: {e}")
