# Write a program to print non-repeating characters in a string.


string = input('enter a string: ')
frequency = {}
for ch in string:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1
print('non-repeating characters:')
for ch in string:
    if frequency[ch] == 1:
        print(ch, end=" ")
