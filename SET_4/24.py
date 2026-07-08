# Write a program to count distinct elements of an array.


arr = list(map(int, input('enter array elements: ').split()))
distinct = set(arr)
print(f'number of distinct elements: {len(distinct)}')
print(f'distinct elements: {distinct}')
