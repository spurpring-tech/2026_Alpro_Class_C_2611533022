# Tugas membuat PROGRAM JAM PASIR KRISTAL PALINDROMIK

N_3022 = int(input("Masukkan tinggi jam pasir (N): "))
if N_3022 <= 0:
    print("Tinggi jam pasir harus lebih besar dari 0.")
elif N_3022 > 9:
    print("Tinggi jam pasir maksimum adalah 9.")
else:
    print("#" + "=" * (3 * N_3022 - (N_3022 - 3)) + "#")

# Bagian atas jam pasir
for i_3022 in range(N_3022, 0, -1):
    kiri_3022 = "".join(str(j_3022) for j_3022 in range(i_3022, 0, -1))
    kanan_3022 = "".join(str(j_3022) for j_3022 in range(1, i_3022 + 1))
    spasi_3022 = " " * (N_3022 - i_3022)

    print("|" + spasi_3022 + kiri_3022 + "<*>" + kanan_3022 + spasi_3022 + "|")

# Bagian tengah jam pasir
print("|" + " " * N_3022 + "<*>" + " " * N_3022 + "|")

# Bagian bawah jam pasir
for i_3022 in range(1, N_3022 + 1):
    kiri_3022 = "".join(str(j_3022) for j_3022 in range(i_3022, 0, -1))
    kanan_3022 = "".join(str(j_3022) for j_3022 in range(1, i_3022 + 1))
    spasi_3022 = " " * (N_3022 - i_3022)

    print("|" + spasi_3022 + kiri_3022 + "<*>" + kanan_3022 + spasi_3022 + "|")

print("#" + "=" * (3 * N_3022 - (N_3022 - 3)) + "#")