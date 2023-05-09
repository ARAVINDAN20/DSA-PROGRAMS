class csc:
    def __init__(self):
        self.stack = list()  # list=[12,34,5,]
        self.maxsize = 5
        self.top = -1

    def push(self, data):
        if self.top == self.maxsize - 1:
            print("stack is Full")
        else:
            self.top = self.top + 1
            self.stack.append(data)

    def display(self):
        print(self.stack)

    def pop(self):
        if self.top == -1:
            print("stack is underflow!!!")
        else:
            item = self.stack.pop()
            self.top = self.top - 1
            print("deleted item", item)

    def peek(self):
        if self.top == 1:
            print("stack is empty")
        else:
            print(self.stack[self.top])


Icsc = csc()
while (1):
    print("1. Push")
    print("2. pop")
    print("3. display")
    print("4. peek")
    print("5.Exit")
    choice = int(input("enter your choice:"))
    if choice == 1:
        value = int(input("Enter the data:"))
        Icsc.push(value)
    elif choice == 2:
        Icsc.pop()
    elif choice == 3:
        Icsc.display()
    elif choice == 4:
        Icsc.peek()
    else:
        break


