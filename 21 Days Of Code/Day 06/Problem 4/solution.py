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
