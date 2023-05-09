# Ex-7= selection sort and INSERTION

# selection o(n**2)
def sel(num):
    for i in range(len(num)):
        min = i
        for j in range(i + 1, len(num)):
            if num[min] > num[j]:
                min = j
        num[i], num[min] = num[min], num[i]
    print(num)

clist = list(map(int,input("Enter the list elements:").strip().split(" ")))
print(clist, "\n after sorting!!!!")
sel(clist)


# INSERTION o(n**2)
def ins(num):
    for i in range(1, len(num)):
        key = num[i]
        j = i - 1
        while j >= 0 and key < num[j]:
            num[j + 1] = num[j]
            j -= 1
        num[j + 1] = key
    print(num)


mylist = list(map(int,input("Enter the list elements:").strip().split(" ")))
print(mylist, "\n after sorting!!!!")
ins(mylist)
