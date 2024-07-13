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
