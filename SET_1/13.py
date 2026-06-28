# Write a program to find sum of N natural numbers.


# n = int(input('enter a positive integer: '))
# if n <= 0:
#     print('enter a valid positive integer.')
# else:
#     total = n * (n + 1) // 2
#     print(f'sum of first {n} natural numbers = {total}')



# n = int(input('enter a positive integer: '))
# if n <= 0:
#     print('enter a valid positive integer.')
# else:
#     total = 0
#     i = 1
#     while i <= n:
#         total += i
#         i += 1
#     print(f'sum of first {n} natural numbers = {total}')



n = int(input('enter a positive integer: '))
if n <= 0:
    print('enter a valid positive integer.')
else:
    total = 0
    for i in range(1, n + 1):
        total += i
    print(f'sum of first {n} natural numbers = {total}')
    