# Write a program to identify id the year is leap year or not.


# year = int(input("Enter a year: "))
# if year % 400 == 0:
#     print(year, "is a Leap Year.")
# elif year % 100 == 0:
#     print(year, "is not a Leap Year.")
# elif year % 4 == 0:
#     print(year, "is a Leap Year.")
# else:
#     print(year, "is not a Leap Year.")



year = int(input("Enter a year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a Leap Year.")
else:
    print(year, "is not a Leap Year.")