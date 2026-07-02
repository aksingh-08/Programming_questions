# Write a program to remove vowels from a string.


string = input('enter a string: ')
res = ""
for _ in string:
    if _ not in "aeiouAEIOU":
        res += _
print(f'string after removing vowels: {res}')

