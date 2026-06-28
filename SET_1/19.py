# Write a program to find power of a number.


# base = int(input('enter the base: '))
# exponent = int(input('enter the exponent: '))
# result = pow(base, exponent)
# print(f'Result = {result}')


# base = int(input('enter the base: '))
# exp = int(input('enter the exponent: '))
# result = base ** exp
# print(f'Result = {result}')


# base = int(input('enter the base: '))
# exp = int(input('enter the exponent: '))
# result = 1
# while exp > 0:
#     result *= base
#     exp -= 1
# print(f'Result = {result}')


base = int(input('enter the base: '))
exp = int(input('enter the exponent: '))
res = 1
for i in range(exp):
    res *= base
print(f'Result = {res}')
