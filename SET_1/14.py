# Write a program to find sum of numbers in a given range.


# start = int(input('enter the starting number: '))
# end = int(input('enter the ending number: '))
# total = (start + end) * (end - start + 1) // 2
# print(f'sum = {total}')



# start = int(input('enter the starting number: '))
# end = int(input('enter the ending number: '))
# total = 0
# while start <= end:
#     total += start
#     start += 1
# print(f'sum = {total}')



start = int(input('enter the starting number: '))
end = int(input('enter the ending number: '))
total = 0
for i in range(start, end + 1):
    total += i
print(f'sum = {total}')
