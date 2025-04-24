import sys

while True:
    respons = input("Ketik 'keluar' untuk berhenti: ")
    if respons == 'keluar':
        print("Anda mengetik keluar.")
        sys.exit() # Keluar dari program
    print("Anda mengetik:", respons)
