# Write a program to find LCM of two numbers.

# num1 = int(input('enter the first number: '))
# num2 = int(input('enter the second number: '))
# lcm = max(num1, num2)
# while True:
#     if lcm % num1 == 0 and lcm % num2 == 0:
#         print(f'LCM = {lcm}')
#         break
#     lcm += 1



num1 = int(input('enter the first number: '))
num2 = int(input('enter the second number: '))
a = num1
b = num2
while b != 0:
    a, b = b, a % b
gcd = a
lcm = (num1 * num2) // gcd
print(f'LCM = {lcm}')
