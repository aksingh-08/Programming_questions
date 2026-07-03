# Write a program to count the sum of numbers in a string.


string = input('enter a string: ')
sum = 0
for _ in string:
    if _.isdigit():
        sum += int(_)
print(f'sum of digit = {sum}')

