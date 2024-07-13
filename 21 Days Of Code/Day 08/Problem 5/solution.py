def is_possible(cooks, P, mid):
    total_paranthas = 0
    for cook in cooks:
        time = 0
        paranthas = 0
        while time + cook * (paranthas + 1) <= mid:
            paranthas += 1
            time += cook * paranthas
        total_paranthas += paranthas
        if total_paranthas >= P:
            return True
    return total_paranthas >= P

def min_time_to_cook_all_paranthas(P, L, ranks):
    start = 0
    end = (P * (P + 1)) // 2 * min(ranks)  # Max time
    result = end
    
    while start <= end:
        mid = (start + end) // 2
        if is_possible(ranks, P, mid):
            result = mid
            end = mid - 1
        else:
            start = mid + 1
    
    return result

# Input reading
import sys
input = sys.stdin.read
data = input().strip().split()

# First line contains P
index = 0
P = int(data[index])
index += 1

# Second line contains L (number of cooks)
L = int(data[index])
index += 1

# Next L integers denote the rank of each cook
ranks = list(map(int, data[index:index + L]))

# Calculate the minimum time required
min_time = min_time_to_cook_all_paranthas(P, L, ranks)
print(min_time)
