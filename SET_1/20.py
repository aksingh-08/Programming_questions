# Write a program to find factors of a number.


# num = int(input('enter a number: '))
# i = 1
# print(f'Factors of {num} are:')
# while i <= num:
#     if num % i == 0:
#         print(i, end=" ")
#     i += 1


num = int(input('enter a number: '))
print(f'Factors of {num} are:')
for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")
        