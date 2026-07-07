# Write a program to find whether an array is a subset of another array or not.


# arr1 = list(map(int, input('enter first array elements: ').split()))
# arr2 = list(map(int, input('enter second array elements: ').split()))
# subset = True
# for i in range(len(arr2)):
#     found = False
#     for j in range(len(arr1)):
#         if arr2[i] == arr1[j]:
#             found = True
#             break
#     if not found:
#         subset = False
#         break
# if subset:
#     print('array2 is a subset of array1.')
# else:
#     print('array2 is not a subset of array1.')



array1 = list(map(int, input("Enter first array elements: ").split()))
array2 = list(map(int, input("Enter second array elements: ").split()))
set1 = set(array1)
subset = True
for num in array2:
    if num not in set1:
        subset = False
        break
if subset:
    print("Array2 is a subset of Array1.")
else:
    print("Array2 is not a subset of Array1.")