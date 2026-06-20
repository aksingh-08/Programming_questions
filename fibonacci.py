# Each number is the sum of the two preceding ones: 0, 1, 1, 2, 3, 5, 8, 13, 21...

num = int(input("Enter the number: "))
a, b = 0, 1
for _ in range(num):
    print(a, end=" ")
    a, b = b, a+b
    