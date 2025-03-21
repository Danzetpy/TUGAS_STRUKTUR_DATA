class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Menambah node baru di akhir list"""
        new_node = Node(data)
        
        # Jika Linked list kosong
        if self.head  is None:
            self.head = new_node
            return
        # Mencari node terakhir
        current = self.head
        while current.next:
            current = current.next

        # Menambah node baru di akhir
        current.next = new_node

    def delete_first(self):
        """Menghapus node pertama"""
        # Jika linked list kosong
        if self.head is None:
            print("Linked list kosong, tidak ada yang dapat dihapus")
            return

        # Simpan referensi ke node pertama
        temp = self.head

        # Mengubah head menjadi node kedua
        self.head = self.head.next

        # Hapus referensi dari node pertama
        temp = None

    def display(self):
        """Menampilkan semua elemen dalam linked list"""
        # Jika linked list kosong
        if self.head is None:
            print("Linked list kosong")
            return
        
        current = self.head
        while current:
            print(current.data, end=" -> ")
            curent = current.next
        print("None")

# Contoh penggunaan
if __name__ == "__main__":
    # Membuat linked list baru
    my_list = LinkedList()

    # Membuat elemen
    my_list.append(10)
    my_list.append(20)
    my_list.append(30)

    # Menampilkan elemen
    print("Linked list setelah penambahan:")
    my_list.display()

    # Menghapus elemen pertama
    my_list.delete_first()

    # Menampilkan elemen setelah penghapusan
    print("Linked list setelah penghapusan:")
    my_list.display
                  

        