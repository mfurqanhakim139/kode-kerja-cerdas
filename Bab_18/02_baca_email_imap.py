# Menggunakan imapclient dan pyzmail untuk membaca email
# Perlu install: pip install imapclient pyzmail
# (Nama pyzmail bisa bervariasi, coba 'pyzmail' atau 'pyzmail36')

import imapclient
import pyzmail # Atau import pyzmail36
import datetime
import pprint # Untuk cetak dictionary/list dengan rapi
import sys

# --- Konfigurasi (GANTI DENGAN DATA ANDA & SIMPAN SECARA AMAN!) ---
# --- !!! GANTI DENGAN KREDENSIAL ASLI ANDA (JANGAN SIMPAN DI KODE!) !!! ---
EMAIL_SAYA = '#' # Ganti dengan email Anda
PASSWORD_SAYA = '#' # Ganti dengan password asli atau metode aman
# --------------------------------------------------------------------------
IMAP_HOST = '#' # Ganti dengan server IMAP Anda
# Port IMAP umum: 993 (SSL), 143 (non-SSL/STARTTLS)
IMAP_PORT = 993 # Port SSL
GUNAKAN_SSL = True # Set True jika port 993, False jika 143 (mungkin perlu STARTTLS nanti)
# --------------------------------------------------------------------------

imap_obj = None # Inisialisasi di luar try
print(f"Mencoba menghubungkan ke server IMAP: {IMAP_HOST} port {IMAP_PORT} (SSL={GUNAKAN_SSL})...")
try:
    # 1. Hubungkan ke Server IMAP
    # Gunakan ssl=True untuk port SSL seperti 993
    imap_obj = imapclient.IMAPClient(IMAP_HOST, port=IMAP_PORT, ssl=GUNAKAN_SSL)
    print("Berhasil membuat koneksi awal.")

    # 2. Login
    print("Mencoba login...")
    imap_obj.login(EMAIL_SAYA, PASSWORD_SAYA)
    print("Login berhasil.")

    # 3. Pilih Folder Mailbox (misal INBOX)
    print("\nMelihat daftar folder...")
    folders = imap_obj.list_folders()
    pprint.pprint(folders)

    folder_target = 'INBOX'
    print(f"\nMemilih folder '{folder_target}' (readonly)...")
    # readonly=True agar status email (misal 'seen') tidak berubah saat dibaca
    imap_obj.select_folder(folder_target, readonly=True)
    print(f"Folder '{folder_target}' berhasil dipilih.")

    # 4. Cari Email
    # Kriteria pencarian bisa beragam, lihat dokumentasi imapclient
    # Contoh: Cari semua email yang belum dibaca (UNSEEN)
    kriteria_cari = ['UNSEEN']
    # Contoh lain: Cari email dari pengirim tertentu sejak tanggal tertentu
    # kriteria_cari = ['FROM', 'pengirim@contoh.com', 'SINCE', datetime.date(2024, 4, 1)]
    print(f"\nMencari email dengan kriteria: {kriteria_cari}...")
    email_uids = imap_obj.search(kriteria_cari) # Mengembalikan list UID (Unique ID)
    print(f"Ditemukan {len(email_uids)} email yang cocok.")

    if email_uids:
        # Ambil detail untuk email terakhir yang ditemukan (UID terbesar)
        uid_terbaru = email_uids[-1]
        print(f"\nMengambil detail email dengan UID: {uid_terbaru}...")

        # 5. Ambil (Fetch) Data Email Mentah
        # 'BODY[]' mengambil seluruh konten email (header dan body)
        # Anda bisa meminta bagian spesifik lain jika perlu
        raw_messages = imap_obj.fetch([uid_terbaru], ['BODY[]'])
        print("Berhasil mengambil data mentah (fetch).")

        # 6. Parsing Email dengan PyzMessage
        if uid_terbaru in raw_messages:
            pesan_mentah_bytes = raw_messages[uid_terbaru][b'BODY[]']
            # Gunakan factory untuk membuat objek PyzMessage
            message = pyzmail.PyzMessage.factory(pesan_mentah_bytes)
            print("\n--- Detail Email ---")
            print(f"Subjek: {message.get_subject()}")

            # Dapatkan alamat pengirim (list of tuples: [(nama, email)])
            sender = message.get_addresses('from')
            if sender:
                print(f"Dari: {sender[0][0]} <{sender[0][1]}>") # Ambil nama dan email

            # Dapatkan alamat penerima (To, Cc, Bcc)
            penerima_to = message.get_addresses('to')
            penerima_cc = message.get_addresses('cc')
            print(f"Kepada (To): {penerima_to}")
            if penerima_cc:
                print(f"Cc: {penerima_cc}")

            # Cek dan cetak body teks atau HTML
            if message.text_part:
                # Decode body teks menggunakan charset yang terdeteksi
                charset = message.text_part.charset if message.text_part.charset else 'utf-8' # Fallback ke utf-8
                try:
                    body_teks = message.text_part.get_payload().decode(charset)
                    print("\n--- Body Teks ---")
                    print(body_teks[:500] + "..." if len(body_teks) > 500 else body_teks) # Cetak preview
                except (UnicodeDecodeError, AttributeError) as decode_err:
                     print(f"\nError decoding text part with charset {charset}: {decode_err}")
                     # Coba fallback atau tampilkan raw bytes jika perlu
                     # print(message.text_part.get_payload())

            elif message.html_part:
                # Decode body HTML
                charset = message.html_part.charset if message.html_part.charset else 'utf-8'
                try:
                    body_html = message.html_part.get_payload().decode(charset)
                    print("\n--- Body HTML (awal) ---")
                    # Body HTML bisa diproses lebih lanjut (misal pakai BeautifulSoup)
                    print(body_html[:500] + "...") # Cetak preview
                except (UnicodeDecodeError, AttributeError) as decode_err:
                    print(f"\nError decoding html part with charset {charset}: {decode_err}")
                    # print(message.html_part.get_payload())
            else:
                print("\nTidak ditemukan body teks atau HTML yang bisa diparsing.")
        else:
            print("Gagal mengambil pesan mentah untuk UID yang diminta.")

    # Contoh Aksi Lain (jika readonly=False saat select_folder):
    # Menandai email sebagai sudah dibaca:
    # if email_uids:
    #     imap_obj.add_flags(email_uids, [imapclient.SEEN])
    #     print(f"\nEmail dengan UID {email_uids} ditandai sebagai SEEN.")

    # Menghapus email:
    # if email_uids:
    #     imap_obj.delete_messages(email_uids)
    #     print(f"\nEmail dengan UID {email_uids} ditandai untuk dihapus.")
    #     # Perlu expunge untuk menghapus permanen
    #     hasil_expunge = imap_obj.expunge()
    #     print(f"Hasil expunge: {hasil_expunge}")

except ImportError:
    print("Error: Library 'imapclient' atau 'pyzmail' belum terinstal.")
    print("Silakan instal dengan: pip install imapclient pyzmail")
except imapclient.exceptions.LoginError:
    print("Gagal login. Periksa email/password dan pastikan akses IMAP diaktifkan di akun Anda.")
    print("Untuk Gmail, mungkin perlu App Password jika 2FA aktif.")
except imapclient.exceptions.IMAPClientError as imap_err:
    print(f"Terjadi error IMAP: {imap_err}")
except Exception as e:
    print(f"Gagal membaca email. Terjadi error lain: {e}")
    print(f"Tipe error: {type(e)}")
finally:
    # 7. Putuskan Koneksi (Logout)
    if imap_obj:
        try:
            print("\nLogout dari server IMAP...")
            imap_obj.logout()
            print("Logout berhasil.")
        except Exception:
            pass # Abaikan jika sudah error sebelumnya

print("\nSkrip IMAP selesai.")