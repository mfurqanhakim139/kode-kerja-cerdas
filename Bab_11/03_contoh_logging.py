import logging

# Konfigurasi logging dasar (lakukan sekali di awal)
logging.basicConfig(
    level=logging.DEBUG, # Tampilkan semua pesan dari level DEBUG ke atas
    # format='%(asctime)s - %(levelname)s - %(message)s', # Format dasar
    format='%(levelname)s:%(name)s:%(asctime)s:%(message)s', # Contoh format lain
    # filename='log_program.txt', # Uncomment untuk menyimpan ke file
    # filemode='w' # 'w' untuk timpa, 'a' untuk tambah
)

# Menonaktifkan semua log (uncomment baris di bawah jika ingin mematikan log)
# logging.disable(logging.CRITICAL)

# Contoh pesan log di berbagai bagian program
logging.debug('Mulai program...')

def faktorial(n):
    logging.debug(f'Mulai faktorial({n})...')
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug(f'  i={i}, total sementara={total}')
    logging.debug(f'Akhir faktorial({n})')
    return total

logging.info('Memanggil faktorial(5)...')
hasil = faktorial(5)
logging.info(f'Faktorial(5) selesai. Hasil = {hasil}')

logging.warning('Ini pesan peringatan contoh.')
logging.error('Ini pesan error contoh.')
logging.critical('Ini pesan critical contoh.')

logging.debug('Program selesai.')
