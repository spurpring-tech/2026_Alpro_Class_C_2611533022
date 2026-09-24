# Buat file dengan nama if_elif_else_NIM.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 angka terakhir NIM, contoh: ipk_1234
# Program ini menggunakan fungsi input

umur_3022 = int(input("Input usia anda: "))
sim_3022 = input("Apakah anda sudah memiliki sim C? [y/n]: ")[0]

if umur_3022 >= 17 and sim_3022 == 'y':
    print("Anda sudah dewasa, dan boleh membawa motor")
elif umur_3022 >= 17 and sim_3022 != 'y':
    print("Anda sudah dewasa, tetapi belum diizinkan membawa motor")
elif umur_3022 < 17 and sim_3022 != 'y':
    print("Anda belum cukup umur untuk menggunakan motor")
else:
    print("Nak, polisi mana yang anda sogok?? -_-")
print("Program selesai")