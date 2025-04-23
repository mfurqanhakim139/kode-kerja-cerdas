# Kode Contoh: Kerja Cerdas dengan Python

Repositori ini berisi kode-kode contoh yang menyertai buku (atau kerangka buku) **"Kerja Cerdas dengan Python: Stop Buang Waktu untuk Tugas Berulang!"** oleh Muhammad Furqan Hakim.

Tujuan utama buku dan kode ini adalah untuk menunjukkan bagaimana Python dapat digunakan untuk mengotomatisasi berbagai tugas komputer yang repetitif dan membosankan, menyasar pengguna seperti pekerja kantoran, staf administrasi, mahasiswa, dan siapa saja yang ingin lebih efisien dalam menggunakan komputer.

## Struktur Repositori

Kode diatur ke dalam folder berdasarkan bab buku:

* `Bab_XX/`: Berisi file-file Python (`.py`) dengan contoh kode spesifik untuk Bab XX. Nama file biasanya mengikuti format `YY_nama_deskriptif.py`.
* `nama_proyek/`: Contoh struktur proyek yang lebih besar (dari Bab 27).
* `requirements.txt`: Daftar semua library Python pihak ketiga yang diperlukan untuk menjalankan semua contoh kode.
* `README.md`: File yang sedang Anda baca ini.

## Cara Menggunakan Kode

1.  **Prasyarat:**
    * Pastikan Anda telah menginstal **Python 3** (versi 3.6 atau lebih baru direkomendasikan).
    * Memiliki `pip` (manajer paket Python) terinstal (biasanya sudah ada dengan Python modern).
    * Memiliki **Git** terinstal jika Anda mengkloning repositori ini.

2.  **Kloning Repositori (Opsional):**
    ```bash
    git clone [https://github.com/mfurqanhakim139/kode-kerja-cerdas.git](https://github.com/mfurqanhakim139/kode-kerja-cerdas.git)
    cd kode-kerja-cerdas
    ```

3.  **Buat Lingkungan Virtual (Sangat Direkomendasikan):**
    Untuk menjaga dependensi proyek tetap terisolasi:
    ```bash
    python -m venv venv
    # Aktifkan venv:
    # Windows: venv\Scripts\activate
    # macOS/Linux: source venv/bin/activate
    ```

4.  **Instal Dependensi:**
    Instal semua library yang diperlukan menggunakan file `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```
    *Catatan: Beberapa contoh (misalnya Selenium, Nmap) mungkin memerlukan setup tambahan seperti mengunduh WebDriver atau menginstal Nmap di sistem operasi Anda.*

5.  **Jalankan Contoh Kode:**
    Navigasi ke folder bab yang relevan dan jalankan file Python yang diinginkan:
    ```bash
    cd Bab_07
    python 01_alur_kerja_dasar.py
    ```
    Atau jalankan dari direktori utama:
    ```bash
    python Bab_07/01_alur_kerja_dasar.py
    ```

## Catatan Penting

* Beberapa skrip, terutama yang berinteraksi dengan API eksternal (Google Sheets, Email, Twilio, AWS), memerlukan **kunci API atau file kredensial** yang harus Anda dapatkan sendiri dan konfigurasikan sesuai petunjuk di dalam kode atau dokumentasi layanan terkait. **Jangan pernah membagikan kredensial rahasia Anda.**
* Skrip otomatisasi GUI (Bab 20, menggunakan `pyautogui`) dapat mengontrol mouse dan keyboard Anda. **Jalankan dengan hati-hati** dan pastikan Anda memahami cara menghentikannya (gunakan Failsafe).
* Kode contoh ini dirancang untuk tujuan pembelajaran. Mungkin perlu penyesuaian untuk kasus penggunaan spesifik Anda.

## Lisensi

(Disarankan untuk menambahkan file lisensi, misalnya MIT License. Jika Anda menambahkannya, sebutkan di sini.)
Contoh: Proyek ini dilisensikan di bawah Lisensi MIT - lihat file `LICENSE` untuk detailnya.

## Kontak

Jika Anda memiliki pertanyaan atau masukan, Anda bisa membuat *Issue* di repositori GitHub ini.
