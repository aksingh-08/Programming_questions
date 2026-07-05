# Write a program to find missing elements of a range.


# arr = list(map(int, input('enter array elements: ').split()))
# start = int(input('enter the starting range: '))
# end = int(input('enter the ending range: '))
# print('missing are => ')
# for i in range(start, end+1):
#     if i not in arr:
#         print(i, end=" ")



arr = list(map(int, input('enter array elements: ').split()))
s = int(input('enter the starting range: '))
e = int(input('enter the ending range: '))
numbers = set(arr)
print('missing are:')
for i in range(s, e+1):
    if i not in numbers:
        print(i, end=' ')
        