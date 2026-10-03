# Buat file dengan nama perulangan_for4_NIM.py
# Buat program untuk perulangan dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Perulangan ini menggunakan fungsi input()

tinggi_3022 = int(input("Masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_3022 % 2 != 0:
    print("Tinggi harus bilangan genap.")
else:
    a_3022 = tinggi_3022
    c_3022 = a_3022
    lebar_3022 = (2 * tinggi_3022) - 2

    for i_3022 in range(1, tinggi_3022 + 1):
        b_3022 = c_3022 + 1

        for j_3022 in range(1, lebar_3022 + 1):
            
            # Baris atas dan bawah
            if i_3022 == 1 or i_3022 == tinggi_3022:
                if j_3022 == 1 or j_3022 == lebar_3022:
                    print("#", end="")
                else:
                    print("=", end="") 
            # Baris isi
            else:
                if j_3022 == 1 or j_3022 == lebar_3022:
                    print("|", end="")
                else:
                    if j_3022 == c_3022:
                        print("<", end="")
                    elif j_3022 == b_3022:
                        print(">", end="")
                    elif j_3022 == (lebar_3022 - c_3022):
                        print("<", end="")
                    elif j_3022 == (lebar_3022 - c_3022 + 1):
                        print(">", end="")
                    elif j_3022 > b_3022 and j_3022 < (lebar_3022 - c_3022):
                        print(".", end="")
                    else:
                        print(" ", end="")
print()

a_3022 -= 2

# Logika asli Java
if a_3022 <= 0:
    c_3022 = (-a_3022) + 2
else:
    c_3022 = a_3022