# Repeatedly compare adjacent elements and swap them if in the wrong order. 
# After each pass, the largest unsorted element 'bubbles' to its correct position.


def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
data = [64, 34, 25, 12, 22, 11, 90]
print("Original:", data)
print("Sorted: ", bubble_sort(data))
