# Write a program to print length of the string without using len() function.


string = input('enter a string: ')
count = 0
for ch in string:
    count += 1
print(f'length of the string = {count}')
