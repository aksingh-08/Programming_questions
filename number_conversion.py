# Number System Conversions (Decimal <-> Binary, Octal, Hex)
# Convert numbers between decimal (base 10), binary (base 2), octal (base 8), and hexadecimal (base 16).

n = 255
print(f'Decimal:      {n}')
print(f'Binary:       {bin(n)}    ->    {bin(n) [2:]}')
print(f'Octal:        {oct(n)}    ->    {oct(n) [2:]}')
print(f'Hex:          {hex(n)}    ->    {hex(n) [2:].upper()}')

print(f'Binary (fmt):    {n:08b}')
print(f'Octal  (fmt):    {n:o}')
print(f'Hex    (fmt):    {n:X}')