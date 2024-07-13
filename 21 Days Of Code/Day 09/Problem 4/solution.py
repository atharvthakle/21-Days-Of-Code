def minimum_swaps(arr):
    n = len(arr)
    visited = [False] * n
    swaps = 0
    
    for i in range(n):
        if visited[i] or arr[i] == i + 1:
            continue
        
        cycle_length = 0
        x = i
        
        while not visited[x]:
            visited[x] = True
            x = arr[x] - 1
            cycle_length += 1
        
        if cycle_length > 0:
            swaps += cycle_length - 1
            
    return swaps

# Read input
n = int(input())
arr = list(map(int, input().split()))

# Calculate and print the minimum number of swaps
print(minimum_swaps(arr))
