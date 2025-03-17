class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements
    
    def insert_at(self, position, value):
        new_node = Node(value)

        # Jika posisi 0 atau linked listl kosong, tambahkan di awal
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        # Mencari posisi untuk penyisipan
        current = self.head
        for i in range(position - 1):
            if current is None:
                # Jika posisi melebihi panjang list, tambahkan di akhir
                print(f"Posisi {position} melebihi panjang list. Menambahkan di akhir.")
                self.append(value)
                return
            current = current.next

        # Jika mencapai akhir list
        if current is None:
            self.append(value)
            return
        
        # Menyisipkan node baru
        new_node.next = current.next
        current.next = new_node

# Contoh penggunaan
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)
    linked_list.append(40)

    print("Linked List awal:", linked_list.display())

    linked_list.insert_at(2, 50)
    print("Setelah insert_at(2, 50):", linked_list.display())

    linked_list.insert_at(0, 5)
    print("Setelah insert_at(0, 5):", linked_list.display())

    linked_list.insert_at(10, 100)
    print("Setelah insert_at(10, 100):", linked_list.display())
