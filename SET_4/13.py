# Write a program to find sum of positive square elements in an array.


arr = list(map(int, input('enter array elements: ').split()))
total = 0
for _ in arr:
    if _ > 0:
        total += _ * _
print(f'sum of squares of positive elements: {total}')
