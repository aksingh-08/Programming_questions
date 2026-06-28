# Write a program to identify if the number is strong number or not.


num = int(input('enter a number: '))
original = num
sum = 0
while num > 0:
    digit = num % 10
    factorial = 1
    for i in range(1, digit + 1):
        factorial *= i
    sum += factorial
    num //= 10
if original == sum:
    print(f'{original} is a strong number.')
else:
    print(f'{original} is not a strong number.')
