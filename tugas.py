class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Insert Depan
    def insert_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert Belakang
    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # Hapus Depan
    def delete_front(self):
        if self.head is None:
            return None
        temp_node = self.head
        self.head = self.head.next
        temp_node.next = None
        return temp_node.data

    # Hapus Belakang
    def delete_end(self):
        if self.head is None:
            return None
        if self.head.next is None:
            self.head = None
            return None
        last_node = self.head
        while last_node.next.next:
            last_node = last_node.next
        temp_node = last_node.next
        last_node.next = None
        return temp_node.data

    # Hapus Semua
    def delete_all(self):
        self.head = None

    # Tampilkan Data
    def display(self):
        if self.head is None:
            print("Linked List kosong")
            return
        current_node = self.head
        while current_node:
            print(current_node.data, end=' ')
            current_node = current_node.next
        print()


# Contoh penggunaan program
linked_list = LinkedList()

while True:
    print("1. Insert Depan")
    print("2. Insert Belakang")
    print("3. Hapus Depan")
    print("4. Hapus Belakang")
    print("5. Hapus Semua")
    print("6. Tampilkan Data")
    print("7. Keluar")

    choice = int(input("Masukkan pilihan anda: "))

    if choice == 1:
        data = input("Masukkan data yang ingin diinsert di depan: ")
        linked_list.insert_front(data)
    elif choice == 2:
        data = input("Masukkan data yang ingin diinsert di belakang: ")
        linked_list.insert_end(data)
    elif choice == 3:
        data = linked_list.delete_front()
        if data is not None:
            print("Data yang dihapus dari depan: ", data)
    elif choice == 4:
        data = linked_list.delete_end()
        if data is not None:
            print("Data yang dihapus dari belakang: ", data)
    elif choice == 5:
        linked_list.delete_all()
        print("Linked List berhasil dihapus")
    elif choice == 6:
        linked_list.display()
    elif choice == 7:
        break
    else:
        print("Pilihan tidak valid, coba lagi")
