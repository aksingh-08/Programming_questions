# Write a program to find greatest of two numbers.


num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
if num1 > num2:
    print(f'{num1} is the grestest number.')
elif num2 > num1:
    print(f'{num2} is the greatest number.')
else:
    print('Both numbers are equal.')
    