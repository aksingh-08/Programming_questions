# Pascal's triangle is a pattern of the triangle which is based on nCr. [ n! / (n - r)! r! ]
#       1
#      1 1
#     1 2 1
#    1 3 3 1
#   1 4 6 4 1

n=5
for i in range(1, n+1):
    for j in range(0, n-i+1):
        print(' ', end='')
    C = 1
    for j in range(1, i+1):
        print(' ', C, sep='', end='')
        C = C*(i-j)//j
    print()


# n=6
# for i in range(n):
#     print(' '*(n-i), end='')
#     coef=1
#     for j in range(0, i+1):
#         print(coef, end=' ')
#         coef=coef*(i-j)//(j+1)
#     print()
