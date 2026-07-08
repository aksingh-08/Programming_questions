# Write a program to find non-repeating elements of an array.


arr = list(map(int, input('enter array elements: ').split()))
frequency = {}
for num in arr:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
print('non-repeating elements:')
for num in arr:
    if frequency[num] == 1:
        print(num, end=" ")
        