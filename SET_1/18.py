# Write a program to identify if the number is perfect number or not.


# num = int(input('enter a number: '))
# sum = 0
# i = 1
# while i < num:
#     if num % i == 0:
#         sum += i
#     i += 1
# if sum == num:
#     print(f'{num} is a perfect number.')
# else:
#     print(f'{num} is not a perfect number.')




num = int(input('enter a number: '))
sum = 0
for i in range(1, num):
    if num % i == 0:
        sum += i
if sum == num:
    print(f'{num} is a perfect number.')
else:
    print(f'{num} is not a perfect number.')
