import math

# Function to compute the LCM of two numbers
def lcm(x, y):
    return abs(x * y) // math.gcd(x, y)

# Read input numbers
N1 = int(input().strip())
N2 = int(input().strip())

# Compute and print the LCM
print(lcm(N1, N2))
