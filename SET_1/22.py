# Write a program to find GCD of two numbers.


# num1 = int(input('Enter the first number: '))
# num2 = int(input('Enter the second number: '))
# gcd = 1
# for i in range(1, min(num1, num2) + 1):
#     if num1 % i == 0 and num2 % i == 0:
#         gcd = i
# print(f'GCD = {gcd}')



num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
while num2 != 0:
    num1, num2 = num2, num1 % num2
print(f'GCD = {num1}')
