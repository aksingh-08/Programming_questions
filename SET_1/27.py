# Write a program to identify if the number is prime number or not.


# num = int(input("Enter a number: "))
# if num <= 1:
#     print(num, "is not a Prime Number.")
# else:
#     i = 2
#     is_prime = True
#     while i <= int(num ** 0.5):
#         if num % i == 0:
#             is_prime = False
#             break
#         i += 1
#     if is_prime:
#         print(num, "is a Prime Number.")
#     else:
#         print(num, "is not a Prime Number.")



num = int(input("Enter a number: "))
if num <= 1:
    print(num, "is not a Prime Number.")
else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, "is a Prime Number.")
    else:
        print(num, "is not a Prime Number.")
