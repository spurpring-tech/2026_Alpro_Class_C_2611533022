segitiga_3022 = int(input("Masukkan tinggi segitiga: "))
for i_3022 in range(1, segitiga_3022 + 1):
    for j_3022 in range(segitiga_3022 - i_3022):
        print(" ", end="")
    print(" *" * i_3022)