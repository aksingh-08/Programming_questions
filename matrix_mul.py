rows1 = int(input("Enter rows od matrix 1: "))
cols1 = int(input("Enter cols of matrix 2: "))
matrix1 = []
print("Enter matrix 1:")
for i in range(rows1):
    row = []
    for j in range(cols1):
        row.append(int(input()))
    matrix1.append(row)
rows2 = int(input("Enter rows of matrix 1: "))
cols2 = int(input("Enter cols of matrix 2: "))
matrix2 = []
print("ENter matrix 2:")
for i in range(rows2):
    row = []
    for j in range(cols2):
        row.append(int(input()))
    matrix2.append(row)
if cols1 != rows2:
    print("Matric multiplication not possible!")
else:
    result = []
    for i in range(rows1):
        result_row = []
        for j in range(cols2):
            total = 0
            for k in range(cols1):
                total += matrix1[i][k] * matrix2[k][j]
            result_row.append(total)
        result.append(result_row)
    print("\nMultiplication Result:")
    for row in result:
        print(*row)
        