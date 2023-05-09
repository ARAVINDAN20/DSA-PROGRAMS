# chaning to handle collision Time complexity it can be 0(n)
class Hash_Table:
    def __init__(self):
        self.MAX = 10
        self.arru = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def add(self, key, val):  # __setitem__ is for using in dictionary              #add(self,key,val):
        h = self.get_hash(key)
        #         self.arru[h] = val
        found = False
        for index, element in enumerate(self.arru[h]):
            if len(element) == 2 and element[0] == key:
                self.arru[h][index] = (key, val)
                found = True
                break
        if not found:
            self.arru[h].append((key, val))

    def get(self, key):  # __getitem__ is for using in dictionary             #get(self,key):
        h = self.get_hash(key)
        for element in self.arru[h]:
            if element[0] == key:
                return element[1]

    def delete(self, key):  # __delitem__  is for using in dictionary for delete     #delete(self,key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arru[h]):
            if element[0] == key:
                del self.arru[h][index]


ht = Hash_Table()
while True:
    print(
        "1.Insert the element and value in Hash_Table\n2.Get_a_value\n3.Get_a_hash_value\n4.Disply\n5.Delete_element\n6.Exit")
    cho = int(input("Enter your choice:"))
    if cho == 1:
        element = str(input("Enter the element as a string:"))
        val = int(input("Enter the value of element:"))
        #         return ht[element] = val
        ht.add(element, val)
    elif cho == 2:
        element = str(input("Enter the element as a string:"))
        print(ht.get(element))
    elif cho == 3:
        element = str(input("Enter the element as a string:"))
        print(ht.get_hash(element))
    elif cho == 4:
        print(ht.arru)
    elif cho == 5:
        element = str(input("Enter the element as a string:"))
        ht.delete(element)
    elif cho == 6:
        break
    else:
        print("invaled input!! :(")
