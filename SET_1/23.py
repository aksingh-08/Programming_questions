# Write a program to identify if the number is Armstrong number or not.


num = int(input('Enter a number: '))
original = num
total_digit = len(str(num))
sum_power = 0
while num > 0:
    digit = num % 10
    sum_power += digit ** total_digit
    num //= 10
if original == sum_power:
    print(f'{original} is an Armstrong number.')
else:
    print(f'{original} is not an Armstrong number.')
    