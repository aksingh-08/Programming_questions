# Write a program to find ASCII values of a character.

char = input("enter a character: ")
if len(char) == 1 and char.isalpha():
    # ascii_value = ord(char)
    print(f'ascii value of {char} is {ord(char)}.')
else:
    print('enter a valid character')