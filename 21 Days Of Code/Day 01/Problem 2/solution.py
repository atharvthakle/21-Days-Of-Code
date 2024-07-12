#Help Lakshya Bhaiya recite tables of an input number x to the limit x*y.

Print the table of x from x*1, x * 2, x * 3… x * y.

Input Format
Take two inputs, x and y

Constraints
x<=10,000 y<=10,000

Output Format
each line contains the table of the number x

Sample Input
2 4
Sample Output
2
4
6
8#


# Read input
x, y = map(int, input().split())

# Generate and print the table
for i in range(1, y + 1):
    print(x * i)
