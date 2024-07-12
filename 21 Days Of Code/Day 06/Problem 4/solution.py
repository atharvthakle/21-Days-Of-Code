#You are given an input array whose each element represents the height of a line towers. The width of every tower is 1. It starts raining. Water is filled between the gap of towers if possible. You need to find how much water filled between these given towers.

Example :
*diagram*
Bars for input {3, 0, 0, 2, 0, 4}
Total trapped water = 3 + 3 + 1 + 3 = 10

Input Format
The first line consists of number of test cases T. Each test case consists an integer N as number of towers and next line contains the N space separated integers.

Constraints
1 <= N <= 1000000 1 <= t <= 10 0 <= A[i] <= 10000000

Output Format
Print how much unit of water collected among towers for each test case.

Sample Input
2
6
3  0  0  2  0  4
12
0  1  0  2  1  0  1  3  2  1  2  1

Sample Output
10
6#


def trapped_water(towers):
    n = len(towers)
    if n <= 2:
        return 0
    
    left_max = [0] * n
    right_max = [0] * n
    
    left_max[0] = towers[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], towers[i])
    
    right_max[n-1] = towers[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], towers[i])
    
    water = 0
    left, right = 0, n - 1
    while left <= right:
        current_water_level = min(left_max[left], right_max[right])
        if towers[left] < towers[right]:
            water += max(0, current_water_level - towers[left])
            left += 1
        else:
            water += max(0, current_water_level - towers[right])
            right -= 1
    
    return water

# Reading input
import sys
input = sys.stdin.read().split('\n')

T = int(input[0])
index = 1
results = []
for _ in range(T):
    N = int(input[index])
    towers = list(map(int, input[index + 1].split()))
    index += 2
    
    results.append(trapped_water(towers))

for result in results:
    print(result)
