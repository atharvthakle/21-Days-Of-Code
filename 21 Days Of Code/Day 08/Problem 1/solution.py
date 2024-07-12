#Farmer John has built a new long barn, with N (2 <= N <= 100,000) stalls. The stalls are located along a straight line at positions x1,…,xN (0 <= xi <= 1,000,000,000).

His C (2 <= C <= N) cows don't like this barn layout and become aggressive towards each other once put into a stall. To prevent the cows from hurting each other, FJ wants to assign the cows to the stalls, such that the minimum distance between any two of them is as large as possible. What is the largest minimum distance?

Input Format
First line contains N and C, separated by a single space, representing the total number of stalls and number of cows respectively. The next line contains N integers containing the indexes of stalls.

Constraints
2 <= N <= 100,000
0 <= xi <= 1,000,000,000
2 <= C <= N

Output Format
Print one integer: the largest minimum distance.

Sample Input
5 3
1 2 8 4 9
Sample Output
3#


def is_possible(stalls, n, c, min_dist):
    count = 1  # Place the first cow in the first stall
    last_position = stalls[0]

    for i in range(1, n):
        if stalls[i] - last_position >= min_dist:
            count += 1
            last_position = stalls[i]
            if count == c:
                return True
    return False

def largest_min_distance(stalls, n, c):
    stalls.sort()
    low = 1  # The smallest possible minimum distance
    high = stalls[-1] - stalls[0]  # The largest possible minimum distance

    best = 0
    while low <= high:
        mid = (low + high) // 2
        if is_possible(stalls, n, c, mid):
            best = mid  # Update best result
            low = mid + 1  # Try for a larger distance
        else:
            high = mid - 1  # Try for a smaller distance

    return best

# Reading input
import sys
input = sys.stdin.read
data = input().strip().split()
n = int(data[0])
c = int(data[1])
stalls = list(map(int, data[2:]))

# Finding the largest minimum distance
result = largest_min_distance(stalls, n, c)

# Printing the result
print(result)
