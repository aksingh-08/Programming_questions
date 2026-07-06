# Write a program to find longest palindrome in an array.


arr = input('enter the array elements: ').split()
longest = ""
for word in arr:
    if word == word[::-1]:
        if len(word) > len(longest):
            longest = word
if longest:
    print(f'longest palindrome: {longest}')
else:
    print('no palindrome found.')
    