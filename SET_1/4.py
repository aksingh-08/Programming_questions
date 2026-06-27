# Write a program to find the number of digits in an integer.

# num = int(input("Enter the integer: "))
# digit = str(abs(num))
# print(f'number of digit in an given number is {len(digit)}')

# print(range(len(digit)))


num = int(input("enter an integer: "))
num = abs(num)
if num == 0:
    count = 1
else:
    count = 0
    while num > 0:
        count += 1
        num //= 10
print('number of digit:', count)
