# Program untuk mencari nilai maksimum dan mminimum dalam list

# Inisialisasi list kosong
angka_list = []
 
# Memminta pengguna memasukkan 10 angka integer
print("Masukkan 10 angka integer:")
for i in range(10):
    while True:
        try:
            angka = int(input(f"Masukkan angka ke-{i+1}: "))
            angka_list.append(angka)
            break
        except valueError:
            print("Input tidak valid! Mohon masukkan angka integer.")

# Mencari nilai maksimum dan minimum
nilai_maksimum = max(angka_list)
nilai_minimum = min(angka_list)

# Menampilkan hasil
print("\nlist angka:", angka_list)
print("Nilai maksimum:", nilai_maksimum)
print("Nilai minimum:", nilai_minimum)
