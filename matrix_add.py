rows = int(input("Enter rows element: "))
col = int(input("Enter columns element: "))
matrix1 = []
matrix2 = []
add_res = []
print("Entries will be done row-wise(matrix 1) =>")
# first matrix 
for i in range(rows):
    mat1_row = []
    for j in range(col):
        mat1_row.append(int(input()))
    matrix1.append(mat1_row)
print("Entries will be done row-wise(matrix 2) =>")
# second matrix
for i in range(rows):
    mat2_row = []
    for j in range(col):
        mat2_row.append(int(input()))
    matrix2.append(mat2_row)
# addition
for i in range(rows):
    res_row = []
    for j in range(col):
        res_row.append(matrix1[i][j] + matrix2[i][j])
    add_res.append(res_row)
# print result matrix
print("\nAddition of matrix is:")
for i in range(rows):
    for j in range(col):
        print(add_res[i][j], end=" ")
    print()
