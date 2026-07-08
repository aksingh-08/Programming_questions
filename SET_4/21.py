# Write a program to find whether the numbers of an array be made equal.


arr = list(map(int, input('enter array elements: ').split()))
for i in range(len(arr)):
    while arr[i] % 2 == 0:
        arr[i] //= 2
same = True
for i in range(1, len(arr)):
    if arr[i] != arr[0]:
        same = False
        break
if same:
    print('all numbers can be made equal.')
else:
    print('all numbers cannot be made equal.')
