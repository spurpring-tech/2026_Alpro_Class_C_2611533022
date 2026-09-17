#Buat file dengan nama aritmetika_NIM.py
#Buat program untuk operator aritmetika dalam python
#Nama variabel ditambah 4 digit terakhir NIM, contoh: angka1_1234
#Program ini menggunakan fungsi input() untuk
#Nilai yang dimasukkan akan dikonversi menjadi tipe data integer

angka1_3022 = int(input("Masukkan angka pertama: "))
angka2_3022 = int(input("Masukkan angka kedua: "))

#Penjumlahan
hasil_penjumlahan_3022 = angka1_3022 + angka2_3022
print("\noperator penjumlahan")
print("Hasil =", hasil_penjumlahan_3022)

#Pengurangan
hasil_pengurangan_3022 = angka1_3022 - angka2_3022
print("\noperator pengurangan")
print("Hasil =", hasil_pengurangan_3022)

#Perkalian
hasil_perkalian_3022 = angka1_3022 * angka2_3022
print("\noperator perkalian")
print("Hasil =", hasil_perkalian_3022)

#Pembagian, pembagian bulat, dan sisa bagi
if angka2_3022 != 0:
    hasil_pembagian_3022 = angka1_3022 / angka2_3022
    print("\noperator pembagian")
    print("Hasil =:", hasil_pembagian_3022)

    hasil_pembagian_bulat_3022 = angka1_3022 // angka2_3022
    print("\noperator pembagian bulat")
    print("Hasil =", hasil_pembagian_bulat_3022)

    sisa_bagi_3022 = angka1_3022 % angka2_3022
    print("\noperator sisa bagi")
    print("Hasil =", sisa_bagi_3022)
else:
    print("Angka kedua tidak boleh bernilai 0.")

#Pangkat
hasil_pangkat_3022 = angka1_3022 ** angka2_3022
print("\noperator pangkat")
print("Hasil =", hasil_pangkat_3022)

#lebih besar dari
hasil_3022 = angka1_3022 > angka2_3022
print("\noperator lebih besar dari")
print("angka1 > angka2:", hasil_3022)

#lebih kecil dari
hasil_3022 = angka1_3022 < angka2_3022
print("\noperator lebih kecil dari")
print("angka1 < angka2:", hasil_3022)

#lebih besar atau sama dengan
hasil_3022 = angka1_3022 >= angka2_3022
print("\noperator lebih besar atau sama dengan")
print("angka1 >= angka2:", hasil_3022)

#lebih kecil atau sama dengan
hasil_3022 = angka1_3022 <= angka2_3022
print("\noperator lebih kecil atau sama dengan")
print("angka1 <= angka2:", hasil_3022)