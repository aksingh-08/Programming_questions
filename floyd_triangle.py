# A right-angled triangle of consecutive natural numbers. Row 1 has 1 number, row 2 has 2, and so on.
# The nth row starts at n*(n-1)/2 + 1
# The pattern can be printed using two nested loops. The outer loop controls the number of rows,
# while the inner loop prints the numbers in each row. A number 'num' is used to keep track of the current number,
# which is incremented after each print so that the numbers appear in increasing order across the triangle.

def floyd(rows):
    num = 1
    for i in range(1, rows+1):
        for j in range(1, i+1):
            print(num, end =" ")
            num += 1
        print()
floyd(6)