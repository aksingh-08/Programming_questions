# Write a program to replace substring in a string.


string = input('enter the string: ')
old = input('enter the substring to replace: ')
new = input('enter the new substring: ')
res = string.replace(old, new)
print(f'updated string: {res}')
