# Buat file dengan nama nested_for3_NIM.py
# Buat program untuk perulangan dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Perulangan ini menggunakan fungsi input()

batas_3022 = int(input("Masukkan nilai batas: "))
for i_3022 in range(batas_3022 + 1):
    for j_3022 in range(batas_3022 + 1):
        print(i_3022 + j_3022, end=" ")
    print()