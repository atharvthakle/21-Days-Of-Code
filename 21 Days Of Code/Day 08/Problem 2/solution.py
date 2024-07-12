#Given K painters to paint N boards where each painter takes 1 unit of time to paint 1 unit of boards i.e. if the length of a particular board is 5, it will take 5 units of time to paint the board. Compute the minimum amount of time to paint all the boards.

Note that:

Every painter can paint only contiguous segments of boards.
A board can only be painted by 1 painter at maximum.
Input Format
First line contains K which is the number of painters. Second line contains N which indicates the number of boards. Third line contains N space separated integers representing the length of each board.

Constraints
1 <= K <= 10
1 <= N <= 10
1<= Length of each Board <= 10^8

Output Format
Output the minimum time required to paint the board.

Sample Input
2
2
1 10
Sample Output
10#


def is_possible(boards, n, k, max_time):
    total_time = 0
    painters = 1
    
    for i in range(n):
        total_time += boards[i]
        
        if total_time > max_time:
            painters += 1
            total_time = boards[i]
            
            if painters > k:
                return False
                
    return True

def find_min_time(boards, n, k):
    low = max(boards)
    high = sum(boards)
    result = high
    
    while low <= high:
        mid = (low + high) // 2
        
        if is_possible(boards, n, k, mid):
            result = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return result

# Reading input
import sys
input = sys.stdin.read
data = input().strip().split()
k = int(data[0])
n = int(data[1])
boards = list(map(int, data[2:]))

# Finding the minimum time required
result = find_min_time(boards, n, k)

# Printing the result
print(result)
