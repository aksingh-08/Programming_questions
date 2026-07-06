# Write a program to find frequency of each element of an array.


arr = list(map(int, input('enter array elements: ').split()))
freq = {}
for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
for key in freq:
    print(f'{key} : {freq[key]}')
    