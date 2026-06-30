# Write a program to print pyramid pattern using stars.


rows = int(input('enter the number of rows: '))
for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()

