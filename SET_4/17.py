# Write a program to find maximum product subarray in a given array.


# arr = list(map(int, input('enter array elements: ').split()))
# n = len(arr)
# max = arr[0]
# for i in range(n):
#     product = 1
#     for j in range(i, n):
#         product *= arr[j]
#         if product >max:
#             max = product
# print(f'maximum product subarray = {max}')


# difficulty: 
# A negative x negative  = positive
# A zero resets the product



arr = list(map(int, input('enter array elements: ').split()))
maxx = arr[0]
minn = arr[0]
ans = arr[0]
for i in range(1, len(arr)):
    if arr[i] < 0:
        maxx, minn = minn, maxx
    maxx = max(arr[i], maxx * arr[i])
    minn = min(arr[i], minn * arr[i])
    ans = max(ans, maxx)
print(f'maximum product subarray = {ans}')
