# Write a program for octal to binary conversion.


octal = input('enter an octal number: ')
decimal = 0
power = 0
for digit in octal[::-1]:
    decimal += int(digit) * (8 ** power)
    power += 1
binary = ""
if decimal == 0:
    binary = "0"
else:
    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal //= 2
print(f'binary = {binary}')
