# Write a program to find fibonacci series upto n.

# n = int(input('ENter the number of terms: '))
# first = 0
# second = 1
# if n <= 0:
#     print('enter a positive number.')
# elif n == 1:
#     print(first)
# else:
#     print('fibonacci series: ')
#     for i in range(n):
#         print(first, end=" ")
#         next_term = first + second
#         first = second
#         second = next_term



# n = int(input('Enter the number of terms: '))
# first = 0
# second = 1
# count = 0
# while count < n:
#     print(first, end=" ")
#     next_term = first + second
#     first = second
#     second = next_term
#     count += 1



def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
n = int(input('enter the number of terms: '))
for i in range(n):
    print(fib(i), end=" ")
    