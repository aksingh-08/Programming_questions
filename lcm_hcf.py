# LCM and GCF (HCF / GCD)
# GCF (Greatest Common Factor) / GCD (Greatest Common Divisor): largest number that divides both inputs.
# LCM (Least Common Multiple): smallest number divisible by both. 
# Relationship: LCM(a,b) = a*b / GCD(a,b)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def lcm(a, b):
    return abs(a * b) // gcd(a, b)
print(f'GCD(48, 18) = {gcd(48, 18)}')
print(f'LCM(4, 6) = {lcm(4, 6)}')
