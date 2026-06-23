# Binary search is a search algorithm that finds the position of a target value within a sorted array.
# It works by repeatedly dividing the seach interval in half, comparing the target value to the middle element, 
# and eliminating the half where the target cannot lie until the target is found or the interval is empty.

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print("Sorted:", arr)
# print(f"6th element: {binary_search(arr, 6)} index")
element = int(input("Enter the element to search: "))
print(f"Target element present on {binary_search(arr, element)} index")