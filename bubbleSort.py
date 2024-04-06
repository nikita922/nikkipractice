def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

list1 = [8,1,6,7,9,5,3,4,5]
list2 = [1,2,7,45,3,4,8,9,1]

merged_list = list1 + list2
bubble_sort(merged_list)

second_largest = merged_list[-2]
print("Merged List:", merged_list)
print("Second Largest Element:", second_largest)
