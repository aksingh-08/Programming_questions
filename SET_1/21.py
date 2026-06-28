# Write a program to add two fractions.


num1 = int(input('Enter the numerator of the first fraction: '))
den1 = int(input('Enter the denominator of the first fraction: '))
num2 = int(input('Enter the numerator of the second fraction: '))
den2 = int(input('Enter the denominator of the second fraction: '))
numerator = num1 * den2 + num2 * den1
denominator = den1 * den2
print(f'Sum = {numerator} / {denominator}')
