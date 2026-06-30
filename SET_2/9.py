# Write a program to find the quadrants in which coordinates lie.


x = int(input('enter x-coordinates: '))
y = int(input('enter y-coordinates: '))
if x > 0 and y > 0:
    print('the pooint lies in the first quadrant.')
elif x < 0 and y > 0:
    print('the point lies in the second quadrant.')
elif x < 0 and y < 0:
    print('the point lies in the third quadrant.')
elif x > 0 and y < 0:
    print('the point lies in the fourth quadrant.')
elif x == 0 and y == 0:
    print('the point lies at the origin.')
elif x == 0:
    print('the point lies on the y-axis.')
else:
    print('the point lies on the x-axis.')
    