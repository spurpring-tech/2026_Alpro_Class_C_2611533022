pemasukkan = int(input("Jumlah pemasukkan: "))
kas = {}
total_kas = 0
print("Input nama *spasi* nominal")

for urutan in range(pemasukkan):
    data = input(f"Pemasukkan ke-{urutan + 1} dari {pemasukkan}: ").split()
    nama = data[0]
    jumlah = int(data[1])
    
    total_kas += jumlah
    if nama in kas:
        kas[nama] += jumlah
    else:
        kas[nama] = jumlah

nama_terbanyak = ""
kas_terbanyak = -1

for nama, total in kas.items():
    print(f"{nama}: {total}")
    if total > kas_terbanyak:
        kas_terbanyak = total
        nama_terbanyak = nama

print(f"Total cash: {total_kas}")
print(f"Top contributor: {nama_terbanyak} ({kas_terbanyak})")