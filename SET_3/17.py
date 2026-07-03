# Write a program to calculate the frequency of characters in a string.


string = input('enter a string: ')
frequency = {}
for ch in string:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1
print('character frequencies:')
for ch in frequency:
    print(f'{ch} : {frequency[ch]}')
    