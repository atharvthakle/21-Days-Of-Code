# Problem 4

You are given an input array whose each element represents the height of a line towers. The width of every tower is 1. It starts raining. Water is filled between the gap of towers if possible. You need to find how much water filled between these given towers.

Example :

*diagram*

Bars for input {3, 0, 0, 2, 0, 4}

Total trapped water = 3 + 3 + 1 + 3 = 10

## Input Format

The first line consists of number of test cases T. Each test case consists an integer N as number of towers and next line contains the N space separated integers.

#### Constraints

1 <= N <= 1000000 1 <= t <= 10 0 <= A[i] <= 10000000

## Output Format

Print how much unit of water collected among towers for each test case.

### Sample Input

2

6

3  0  0  2  0  4

12

0  1  0  2  1  0  1  3  2  1  2  1

### Sample Output

10

6
