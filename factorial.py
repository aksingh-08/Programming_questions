# Factorial of n (written n!) is the product 1x2x3x...xn.
# Example: 5! = 120


def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)
num = int(input("Enter the number: "))
print(f"factorial of {num} is:", fact(num))