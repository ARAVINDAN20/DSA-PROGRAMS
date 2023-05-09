class queue:
    def __init__(self):
        self.queue = list()
        self.maxsize = 5
        self.queue = [None] * self.maxsize
        self.front = -1
        self.rear = -1

    def enqueue(self, data):
        if self.rear == self.maxsize - 1:
            print("queue is full")
        else:
            if self.front == -1:
                self.front = 0
            self.rear = self.rear + 1
            self.queue[self.rear] = data

    try:
        def dequeue(self):
            if self.front == -1:
                print("queue is empty")
            else:
                print("deleted item", self.queue[self.front])
                self.queue[self.front] = None
                self.front = self.front + 1
    except:
        print("the queue is empty")

    def display(self):
        if self.front == -1:
            print("queue is empty ::")
        else:
            i = self.front
            while (i <= self.rear):
                print(self.queue[i])
                i = i + 1

    def peek(self):
        if self.front == -1:
            print("queue is empty")
        else:
            print(self.queue[self.front])


Icse = queue()
while (1):
    print("1.enqueue:\n2.dequeue:\n3.display:\n4.peek:\n5 exit")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        value = int(input("Enter the data:"))
        Icse.enqueue(value)
    elif choice == 2:
        Icse.dequeue()
    elif choice == 3:
        Icse.display()
    elif choice == 4:
        Icse.peek()

    else:
        break