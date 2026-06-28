# Write a program to identify if the number is palindrome or not.


# num = input("Enter a number: ")
# if num == num[::-1]:
#     print(num, "is a Palindrome Number.")
# else:
#     print(num, "is not a Palindrome Number.")




num = int(input("Enter a number: "))
original_num = num
reversed_num = 0
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
if original_num == reversed_num:
    print(original_num, "is a Palindrome Number.")
else:
    print(original_num, "is not a Palindrome Number.")




