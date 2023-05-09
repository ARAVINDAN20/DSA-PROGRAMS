# binary_search
def binary_search(list1, key):
    low = 0
    high = len(list1) - 1
    found = False
    while low <= high and not found:
        mid = (low + high) // 2
        if key == list1[mid]:
            found = True
        elif key > list1[mid]:
            low = mid + 1
        else:
            high = mid - 1
    if found == True:
        print("key is found")
    else:
        print("key is not found")

n = int(input("ENTER THE VALUE FOR LENGTH OF LIST :"))
list1 = list(map(int, input().strip().split(' ')))
list1.sort()
print(list1)
key = int(input("enter the value to check in list:"))
binary_search(list1,key)

# Linear_search
def Linear_search(a,n,x):
    for i in range(0,n):
        if (a[i] == x):
            return i
    return -1
a = list(map(int, input().strip().split(' ')))
x = 1
n = len(a)
result = Linear_search(a,n,x)
if(result==-1):
    print("Element not found!")
else:
    print("Element found at index: ", result)
