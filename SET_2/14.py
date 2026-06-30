# Write a program for decimal to binary conversion.


num = int(input('enter a decimal number: '))
original = num
binary = ""
if num == 0:
    binary = "0"
else:
    while num > 0:
        remainder = num % 2
        binary = str(remainder) + binary
        num //= 2
print(f'binary = {binary}')
