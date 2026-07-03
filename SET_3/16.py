# Write a program to capitalize the first and last letter of each word of a string.


string = input('enter a string: ')
words = string.split()
res = ""
for word in words:
    if len(word) == 1:
        res += word.upper() + " "
    else:
        new_word = word[0].upper() + word[1:-1] + word[-1].upper()
        res += new_word + " "
print(f'results: {res.strip()}')

