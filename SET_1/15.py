# Write a program to reverse a given number.

num = int(input('enter a number: '))
original = num
num = abs(num)
reversed = 0
while num > 0:
    digit = num % 10
    reversed = reversed * 10 + digit
    num //= 10
if original < 0:
    reversed = -reversed
print(f'reversed number = {reversed}')
