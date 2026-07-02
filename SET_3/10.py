# Write a program to check if string is a palindrome or not.


string = input('enter a string: ')
reverse = ""
for _ in string:
    reverse = _ + reverse
if string == reverse:
    print('the string is a palindrome.')
else:
    print('the string is not a palindrome.')

