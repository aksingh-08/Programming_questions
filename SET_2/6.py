# Write a program to print pyramid pattern using numbers.


rows = int(input('enter the number of rows: '))
for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print(i, end="")
    print()
    