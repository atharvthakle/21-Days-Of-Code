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
