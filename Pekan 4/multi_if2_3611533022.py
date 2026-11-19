# Buat file dengan nama multiif2_NIM.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 angka terakhir NIM, contoh: ipk_1234
# Program ini menggunakan fungsi input

#Input dari User
total_belanja_3022 = float(input("Masukkan total belanja: (Rp) "))

# Input status member (mengecek apakah user mengetik 'y' atau 'ya')
input_member_3022 = input("Apakah pelanggan ini bagian dari member? [y/n]: ").strip().lower()
is_member_3022 = input_member_3022 in ['y','ya']

# Input status kode promo (mengecek apakah user mengetik 'y' atau 'ya'
input_promo_3022 = input("Apakah kode promo valid? [y/n]: ").strip().lower()
kode_promo_valid_3022 = input_promo_3022 in ["y","ya"]

total_diskon_persen_3022 = 0

# Multi If terpisah:

if total_belanja_3022 > 1000000:
    total_diskon_persen_3022 += 10 # Diskon belanja besar
if is_member_3022:
    total_diskon_persen_3022 += 5 # Diskon member
if kode_promo_valid_3022:
    total_diskon_persen_3022 += 10 # Diskon voucher

# Menghitung total nominal belanja dan diskon
nominal_diskon_3022 = total_belanja_3022 + (total_diskon_persen_3022/100)
total_bayar_3022 = total_belanja_3022 - nominal_diskon_3022

# output hasil
print("---Rincian Pembayaran---")
print(f"Total diskon:  {total_diskon_persen_3022}% (Rp. {nominal_diskon_3022:,.0f})")
print(f"Total bayar: Rp {total_bayar_3022:,.0f}")

print(f"Total diskon yang anda dapatkan {total_diskon_persen_3022}%")
# Total diskon yang anda dapatkan: 10% jika belanja > 1 juta, member, dan kode promo valid