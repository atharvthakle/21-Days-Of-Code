#Take the following as input.

A number (N1)
A number (N2)
Write a function which returns the LCM of N1 and N2. Print the value returned.

Input Format
Constraints
0 < N1 < 1000000000
0 < N2 < 1000000000

Output Format
Sample Input
4 
6
Sample Output
12
Explanation
The smallest number that is divisible by both N1 and N2 is called the LCM of N1 and N2.#

import math

# Function to compute the LCM of two numbers
def lcm(x, y):
    return abs(x * y) // math.gcd(x, y)

# Read input numbers
N1 = int(input().strip())
N2 = int(input().strip())

# Compute and print the LCM
print(lcm(N1, N2))
