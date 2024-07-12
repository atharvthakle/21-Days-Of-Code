#Take as input N, a number. Print the pattern as according to given input and output section.

Input Format
Integer

Constraints
1 <= N <=; 100

Output Format
Pattern

Sample Input
3
Sample Output
*

**

***#


# Read the input integer N
N = int(input().strip())

# Loop from 1 to N to print the pattern
for i in range(1, N + 1):
    print('*' * i)
