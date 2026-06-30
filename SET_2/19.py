# Write a program to find number of times digit 3 occurs in each and every
# number from 0 to n.


n = int(input('enter the value of n: '))
count = 0
for i in range(n + 1):
    count += str(i).count('3')
print(f'number of times digit 3 occurs = {count}')



# n = int(input('enter the value of n: '))
# count = 0
# for i in range(n + 1):
#     num = i
#     if num == 0:
#         continue
#     while num > 0:
#         digit = num % 10
#         if digit == 3:
#             count += 1
#         num //= 10
# print(f'number of times digit 3 occurs = {count}')
