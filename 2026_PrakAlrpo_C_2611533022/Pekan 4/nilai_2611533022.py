# Buat file dengan nama nilai_NIM.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 angka terakhir NIM, contoh: ipk_1234
# Program ini menggunakan fungsi input
# Program konversi nilai angka menjadi huruf

nilai_3022 = int(input("Masukkan nilai anda: "))

if nilai_3022 >= 81:
    print("A")
elif nilai_3022 >= 70:
    print("B")
elif nilai_3022 >= 60:
    print("C")
elif nilai_3022 >= 50:
    print("D")
else:
    print("E")