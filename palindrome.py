# A number is a palindrome if it reads the same forwards and backwards. Example: 121, 1221,


# num = int(input("Enter the number: "))
# original_num = num
# reversed_num = 0
# while num > 0:
#     digit = num % 10
#     reversed_num = reversed_num * 10 + digit
#     num //= 10
# print(original_num == reversed_num)


def is_palindrome(n):
    s = str(abs(n))
    print(s, s[::-1])
    return s == s[::-1]
num = int(input("Enter the number: "))
print(is_palindrome(num))

