
jumlah_barang = int(input("Masukkan Jumlah Barang: "))
    
total_harga = 0

for i in range(1, jumlah_barang + 1):
        harga_barang = float(input(f"Masukkan Harga Barang Ke-{i}: "))
        total_harga += harga_barang 

print(f"Total Belanjaan Rp.{total_harga:.2f}")

