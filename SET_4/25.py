# Write a program to find repeating elements in an array.


arr = list(map(int, input('enter array elements: ').split()))
frequency = {}
for num in arr:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
print('repeating elements:')
found = False
for key in frequency:
    if frequency[key] > 1:
        print(key, end=" ")
        found = True
if not found:
    print('no repeating elements.')
    