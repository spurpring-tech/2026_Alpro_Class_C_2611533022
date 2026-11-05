tinggi = int(input("Silahkan masukkan tinggi segitiga: "))

for row in range(tinggi, 0, -1):
    for column in range(row, 0, -1):
        print("*"*column)
    print()