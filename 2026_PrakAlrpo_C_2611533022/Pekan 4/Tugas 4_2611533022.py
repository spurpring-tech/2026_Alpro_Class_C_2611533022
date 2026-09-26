# Bagian 1
print("==== SELAMAT DATANG DI TUGAS4_2611533022 PARK! ====")
print("\nSebelum masuk ke park, silahkan isi formulir ini terlebih dahulu.")
Nama_3022 = input("Masukkan nama anda: ")
while True:
    Umur_input_3022 = input("Masukkan Umur anda: ")
    if Umur_input_3022.isdigit(): 
        Umur_3022 = int(Umur_input_3022)
        break
    print("Umur harus berupa angka bulat.")
while True:
    Tinggi_input_3022 = input("Masukkan tinggi badan anda (dalam cm): ")
    if Tinggi_input_3022.isdigit():
        Tinggi_3022 = int(Tinggi_input_3022)
        break
    print("Tinggi badan harus berupa angka bulat.")
while True:
    BB_input_3022 = input("Masukkan berat badan anda (dalam kg): ")
    if BB_input_3022.isdigit():
        BB_3022 = int(BB_input_3022)
        break
    print("Berat badan harus berupa angka bulat.")
Harga_Tiket_3022 = 0

# Bagian 2
print(f"\nBerikut data yang telah anda input\nNama: {Nama_3022}\nUsia: {Umur_3022} Tahun\nTinggi badan: {Tinggi_3022} cm\nBerat badan: {BB_3022} kg")

# Bagian 3
print("\n==== PILIH WAHANA YANG INGIN ANDA KUNJUNGI ====")

# Bagian 3.1
print("\nWahana 1: Bianglala Biang Raksasa\nWahana kincir ria berukuran besar yang berputar secara perlahan. Menyajikan pemandangan lanskap seluruh area taman hiburan dari ketinggian.")
print("\n  > Tidak memerlukan usia minimum\n  > Berat badan maksimum: 120kg\n  > Harga Tiket:\n   - Untuk 12 Tahun kebawah: Rp.20.000\n   - Untuk 13 Tahun keatas: Rp.30.000\n")

# Bagian 3.2
print("\nWahana 2: Roller Coaster Mini\nWahana kereta luncur tingkat sedang yang melintasi rel berbelok dan naik-turun. Cocok untuk anak-anak yang menyukai sensasi petualangan ringan.")
print("\n  > Usia minimum/maksimum: 5 Tahun/15 Tahun\n  > Tinggi minimum/maksimum: 100cm/145cm\n  > Berat badan maksimum: 75kg\n  > Perlu Bimbingan orang tua untuk anak dibawah 8 Tahun\n  > Harga tiket: Rp.15.000")

# Bagian 3.3
print("\nWahana 3: Roller Coaster Ekstrim\nKereta luncur kecepatan tinggi dengan lintasan curam, turunan tajam, dan putaran 360 derajat (loop) yang memicu adrenalin.")
print("\n  > Usia minimum: 16 Tahun\n  > Tinggi badan minimum: 140cm\n  > Berat badan maksimum: 90kg\n  > Harga tiket: Rp.35.000")

# Bagian 3.4
print("\nWahana 4: Arum Jeram Buatan\nWahana air menyusuri sungai buatan berketinggian dan berarus deras menggunakan perahu karet bulat. Penumpang akan merasakan sensasi cipratan air dan hempasan arus.")
print("\n  > Usia minimum: 7 Tahun\n  > Tinggi minimum: 120cm\n  > Berat badan maksimum: 80kg\n  > Harga tiket:\n   - 12 Tahun kebawah: Rp.30.000\n   - 13 Tahun keatas: Rp.40.000")

#  Bagian 3.5
print("\nWahana 5: Rumah berhantu\nWahana berjalan kaki atau menggunakan kereta mini menyusuri lorong gelap dengan berbagai kejutan dekoratif, efek suara, dan aktor penakut.")
print("\n  > Usia minimum 8 Tahun\n  > Harga tiket: Rp.15.000")

# Bagian 3.6
print("\nAll-Rounder Pass: Nikmati semua wahana hanya menggunakan satu tiket yang sama!\n  > Hanya berlaku untuk 18+\n  > Harga tiket: Rp.100.000")

# Bagian 4
while True:

    Tujuan_3022 = int(input("Silahkan pilih Opsi 1 sampai 6!"))

    match Tujuan_3022:
        case 1:
            if Umur_3022 <= 12 & BB_3022 <= 120:
                Harga_Tiket_3022 += 20000
                print("Wahana Bianglala Biang Raksasa telah dipilih!")
                break
            elif Umur_3022 >= 13 & BB_3022:
                Harga_Tiket_3022 += 30000
                print("Wahana Bianglala Biang Raksasa telah dipilih!")
                break
            else:
                print("Maaf, anda tidak memenuhi persyaratan masuk")
        case 2:
            if Umur_3022 >= 5 & Umur_3022 <=15 & Tinggi_3022 >= 100 & Tinggi_3022 <= 145 & BB_3022 <= 75:
                Harga_Tiket_3022 += 15000
                print("Wahana Roller Coaster Mini telah dipilih!")
                break
            else:
                print("Maaf, anda tidak memenuhi persyaratan masuk")
        case 3:
            if Umur_3022 >= 12 & Tinggi_3022 >= 140 & BB_3022 >= 90:
                Harga_Tiket_3022 += 35000
                print("Wahana Roller coaster ekstrim telah dipilih!")
                break
            else:
                print("Maaf, anda tidak memenuhi persyaratan masuk")
        case 4:
            if Umur_3022 <= 12 & BB_3022 <= 80 & Tinggi_3022 <= 120:
                Harga_Tiket_3022 += 30000
                print("Wahana Arung Jeram Buatan dipilih!")
                break
            elif Umur_3022 >= 13 & BB_3022 <= 80 & Tinggi_3022 <= 120:
                Harga_Tiket_3022 += 40000
                print("Wahana Arung Jeram Buatan dipilih")
                break
        case 5:
            if Umur_3022 >= 8 & Umur_3022 < 15:
                Harga_Tiket_3022 += 15000
                print("Wahana Rumah berhantu telah dipilih!")
                break
            elif Umur_3022 >= 15:
                Harga_Tiket_3022 += 15000
                print("Wahana Rumah berhantu telah dipilih!")
                break
        case 6:
            if Umur_3022 > 18:
                Harga_Tiket_3022 += 100000
                print("Tiket All-rounder pass telah dipilih.")
                break
            else:
                print("Maaf, usia anda tidak memenuhi persyaratan.")
        case _:
            print("Input tidak valid, coba lagi.")

# Bagian 5
Total_Harga_3022 = Harga_Tiket_3022
Vip_Discount = Harga_Tiket_3022 - 5000
Vip_Input = input("\nApakah anda memiliki pass vip? [Y/N]").lower
if Vip_Input == "y":
    Total_Harga_3022 -= Vip_Discount
else:
    Vip_Discount = 0

# Bagian 6
print("\n====== PEMBAYARAN ======")
print(f"\nBerikut rincian harga\nBiaya Wahana: {Harga_Tiket_3022}\nDiskon member: {Vip_Discount}\n\nBiaya yang harus dibayar: {Total_Harga_3022}")
print("\nTerimakasih telah datang, silahkan berkunjung lagi ke wahana kami!")