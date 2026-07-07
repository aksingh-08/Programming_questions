# Write a program for reversing an array.


# arr = list(map(int, input('enter array elements: ').split()))
# rev = []
# for _ in range(len(arr) - 1, -1, -1):
#     rev.append(arr[_])
# print(f'Reversed array: {rev}')



arr = list(map(int, input("enter array elements: ").split()))
left = 0
right = len(arr) - 1
while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1
print('reversed array: ', arr)
