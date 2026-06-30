# Write a program to print Pascal triangle.


rows = int(input('enter the number of rows: '))
for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end=" ")
    value = 1
    for j in range(i + 1):
        print(value, end="   ")
        value = value * (i - j) // (j + 1)
    print()
    