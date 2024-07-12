def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Input: Two integers separated by a newline
N1 = int(input().strip())
N2 = int(input().strip())

# Output the GCD of the two numbers
print(gcd(N1, N2))
