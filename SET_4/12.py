# Write a program to find minimum scalar product of two vectors.


# n = int(input('enter the number of elements: '))
# vec1 = list(map(int, input('enter first vector: ').split()))
# vec2 = list(map(int, input("enter second vector: ").split()))
# vec1.sort()
# vec2.sort(reverse=True)
# min = 0
# for _ in range(n):
#     min += vec1[_] * vec2[_]
# print(f'minimum scalar product = {min}')



n = int(input('enter the number of elements: '))
vec1 = list(map(int, input('enter first vector: ').split()))
vec2 = list(map(int, input('enter second vector: ').split()))
for i in range(n):
    for j in range(i+1, n):
        if vec1[i] > vec1[j]:
            vec1[i], vec1[j] = vec1[j], vec1[i]
for i in range(n):
    for j in range(i+1, n):
        if vec2[i] < vec2[j]:
            vec2[i], vec2[j] = vec2[j], vec2[i]
min = 0
for i in range(n):
    min += vec1[i] * vec2[i]
print('minimum scalar product =', min)
