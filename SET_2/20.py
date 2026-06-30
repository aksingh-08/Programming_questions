# Write a program to find number of integers which has exactly 9 divisors.


n = int(input('enter the value of n: '))
count_numbers = 0
for num in range(1, n + 1):
    divisors = 0
    for i in range(1, n + 1):
        if num % i == 0:
            divisors += 1
    if divisors == 9:
        count_numbers += 1
print(f'numbers having exactly 9 divisors = {count_numbers}')
