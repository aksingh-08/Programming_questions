# Write a program to find number of even and odd elements in an array.


arr = list(map(int, input('enter array elements: ').split()))
even = 0
odd = 0
for _ in arr:
    if _ % 2 == 0:
        even += 1
    else:
        odd += 1
print(f'number of even elements: {even}')
print(f'number of odd elements: {odd}')




# arr = list(map(int, input('enter array elements: ').split()))
# even = sum(1 for _ in arr if _ % 2 == 0)
# odd = sum(1 for _ in arr if _ % 2 != 0)
# print(f'number of even elements: {even}')
# print(f'number of odd elements: {odd}')
