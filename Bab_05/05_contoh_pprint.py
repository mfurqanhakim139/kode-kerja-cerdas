# Contoh menggunakan pprint untuk mencetak struktur data kompleks
import pprint 

data_kompleks = {
    'proyek': 'Sistem Inventaris Toko Buku', 'versi': 1.2, 'aktif': True,
    'modul': [
        {'nama': 'Manajemen Buku', 'file': ['buku.py', 'kategori.py', 'penerbit.py'], 'status': 'stabil', 'prioritas': 1},
        {'nama': 'Transaksi', 'file': ['penjualan.py', 'pembelian.py', 'stok.py', 'laporan_tx.py'], 'status': 'pengembangan', 'prioritas': 1},
        {'nama': 'Manajemen Anggota', 'file': ['anggota.py', 'poin.py'], 'status': 'beta', 'prioritas': 2}
    ],
    'tim_pengembang': {
        'backend': {'nama': 'Dewi Lestari', 'email': 'dewi.l@example.com'},
        'frontend': {'nama': 'Bambang Susilo', 'email': 'bambang.s@example.com'},
        'database': {'nama': 'Agus Salim', 'email': 'agus.s@example.com'}
    },
    'server_config': ('192.168.1.105', 8080, {'timeout': 30, 'max_connections': 100})
}

print("--- Output menggunakan print() bawaan ---")
print(data_kompleks)

print("\n" + "="*50 + "\n") # Pemisah

print("--- Output menggunakan pprint.pprint() ---")
# pprint otomatis mengurutkan kunci dict dan memberi indentasi
pprint.pprint(data_kompleks, indent=2, width=100) # Atur indent dan lebar output

print("\n" + "="*50 + "\n") 

print("--- Output menggunakan pprint.pformat() (mendapatkan string) ---")
# pformat mengembalikan string yang sudah diformat
string_terformat = pprint.pformat(data_kompleks, indent=2, width=100)
print(string_terformat)
# Anda bisa menyimpan string_terformat ini ke file log, dll.
