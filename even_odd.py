# A number is even if divisible by 2 (remainder 0), otherwise it is edd.

# def even_odd(n):
#     if n % 2 == 0:
#         print("given number is even.")
#     else:
#         print("given number is odd")
# num = int(input("Enter the number: "))
# even_odd(num)

def even_odd(n):
    return 'Even' if n % 2 == 0 else 'Odd'
num = int(input("Enter the number: "))
print(even_odd(num))
