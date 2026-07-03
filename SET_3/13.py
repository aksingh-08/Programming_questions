# Wrire a program to remove characters in a string except alphabets.


string = input('enter a string: ')
res = ""
for ch in string:
    if ch.isalpha():
        res += ch
print(f'string after removing characters: {res}')
