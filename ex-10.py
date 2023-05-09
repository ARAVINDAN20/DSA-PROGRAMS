# quicksort- ex-10
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

arr = list(map(int, input("Enter the array:").strip().split(' ')))
sorted_arr = quick_sort(arr)
print(f"the sorted array is {sorted_arr}")

# def pivot_place(list1,first,last):
#     pivot = list1[first]
#     left = first+1
#     right = last
#     while True:
#         while left<=right and list1[left] <=pivot:
#
#             left = left+1
#         while left<= right and list1[right]>= pivot:
#             right = right-1
#         if right <left:
#             break
#         else:
#             list1[left],list1[right] = list1[right],list1[left]
#     list1[first],list1[right] = list1[right],list1[first]
#     return right
# def quick_sort(list1,first,last):
#     if first<last:
#         p = pivot_place(list1,first,last)
#         quick_sort(list1,first,p-1)
#         quick_sort(list1,p+1,last)
# myl = list(map(int,input("Enter the list:").strip().split(' ')))
# n = len(myl)
# quick_sort(myl,0,n-1)
# print(myl)

# marge_sort-ex10
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#
#     mid = len(arr) // 2
#     left_half = arr[:mid]
#     right_half = arr[mid:]
#
#     left_half = merge_sort(left_half)
#     right_half = merge_sort(right_half)
#
#     return merge(left_half, right_half)
#
# def merge(left_half, right_half):
#     result = []
#     left_index = right_index = 0
#
#     while left_index < len(left_half) and right_index < len(right_half):
#         if left_half[left_index] < right_half[right_index]:
#             result.append(left_half[left_index])
#             left_index += 1
#         else:
#             result.append(right_half[right_index])
#             right_index += 1
#
#     result.extend(left_half[left_index:])
#     result.extend(right_half[right_index:])
#     return result
#
# arr = list(map(int, input("Enter the array:").strip().split(' ')))
# sorted_arr = merge_sort(arr)
# print(f"the sorted array is {sorted_arr}")
#
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort the left and right halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted left and right halves
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr
arr = list(map(int, input("Enter the array:").strip().split(' ')))
sorted_arr = merge_sort(arr)
print(f"the sorted array is {sorted_arr}")
