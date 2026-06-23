# Reverse the digits of a given integer. Example: 12345 -> 54321

# num = int(input("Enter the number: "))
# rev = 0
# reverse_string = str(num)[::-1]
# rev = int(reverse_string)
# print(rev)

def reverse(n):
    rev = 0
    while n != 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10
    print(rev)
num = int(input("Enter the number: "))
reverse(num)