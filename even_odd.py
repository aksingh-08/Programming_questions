# A number is even if divisible by 2 (remainder 0), otherwise it is edd.

def even_odd(n):
    if n % 2 == 0:
        print("given number is even.")
    else:
        print("given number is odd")
num = int(input("Enter the number: "))
even_odd(num)
