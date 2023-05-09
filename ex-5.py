class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None


class Doubly_Link_list:
    def __init__(self):
        self.head = None

    def display_frw(self):
        if self.head is None:
            print("The link_list is empty!!")
        else:
            n = self.head
            while n is not None:
                print(f"{n.data} ---> ", end="")
                n = n.nref

    def insert_begining(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head

            self.head.pref = new_node
            self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n

    def add_after(self, data, x):
        if self.head is None:
            print("The link_list is empty!!")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("Given Node is not present in Doubly_Link_list!!!")
            else:
                new_node = Node(data)
                new_node.nref = n.nref
                new_node.pref = n
                if n.nref is not none:
                    n.nref.npref = new_node
                n.nref = new_node

    def add_before(self, data, x):
        if self.head is None:
            print("The link_list is empty!!")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("Given Node is not present in Doubly_Link_list!!!")
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                else:
                    self.head = new_node
                n.pref = new_node

    def delete_begin(self):
        if self.head is None:
            print("Doubly_Link_list is empty, can't deleat!!")
            return
        if self.head.nref is None:
            self.head = None
            print("Doubly_Link_list is empty after deleating a Node!!")
        else:
            self.head = self.head.nref
            self.head.pref = None

    def delete_end(self):
        if self.head is None:
            print("Doubly_Link_list is empty, can't deleat!!")
            return
        if self.head.nref is None:
            self.head = None
            print("Doubly_Link_list is empty after deleating a Node!!")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.pref.nref = None

    def delete_by_value(self, x):
        if self.head is None:
            print("Doubly_Link_list is empty, can't deleat!!")
            return
        if self.head.nref is None:
            if x == self.head.data:
                self.head = None
            else:
                print("The number is undefind :(")
            return
        if self.head.data == x:
            self.head = self.head.nref
            self.head.pref = None
            return
        n = self.head
        while n.nref is not None:
            if x == n.data:
                break
            n = n.nref
        if n.nref is not None:
            n.nref.pref = n.pref
            n.pref.nref = n.nref
        else:
            if n.data == x:
                n.pref.nref = None
            else:
                print("The number is undefind :( ")


dll = Doubly_Link_list()
# dll=Doubly_Link_list()
# dll.insert_begining(10)
# dll.insert_end(20)
# dll.add_before(50,20)
# dll.deleat_begin()
# dll.display_frw()
# dll.display_rev()
while True:
    print('''
    1. Add_data front:
    2. Add_data end:
    3. Add_data after a Node:
    4. Add_data before a Node:
    5. Delete_data in front:
    6. Delete_data in end:
    7. Delete_data at mid:
    8. Display the Linkedlist:
    9. Exit
''')
    cho = int(input("Enter your choice:"))
    if cho == 1:
        n = int(input("Enter a data:"))
        dll.insert_begining(n)
    elif cho == 2:
        n = int(input("Enter a data:"))
        dll.insert_end(n)
    elif cho == 3:
        n = int(input("Enter a data:"))
        node_index = int(input("Enter a node after to be inserted: "))
        dll.add_after(n, node_index)
    elif cho == 4:
        n = int(input("Enter a data:"))
        node_index = int(input("Enter a node before to be inserted: "))
        dll.add_before(n, node_index)
    elif cho == 5:
        dll.delete_begin()
    elif cho == 6:
        dll.delete_end()
    elif cho == 7:
        n = int(input("Enter the node to be deleted:"))
        dll.delete_by_value(n)
    elif cho == 8:
        dll.display_frw()
    elif cho == 9:
        break
    else:
        print("Invalid Input :(")

