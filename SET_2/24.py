# Write a program to print diamond pattern printing using numbers.


rows = int(input('enter the number or rows: '))
for i in range(1, rows + 1):
    for j in range(rows - i):     #spaces
        print(" ", end=" ")
    for j in range(i, 0, -1):     #descending
        print(j, end=" ")
    for j in range(2, i + 1):     #ascending
        print(j, end=" ")
    print()
for i in range(rows - 1, 0, -1):
    for j in range(rows - i):
        print(" ", end=" ")
    for j in range(i, 0, -1):
        print(j, end=" ")
    for j in range(2, i + 1):
        print(j, end=" ")
    print()
    