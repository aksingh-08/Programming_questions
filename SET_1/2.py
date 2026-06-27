# Write a program to identify if the charaacter is an alphabet or not.

# char = input("Enter a character: ")
# if len(char) == 1 and (
# 'A' <= char <= 'Z' or
# 'a' <= char <= 'z'
# ):
#     print('it is an alphabet.')
# else:
#     print('it is not an alphabet')


# char = input("Enter a character: ")
# if len(char) == 1:
#     ascii_value = ord(char)
#     if (65 <= ascii_value <= 90) or (97 <= ascii_value <= 122):
#         print('it is an alphabet.')
#     else:
#         print('it is not an alphabet.')
# else:
#     print('enter a single character.')


char = input("Enter a character: ")
if len(char) == 1:
    if char.isalpha():
        print('it is an alphabet.')
    else:
        print('is it not an alphabet.')
else:
    print('enter a valid single character.')