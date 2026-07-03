# Write a program to check if two strings are Anagram or not.


# str1 = input('enter the first string: ').lower()
# str2 = input('enter the second string: ').lower()
# if sorted(str1) == sorted(str2):
#     print('the strings are Anagrams.')
# else:
#     print('the strings are not Anagrams.')


str1 = input('enter the first string: ').lower()
str2 = input('enter the second string: ').lower()
if len(str1) != len(str2):
    print('the strings are not Anagrams.')
else:
    frequency = {}
    for ch in str1:
        frequency[ch] = frequency.get(ch, 0) + 1
    for ch in str2:
        if ch not in frequency:
            print('the strings are not Anagrams.')
            break
            frequency[ch] -= 1
            if frequency[ch] < 0:
                print('the strings are not Anagrams.')
                break
    else:
        print('the strings are Anagrams.')
        