# A perfect number equals the sum of all its proper divisors (excluding itself). Example: 6 = 1+2+3.

# Step 1: Iterate from 1 to n-1
# Step 2: Accu,ulate divisors where n % i ==0
# Step 3: Compare the toal sum to n

# def is_perfect(n):
#     sum = 0 
#     if n<2:
#         return False
#     for i in range(1, n):
#         if n % i == 0:
#             sum += i
#     if (sum == n):
#         print("yes")
#     else:
#         print("no")  
# num = int(input("Enter the number: "))
# is_perfect(num)


def is_perfect(n):
    if n < 2:
        return False
    total = sum(i for i in range(1, n) if n % i == 0)
    return print(f"{total == n} {total}") 
    
n = int(input("Enter the number: "))
is_perfect(n)