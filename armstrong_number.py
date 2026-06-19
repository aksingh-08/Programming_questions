# A number where the sum of each digit raised to the power of the number of digits equals the number itself.
# Example: 1^3 + 5^3 + 3^3 = 153

# n = 153
# t = n
# p = len(str(n))
# s = 0

# while t > 0:
#     d = t % 10
#     s += d ** p
#     t //= 10

# if s == n:
#     print("Armstrong")
# else:
#     print("NO")


def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    return sum(int(d) ** power for d in digits) == n
num = int(input("Enter the number: "))
print(num, is_armstrong(num))
