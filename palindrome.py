# A number is a palindrome if it reads the same forwards and backwards. Example: 121, 1221,

def is_palindrome(n):
    s = str(abs(n))
    print(s, s[::-1])
    return s == s[::-1]
num = int(input("Enter the number: "))
print(is_palindrome(num))
