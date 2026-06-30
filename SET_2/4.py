# Write a program to replace all 0's with 1 in a given integer.


num = int(input('enter a number: '))
if num == 0:
    print('result = 1')
else:
    result = 0
    place = 1
    while num > 0:
        digit = num % 10
        if digit == 0:
            digit = 1
        result = result + digit * place
        place *= 10
        num //= 10
    print(f'result = {result}')
