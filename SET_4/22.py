# Write a program to find symmetric pairs in an array.


n = int(input('enter the number of pairs: '))
pairs = {}
print('enter the pairs:')
for i in range(n):
    a, b = map(int, input().split())
    if (b, a) in pairs:
        print('symmetric pair:', (b, a), "and", (a, b))
    pairs[(a, b)] = True
    