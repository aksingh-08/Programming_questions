# Write a program for binary to octal conversion.


binary = input('enter a binary number: ')
decimal = 0
power = 0
for digit in binary[::-1]:
    decimal += int(digit) * (2 ** power)
    power += 1
octal = ""
if decimal == 0:
    octal = "0"
else:
    while decimal > 0:
        remainder = decimal % 8
        octal = str(remainder) + octal
        decimal //= 8
print(f'octal = {octal}')
