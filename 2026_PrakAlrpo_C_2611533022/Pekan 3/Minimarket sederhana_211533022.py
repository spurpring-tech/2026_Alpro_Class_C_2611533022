# Store data awal
# 1. Memasukkan data harga barang
harga_barang = {"beras": 85000, "gula": 5000, "minyak goreng": 20000, "telur": 2000, "susu": 10000, 
"kecap": 15000, "mie instan": 3000, "kopi": 10000, "teh": 5000, "roti": 15000, 
"air mineral": 5000, "sabun": 10000, "pasta gigi": 15000, "shampoo": 25000,
"popok": 30000, "tisu": 10000, "deterjen": 15000, "pembersih lantai": 20000,
"deodorant": 15000, "parfum": 30000, "minyak wangi": 40000, "lotion": 35000,
"saos": 10000, "sambal": 8000, "bumbu": 12000, "saus tiram": 12000, "saus tomat": 10000, 
"saus mayones": 15000, "saus barbekyu": 20000,}

# 2. Memasukkan data pelanggan vip
pelanggan_vip = ["Angga", "Bob", "Cahya", "Dewi", "Eka"]

# 3. Memasukkan data diskon
diskon_vip = 0.1 # 10% diskon untuk pelanggan vip

# 4. Memasukkan data pajak
pajak = 0.011 # 1.1% pajak untuk semua pembelian

# 5. Melakukan tranksaksi
print("Selamat datang di Minimarket kami!")
nama_pelanggan = input("\nMasukkan nama pelanggan: ")
total_belanja = 0
jumlah_barang = 0

while True:
    barang = input("Masukkan nama barang (atau ketik 'selesai' untuk mengakhiri): ")
    if barang.lower() == 'selesai':
            break
    if barang in harga_barang:
            jumlah = int(input(f"Masukkan jumlah {barang}: "))
            harga_produk = harga_barang[barang]
            total_belanja += harga_produk * jumlah
            jumlah_barang += jumlah
    else:
            print("Barang tidak tersedia. Silakan coba lagi.")

# 6. Menghitung diskon
    diskon_total = 0
    if nama_pelanggan in pelanggan_vip:
        diskon_total += total_belanja * diskon_vip

# 7. Menghitung pajak
    pajak_total = (total_belanja - diskon_total) * pajak

# 8. Total akhir yang harus dibayar
total_akhir = total_belanja - diskon_total + pajak_total

print(f"\nTotal belanja: Rp{total_belanja}")
print(f"Diskon: Rp{diskon_total}")
print(f"Pajak: Rp{pajak_total}")
print(f"Total akhir yang harus dibayar: Rp{total_akhir}")
jenis_transaksi = input("Jenis transaksi apa yang ingin dilakukan? (Tunai/Non-Tunai): ")
if jenis_transaksi.lower() == 'tunai':
    print("Baik, ini struk pembayaran Anda.")
    print("Terima kasih telah berbelanja di Minimarket kami!")
elif jenis_transaksi.lower() == 'non-tunai':
    print("Silakan lakukan pembayaran melalui aplikasi.")
    print("Baik, ini struk pembayaran Anda. Terima kasih telah berbelanja di Minimarket kami!")
print("\n================================")

# 9. Mengulangi transaksi atau selesai
ulang = input("\nApakah Anda ingin melakukan transaksi lagi? (ya/tidak): ")
if ulang.lower() == 'ya':
    # Reset total belanja dan jumlah barang
    total_belanja = 0
    jumlah_barang = 0
    # Memulai transaksi baru
    print("\nTransaksi baru dimulai.")
else:
    print("Program selesai, menutup terminal.")