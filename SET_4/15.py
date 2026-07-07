# Write a program for sorting the elements of an array.


arr = list(map(int, input('enter the array elements: ').split()))
n = len(arr)
for i in range(n):
    for j in range(i+1, n):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
print(f'ascending sorting: {arr}')
