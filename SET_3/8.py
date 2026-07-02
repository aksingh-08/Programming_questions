# Write a program to toggle each character in a string.


string = input('enter a string: ')
res = ""
for ch in string:
    if ch.isupper():
        res += ch.lower()
    elif ch.islower():
        res += ch.upper()
    else:
        res += ch
print(f'toggled string: {res}')

