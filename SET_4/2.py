# Write a program to find array type. (homogeneous or Hetrogeneous)


# arr = input('enter the arrays elements: ').split()
# first_element = type(arr[0])
# same = True
# for item in arr:
#     if type(item) is not first_element:
#         same = False
#         break
# if same:
#     print('homogeneous array')
# else:
#     print('hetrogeneous array')



arr = [1, 'python', 3.14, True]
for _ in arr:
    print(f'{_} = {type(_)}')
    