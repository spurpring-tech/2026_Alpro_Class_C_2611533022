#Buat file dengan nama lainnya_NIM.py
#Nama variabel ditambah 4 digit terakhir NIM contoh: a1_1234
#Program ini menggunakan fungsi input()
#Program operator keanggotaan dan identias

print("=======================================")
print("1. OPERATOR KEANGGOTAAN")
print("=======================================")

# Input beberapa data yang dipisahkan dengan koma
input_data_3022 = input("Masukkan beberapa data, pisahkan dengan koma: ")

# Mengubah input menjadi list interger
data_3022 = [int(item.strip()) for item in input_data_3022.split(",")]

nilai_dicari_3022 = int(input("Masukkan angka yang ingin dicari: "))

#Operator In
hasil_3022 = nilai_dicari_3022 in data_3022
print("\nOperator keanggotaan In")
print(nilai_dicari_3022, "in", data_3022, "=", hasil_3022)

#Operator Not In
hasil_3022 = nilai_dicari_3022 not in data_3022
print("\nOperator keanggotaan Not In")
print(nilai_dicari_3022, "not in", data_3022, "=", hasil_3022)   

print("=======================================")
print("2. OPERATOR IDENTITAS")
print("=======================================")

# Objek 1 menggunakan list dari pengguna
objek1_3022 = data_3022

# Objek 2 merujuk pada objek yang sama dengan objek 1
objek2_3022 = objek1_3022

# Objek 3 memiliki isi sama, tetapi merupakan objek baru
objek3_3022 = data_3022.copy()

print("objek1_3022 =", objek1_3022)
print("objek2_3022 =", objek2_3022)
print("objek3_3022 =", objek3_3022)

# Operator Is
hasil_3022 = objek1_3022 is objek2_3022
print("\nOperator identitas Is")
print("objek1_3022 is objek2_3022 = ", hasil_3022)

# Operator Is Not
hasil_3022 = objek1_3022 is not objek3_3022
print("\nOperator identitas Is Not")
print("objek1_3022 is not objek3_3022 = ", hasil_3022)

# Membandingkan identitas dan nilai
print("\nPerbandingan identitas dan nilai:")
print("objek1_3022 is objek3_3022:", objek1_3022 is objek3_3022)
print("objek1_3022 == objek3_3022:", objek1_3022 == objek3_3022)