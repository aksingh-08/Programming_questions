# Write a program to find sum of elements in an array.


arr = list(map(int, input('enter array elements: ').split()))
total = 0
for num in arr:
    total += num
print(f'sum of elements: {total}')
