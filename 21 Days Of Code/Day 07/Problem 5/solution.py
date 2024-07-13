def running_sum(nums):
    n = len(nums)
    result = [0] * n
    current_sum = 0
    
    for i in range(n):
        current_sum += nums[i]
        result[i] = current_sum
    
    return result

# Reading input
import sys
input = sys.stdin.read
data = input().strip().split()

n = int(data[0])
nums = list(map(int, data[1:]))

# Finding the running sum
result = running_sum(nums)

# Printing the result
print(" ".join(map(str, result)))
