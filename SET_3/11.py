# Write a program to sort a string in alphabetical order.


string = input('enter a string: ')
chars = list(string)
for i in range(len(chars)):
    for j in range(i + 1, len(chars)):
        if chars[i] > chars[j]:
            chars[i], chars[j] = chars[j], chars[i]
sorted_string = ""
for ch in chars:
    sorted_string += ch
print(f'sorted string: {sorted_string}')

