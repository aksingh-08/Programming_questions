# Write a program to find triplets with a given sum.


# arr = list(map(int, input('enter array elements: ').split()))
# tagt = int(input('enter the target sum: '))
# n = len(arr)
# found = False
# for i in range(n-2):
#     for j in range(i+1, n-1):
#         for k in range(j+1, n):
#             if arr[i] + arr[j] + arr[k] == tagt:
#                 print(f'triplets: {arr[i]} {arr[j]} {arr[k]}')
#                 found = True
# if not found:
#     print('no triplet exists.')



arr = list(map(int, input('enter array elements: ').split()))
target = int(input('enter the target sum: '))
arr.sort()
n = len(arr)
found = False
for i in range(n-2):
    left = i+1
    right = n-1
    while left < right:
        first_sum = arr[i] + arr[left] + arr[right]
        if first_sum == target:
            print(f'triplets: {arr[i]} {arr[left]} {arr[right]}')
            found = True
            left += 1
            right -= 1
        elif first_sum < target:
            left += 1
        else:
            right -= 1
if not found:
    print('no triplets exists.')
    