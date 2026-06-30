# Write a program to find permutations in which n people can occupy r sets in a classroom.


n = int(input('enter the number of people (n): '))
r = int(input('enter the number of seats (r): '))
if r > n or n < 0 or r < 0:
    print('invalid input')
else:
    n_fact = 1
    for i in range(1, n + 1):
        n_fact *= i
    nr_fact = 1
    for i in range(1, n - r + 1):
        nr_fact *= i
    permutation = n_fact // nr_fact
    print(f'number of permutations = {permutation}')
    