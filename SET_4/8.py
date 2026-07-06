# Write a program to find smallest and largest element in an array.


arr = list(map(int, input('enter array elements: ').split()))
sm = arr[0]
lg = arr[0]
for _ in arr:
    if _ < sm:
        sm = _
    if _ > lg:
        lg = _
print(f'smallest element: {sm}')
print(f'largest element: {lg}')
