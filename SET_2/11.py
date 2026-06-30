# Write a program to find number of days in a given month of a given year.


month = int(input('enter the month (1-12): '))
year = int(input('enter the year: '))
if month == 2:
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print('number of days = 29')
    else:
        print('number of days = 28')
elif month in [4, 6, 9, 11]:
    print('number od days = 30')
elif month in [1, 3, 5, 7, 8, 10, 12]:
    print('number of days = 31')
# else:
    # print('invalid month')
