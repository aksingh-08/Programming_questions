# Write a program to reverse a string.


string = input('enter a string: ')
reverse = ""
for ch in string:
    reverse = ch + reverse
print(f'reversed string: {reverse}')


# string = input('enter a string: ')
# reverse = string[::-1]
# print(f'reverse string: {reverse}')


