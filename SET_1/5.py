# Write a program to find factorial of a number.

# num = int(input("Enter a number: "))
# if num < 0:
#     print('factorial does not exist for negative numbers.')
# else:
#     fact = 1
#     for i in range(1, num+1):
#         fact *= i
#     print('factorial =', fact)


# num = int(input("Enter a number: "))
# if num < 0:
#     print('factorial does not exist for negative numbers.')
# else:
#     fact = 1
#     while num > 0:
#         fact *= num
#         num -= 1
#     print('factorial =', fact)


def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n-1)
num = int(input('Enter a number: '))
print('factorial =', fact(num))

