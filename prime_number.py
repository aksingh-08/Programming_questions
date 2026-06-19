# A natural number greater than 1 that has no divisors other than 1 and itself. 
# Examples: 2, 3, 5, 7, 11, 13....
# Note: 2 is the only even prime number

n = int(input("Enter the number: "))
if n <= 1:
    print(False)
else:
    prime = True
    for i in range(2, n):
        if n % i == 0:
            prime = False
            break
    print(prime)

# for i in range(2, int(n**0.5) + 1)