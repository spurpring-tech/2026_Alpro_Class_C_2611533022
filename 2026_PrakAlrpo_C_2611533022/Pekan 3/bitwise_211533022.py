#Buat file dengan nama bitwise_NIM.py
#Nama variabel ditambah 4 digit terakhir NIM contoh: angka1_1234
#Program ini menggunakan fungsi input()

print("=======================================")
print("OPERATOR BITWISE")
print("=======================================")

angka1_3022 = int(input("Masukkan angka bitwise-1: "))
angka2_3022 = int(input("Masukkan angka bitwise-2: "))

print("\nAngka dalam bentuk desimal dan biner:")
print("Angka 1: ", angka1_3022, "| Biner:", bin(angka1_3022))
print("Angka 2: ", angka2_3022, "| Biner:", bin(angka2_3022))

#Bitwise AND
hasil_3022 = angka1_3022 & angka2_3022
print("\nOperator Bitwise AND (&)")
print(angka1_3022, "&", angka2_3022, "=", hasil_3022)
print("Biner hasil_3022 = ", bin(hasil_3022))
print("Biner hasil_3022 (8 bit) = ", format(hasil_3022, '08b'))

#Bitwise OR
hasil_3022 = angka1_3022 | angka2_3022
print("\nOperator Bitwise OR (|)")
print(angka1_3022, "|", angka2_3022, "=", hasil_3022)
print("Biner hasil_3022 = ", bin(hasil_3022))
print("Biner hasil_3022 (8 bit) = ", format(hasil_3022, '08b'))

#Bitwise XOR
hasil_3022 = angka1_3022 ^ angka2_3022
print("\nOperator Bitwise XOR (^)")
print(angka1_3022, "^", angka2_3022, "=", hasil_3022)
print("Biner hasil_3022 = ", bin(hasil_3022))
print("Biner hasil_3022 (8 bit) = ", format(hasil_3022, '08b'))

#Bitwise NOT
hasil_3022 = ~angka1_3022
print("\nOperator Bitwise NOT (~)")
print("~", angka1_3022, "=", hasil_3022)
print("Biner hasil_3022 = ", bin(hasil_3022))
print("Biner hasil_3022 (8 bit) = ", format(hasil_3022, '08b'))

#Bitwise geser kiri
jumlah_geser_3022 = int(input("\nMasukkan jumlah bit pergeseran bit: "))
hasil_3022 = angka1_3022 << jumlah_geser_3022
print("\nOperator Bitwise geser kiri (<<)")
print(angka1_3022, "<<", jumlah_geser_3022, "=", hasil_3022)
print("Biner hasil_3022 = ", bin(hasil_3022))
print("Biner hasil_3022 (8 bit) = ", format(hasil_3022, '08b'))

#Bitwise geser kanan
hasil_3022 = angka1_3022 >> jumlah_geser_3022
print("\nOperator Bitwise geser kanan (>>)")
print(angka1_3022, ">>", jumlah_geser_3022, "=", hasil_3022)
print("Biner hasil_3022 = ", bin(hasil_3022))
print("Biner hasil_3022 (8 bit) = ", format(hasil_3022, '08b'))