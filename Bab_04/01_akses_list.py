# Contoh mengakses item dan slice dalam List

buah = ["apel", "mangga", "jeruk", "pisang", "anggur"]
print(f"List buah awal: {buah}")

# Mengakses item tunggal
item_pertama = buah[0]         
item_kedua = buah[1]           
item_terakhir = buah[-1]        
item_kedua_terakhir = buah[-2]  

print(f"Item pertama (indeks 0): {item_pertama}")       # -> "apel"
print(f"Item kedua (indeks 1): {item_kedua}")          # -> "mangga"
print(f"Item terakhir (indeks -1): {item_terakhir}")     # -> "anggur"
print(f"Item kedua terakhir (indeks -2): {item_kedua_terakhir}") # -> "pisang"

# Mengambil slice (irisan)
# Slice dari indeks 1 sampai sebelum indeks 4 (item ke-2, 3, 4)
sub_list1 = buah[1:4] 
print(f"\nSlice [1:4]: {sub_list1}") # -> ['mangga', 'jeruk', 'pisang']

# Slice dari awal sampai sebelum indeks 3 (item ke-1, 2, 3)
sub_list2 = buah[:3] 
print(f"Slice [:3]: {sub_list2}") # -> ['apel', 'mangga', 'jeruk']

# Slice dari indeks 2 sampai akhir (item ke-3 dst)
sub_list3 = buah[2:] 
print(f"Slice [2:]: {sub_list3}") # -> ['jeruk', 'pisang', 'anggur']

# Slice seluruh list (membuat salinan dangkal)
sub_list_semua = buah[:]
print(f"Slice [:].: {sub_list_semua}") # -> ['apel', 'mangga', 'jeruk', 'pisang', 'anggur']
