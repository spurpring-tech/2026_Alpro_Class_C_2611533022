#Buat file dengan nama logika_NIM.py
#Nama variabel ditambah 4 digit terakhir NIM contoh: a1_1234
#Program ini menggunakan fungsi input()
#Program operator logika dalam Python

#Memasukkan nilai boolean
#Input tidak peka terhadap huruf besar dan kecil
a1_3022 = input("Masukkan nilai boolean-1 (True/False) untuk a1_3022: ").strip().lower() == "true"
a2_3022 = input("Masukkan nilai boolean-2 (True/False) untuk a2_3022: ").strip().lower() == "true"

#Konjungsi: Bernilai True jika keduanya True
hasil_3022 = a1_3022 and a2_3022
print("\nKonjungsi (AND)")
print("a1_3022 and a2_3022 =", hasil_3022)

#Disjungsi: Bernilai True jika salah satunya True
hasil_3022 = a1_3022 or a2_3022
print("\nDisjungsi (OR)")
print("a1_3022 or a2_3022 =", hasil_3022)

#Negasi a1: Membalikkan nilai a1
hasil_3022 = not a1_3022
print("\nNegasi a1 (NOT)")
print("not a1_3022 =", hasil_3022)

#Negasi a2: Membalikkan nilai a2
hasil_3022 = not a2_3022
print("\nNegasi a2 (NOT)")
print("not a2_3022 =", hasil_3022)

# XOR: Bernilai True jika kedua nilai berbeda
hasil_3022 = a1_3022 != a2_3022
print("\nXOR (Exclusive OR)")
print("a1_3022 XOR a2_3022 =", hasil_3022)