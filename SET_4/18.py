# Write a program to find whether arrays are disjoint or not.


# arr1 = list(map(int, input('enter first array elements: ').split()))
# arr2 = list(map(int, input('enter second array elements: ').split()))
# disjoint = True
# for i in range(len(arr1)):
#     for j in range(len(arr2)):
#         if arr1[i] == arr2[j]:
#             disjoint = False
#             break
#     if not disjoint:
#         break
# if disjoint:
#     print('the arrays are disjoint.')
# else:
#     print('the arrays are not disjoint')



arr1 = list(map(int, input('enter first array elements: ').split()))
arr2 = list(map(int, input('enter second array elements: ').split()))
set1 = set(arr1)
disjoint = True
for num in arr2:
    if num in set1:
        disjoint = False
        break
if disjoint:
    print('the arrays are disjoint.')
else:
    print('the arrays are not disjoint.')
    