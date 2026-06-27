# Write a program to identify if the character is a vowel or consonant.

# char = input("Enter a character: ")
# if char in "aeiouAEIOU":
#     print("It is a vowel.")
# else:
#     print("It is a consonant.")


char = input("Enter a character: ")
if len(char) != 1 or not char.isalpha():
    print("Please enter a single alphabet.")
elif char.lower() in 'aeiou':
    print('it is a vowel.')
else:
    print('it is a consonant')