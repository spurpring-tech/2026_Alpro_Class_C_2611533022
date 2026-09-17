#Buat file dengan nama assignment_NIM.py
#Nama variabel ditambah 4 digit terakhir NIM contoh: angka1_1234
#Program ini menggunakan fungsi input()
#Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
#Program operator assignment dalam Python

angka1_3022 = int(input("Input angka 1: "))
angka2_3022 = int(input("Input angka 2: "))

print("\nNilai awal angka1_3022 =", angka1_3022)
print("Nilai angka2_3022 =", angka2_3022)

#assignment biasa
hasil_3022 = angka1_3022
print("\nAssignment biasa (=)")
print("hasil_3022 = ", hasil_3022)

#assignment penjumlahan
hasil_3022 = angka1_3022
hasil_3022 += angka2_3022
print("\nAssignment penjumlahan (+=)")
print("hasil_3022 = ", hasil_3022)

#assignment pengurangan
hasil_3022 = angka1_3022
hasil_3022 -= angka2_3022
print("\nAssignment pengurangan (-=)")
print("hasil_3022 = ", hasil_3022)

#assignment perkalian
hasil_3022 = angka1_3022
hasil_3022 *= angka2_3022
print("\nAssignment perkalian (*=)")
print("hasil_3022 = ", hasil_3022)

#assignment pembagian, pembagian bulat, dan sisa bagi
if angka2_3022 != 0:
    hasil_3022 = angka1_3022
    hasil_3022 /= angka2_3022
    print("\nAssignment pembagian (/=)")
    print("hasil_3022 = ", hasil_3022)

    hasil_3022 = angka1_3022
    hasil_3022 //= angka2_3022
    print("\nAssignment pembagian bulat (//=)")
    print("hasil_3022 = ", hasil_3022)

    hasil_3022 = angka1_3022
    hasil_3022 %= angka2_3022
    print("\nAssignment sisa bagi (%=)")
    print("hasil_3022 = ", hasil_3022)
else:
    print("\nPembagian tidak dapat dilakukan")
    print("Angka 2 tidak boleh bernilai 0.")

# Operator tambahan: assignment perpangkatan
hasil_3022 = angka1_3022
hasil_3022 **= angka2_3022
print("\nAssignment perpangkatan (**=)")
print("hasil_3022 = ", hasil_3022)