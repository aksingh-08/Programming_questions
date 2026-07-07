# Write a program to remove duplicate elements in an array.


arr = list(map(int, input('enter array elements: ').split()))
res = []
for _ in arr:
    if _ not in res:
        res.append(_)
print(res)
