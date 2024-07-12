import math

def is_prime(N):
    if N <= 1:
        return False
    if N <= 3:
        return True
    if N % 2 == 0 or N % 3 == 0:
        return False
    i = 5
    while i * i <= N:
        if N % i == 0 or N % (i + 2) == 0:
            return False
        i += 6
    return True

# Read input number
N = int(input().strip())

# Check if the number is prime and print the result
if is_prime(N):
    print("Prime")
else:
    print("Not Prime")
