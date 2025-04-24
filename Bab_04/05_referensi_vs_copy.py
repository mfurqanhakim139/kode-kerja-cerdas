# Memahami perbedaan referensi dan salinan (copy) pada List
import copy # Impor modul copy untuk deepcopy

print("--- Perilaku Referensi (Assignment Biasa) ---")
list_a = [1, 2, [10, 20]] # List A punya sub-list
list_b = list_a # list_b SEKARANG menunjuk ke objek list YANG SAMA dengan list_a

print(f"ID objek list_a: {id(list_a)}")
print(f"ID objek list_b: {id(list_b)}") # ID nya sama!
print(f"Sebelum ubah B: List A = {list_a}")
print(f"Sebelum ubah B: List B = {list_b}")

# Mengubah list melalui variabel B
list_b.append(4) 
list_b[2].append(30) # Mengubah sub-list di dalam B

print(f"Setelah ubah B: List A = {list_a}") # Perhatikan A ikut berubah!
print(f"Setelah ubah B: List B = {list_b}") 

print("\n--- Menggunakan copy.copy() (Salinan Dangkal / Shallow Copy) ---")
list_c = [1, 2, [10, 20]]
list_d = copy.copy(list_c) # Membuat salinan baru, tapi sub-list masih referensi

print(f"ID objek list_c: {id(list_c)}")
print(f"ID objek list_d: {id(list_d)}") # ID nya BEDA!
print(f"ID sub-list c[2]: {id(list_c[2])}")
print(f"ID sub-list d[2]: {id(list_d[2])}") # ID sub-list SAMA! (shallow)
print(f"Sebelum ubah D: List C = {list_c}")
print(f"Sebelum ubah D: List D = {list_d}")

list_d.append(4)       # Mengubah D tidak mengubah C
list_d[2].append(30)   # MENGUBAH SUB-LIST di D AKAN MENGUBAH C juga!

print(f"Setelah ubah D: List C = {list_c}") # Sub-list ikut berubah!
print(f"Setelah ubah D: List D = {list_d}")

print("\n--- Menggunakan copy.deepcopy() (Salinan Mendalam / Deep Copy) ---")
list_e = [1, 2, [10, 20]]
list_f = copy.deepcopy(list_e) # Membuat salinan baru, termasuk semua sub-list

print(f"ID objek list_e: {id(list_e)}")
print(f"ID objek list_f: {id(list_f)}") # ID nya BEDA!
print(f"ID sub-list e[2]: {id(list_e[2])}")
print(f"ID sub-list f[2]: {id(list_f[2])}") # ID sub-list juga BEDA! (deep)
print(f"Sebelum ubah F: List E = {list_e}")
print(f"Sebelum ubah F: List F = {list_f}")

list_f.append(4)       # Mengubah F tidak mengubah E
list_f[2].append(30)   # Mengubah sub-list di F TIDAK mengubah E

print(f"Setelah ubah F: List E = {list_e}") # E TIDAK berubah sama sekali
print(f"Setelah ubah F: List F = {list_f}")
