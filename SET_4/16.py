# Write a program for reversing an array.


arr = list(map(int, input('enter array elements: ').split()))
rev = []
for _ in range(len(arr) - 1, -1, -1):
    rev.append(arr[_])
print(f'Reversed array: {rev}')
