# Write a program to find second smallest element in an array.


# arr = list(map(int, input('enter array elements: ').split()))
# smallest = float('inf')
# second_smallest = float('inf')
# for num in arr:
#     if num < smallest:
#         second_smallest = smallest
#         smallest = num
#     elif num < second_smallest and num != smallest:
#         second_smallest = num
# if second_smallest == float('inf'):
#     print('invalid')
# else:
#     print(second_smallest)



arr = list(map(int, input('enter array elements: ').split()))
smallest = arr[0]
second_smallest = None
for num in arr[1:]:
    if num < smallest:
        second_smalllest = smallest
        smallest = num
    elif num != smallest:
        if second_smallest is None or num < second_smallest:
            second_smallest = num
if second_smallest is None:
    print('second smallest element does not exist.')
else:
    print(second_smallest)
    