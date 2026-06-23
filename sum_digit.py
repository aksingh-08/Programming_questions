# Find the sum of all digits of a number. Example: 12345 -> 1+2+3+4+5 = 15

n = int(input("Enter the number: "))
sum = 0
while n > 0:
    # sum = sum + n % 10
    sum += n % 10
    n //= 10
print(sum)
