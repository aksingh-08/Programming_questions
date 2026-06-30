# Write a program for octal to decimal conversion.


octal = int(input('enter an octal number: '))
decimal = 0
power = 0
while octal > 0:
    digit = octal % 10
    decimal += digit * (8 ** power)
    power += 1
    octal //= 10
print(f'decimal = {decimal}')
