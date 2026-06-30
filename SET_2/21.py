# Write a program to find roots of a quadratic equation.


import math
a = float(input('enter coefficient a: '))
b = float(input('enter coefficient b: '))
c = float(input('enter coefficient c: '))
if a == 0:
    print('not a quadratic equation.')
else:
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        print(f'root 1 = {root1}')
        print(f'root 2 = {root2}')
    elif discriminant == 0:
        root = -b / (2*a)
        print('both roots are equal.')
        print(f'root = {root}')
    else:
        print('the roots are imaginary (complex).')
        