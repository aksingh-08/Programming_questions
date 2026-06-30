# Write a program to calculate maximum number of handshakes.


n = int(input('enter the number of peoples: '))
handshakes = n * (n - 1) // 2
print(f'number of handshakes = {handshakes}')
