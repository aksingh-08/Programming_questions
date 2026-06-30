# Write a program for decimal to octal conversion.


num = int(input('enter a decimal number: '))
octal = ""
if num == 0:
    octal = "0"
else:
    while num > 0:
        remainder = num % 8
        octal = str(remainder) + octal
        num //= 8
print(f'octal = {octal}')
