# A number where the sum of the factorials of its digits equals the number itself. 
# Example: 145 -> 1! + 4! + 5! = 1 + 24 + 120 = 145

def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)
def is_strong(n):
    original = n
    total = 0
    while n > 0:
        digit = n % 10
        total += fact(digit)
        n //= 10
    return total == original
n = int(input("Enter the number: "))
if is_strong(n):
    print(f"{n} is an strong number")
else:
    print(False)
