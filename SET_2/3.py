# Write a program to express a number as a sum of two prime numbers.

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
num = int(input('enter a number: '))
found = False
for i in range(2, num):
    if is_prime(i) and is_prime(num - i):
        print(f'{num} = {i} + {num - i}')
        found = True
if not found:
    print('can\'t be expressed as the sum of two prime numbers.')
    