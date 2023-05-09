class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class Link_list:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("The link_list is empty!!")
        else:
            n = self.head
            while n is not None:
                print(f"{n.data} ---> ", end="")
                n = n.ref

    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def add_after(self, data, x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print("node is not present!!")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    def add_before(self,data,x):
        if self.head is None:
            print("The link_list is empty!!")
            return
        if self.head.data ==x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n= self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n=n.ref
        if n.ref is None:
            print("Node is not found!!")
        else:
            new_node =Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    def delete_begin(self):
        if self.head is None:
            print("THE LInk list is already empty!!")
        else:
            self.head = self.head.ref

    def delete_end(self):
        if self.head is None:
            print("THE LInk list is already empty!!")
        elif self.head.ref is None:
            self.head = None
        else:
            n = self.head
            while n.ref.ref is  not None:
                n = n.ref
            n.ref = None

    def delete_mid(self,x):
        if self.head is None:
            print("THE LInk list is already empty!!")
            return
        if x ==self.head.data:
            return
        n = self.head
        while n.ref is not None:
            if x ==n.ref.data:
                break
            n = n.ref
        if n.ref is None:
            print("The Node is not present!!!")
        else:
            n.ref = n.ref.ref

ll = Link_list()
# ll.add_begin(10)
# ll.add_end(9)
# ll.add_before(56,9)
# ll.add_after(5, 10)
# ll.add_begin(1)
# ll.add_begin(2)
# ll.delete_end()
# ll.delete_begin()
# ll.delete_mid(5)
# ll.display()
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
        ll.add_begin(n)
    elif cho == 2:
        n = int(input("Enter a data:"))
        ll.add_end(n)
    elif cho == 3:
        n = int(input("Enter a data:"))
        node_index = int(input("Enter a node after to be inserted: "))
        ll.add_after(n,node_index)
    elif cho == 4:
        n = int(input("Enter a data:"))
        node_index = int(input("Enter a node before to be inserted: "))
        ll.add_before(n,node_index)
    elif cho == 5:
        ll.delete_begin()
    elif cho == 6:
        ll.delete_end()
    elif cho == 7:
        n = int(input("Enter the node to be deleted:"))
        ll.delete_mid(n)
    elif cho == 8:
        ll.display()
    elif cho == 9:
        break
    else:
        print("Invalid Input :(")