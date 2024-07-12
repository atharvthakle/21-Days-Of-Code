#Take the following as input.

A number (N1)
A number (N2)
Write a function which returns the GCD of N1 and N2. Print the value returned.

Input Format
Two integers seperated by a new line.

Constraints
0 < N1 < 1000000000
0 < N2 < 1000000000

Output Format
Output a single integer which is the GCD of the given integers.

Sample Input
16 
24
Sample Output
8
Explanation
The largest number that divides both N1 and N2 is called the GCD of N1 and N2.#

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Input: Two integers separated by a newline
N1 = int(input().strip())
N2 = int(input().strip())

# Output the GCD of the two numbers
print(gcd(N1, N2))
