# Write a program to check if two arrays are the same or not.


n = int(input('enter the number of elements: '))
arr1 = []
arr2 = []
print('enter the elements of first array:')
for i in range(n):
    arr1.append(int(input()))
print('enter the elements of second array:')
for i in range(n):
    arr2.append(int(input()))
if arr1 == arr2:
    print('both are the same.')
else:
    print('both are not same.')
    