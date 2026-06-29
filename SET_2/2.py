# Write a program to print Armstrong numbers between two intervals?


# start = int(input('enter the starting number: '))
# end = int(input('enter the ending number: '))
# for num in range(start, end + 1):
#     original = num
#     temp = num
#     digits = len(str(num))
#     sum = 0
#     while temp > 0:
#         digit = temp % 10
#         sum += digit ** digits
#         temp //= 10
#     if original == sum:
#         print(original, end=" ")



def is_armstrong(num):
    original = num
    digits = len(str(num))
    total = 0
    while num > 0:
        digit = num % 10
        total += digit ** digits
        num//= 10
    return original == total
start = int(input('enter the starting number: '))
end = int(input('enter the ending number: '))
print('armstrong number are:')
for num in range(start, end + 1):
    if is_armstrong(num):
        print(num, end=" ")
        