#Program Operasi Dasar pada List




# 1. Membuat list kosong
my_list = []
print("List kosong awal:", my_list)

# 2. Menambah elemen 10, 20, 30, 40, 50
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.append(50)
print("List setelah menambahkan elemen:", my_list)
 
# 3. Hapus elemen pertama dan terakhir dari list
my_list.pop(0) # menghapus elemen pertama dari list
my_list.pop() # menghapus elemen terakhir
print("List setelah menghapus elemen pertama dan terakhir:", my_list)

# 4. Sisipkan angka 25 pada indekkks ke-2
my_list.insert(2, 25)
print("List settelah menyisipkan 25 pada indeks ke-2:", my_list)
