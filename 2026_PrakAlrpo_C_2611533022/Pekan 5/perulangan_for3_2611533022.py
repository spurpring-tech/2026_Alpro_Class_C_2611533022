# Buat file dengan nama perulangan_for3_NIM.py
# Buat program untuk perulangan dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Perulangan ini menggunakan fungsi input()

ulang_3022 = int(input("Masukkan jumlah perulangan: "))

jumlah_3022 = 0
for i_3022 in range(1, ulang_3022 + 1):
    print(i_3022, end=" ")
    jumlah_3022 = jumlah_3022 + 1

    if 1 < ulang_3022:
        print(" + ", end=" ")
    else:
        print(" = ",end=" ")
print()
print(f"jumlah = {jumlah_3022}")