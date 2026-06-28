# Write a program to find sum of digits of a number.

num = int(input('enter a number: '))
num = abs(num)
sum = 0
while num > 0:
    digit = num % 10
    sum += digit
    num //= 10
print(f'sum of digits = {sum}')



# num = abs(int(input('enter a number: ')))
# sum = 0
# for digit in str(num):
#     sum += int(digit)
# print(f'sum of digit = {sum}')
