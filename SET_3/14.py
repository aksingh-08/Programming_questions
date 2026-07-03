# Write a program to remove spaces from a string.


string = input('enter a string: ')
res = ""
for _ in string:
    if _ != " ":
        res += _
print(f'string after removing spaces: {res}')

