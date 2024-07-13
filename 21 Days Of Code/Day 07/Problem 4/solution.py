def sorted_squares(nums):
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    position = n - 1
    
    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result[position] = nums[left] ** 2
            left += 1
        else:
            result[position] = nums[right] ** 2
            right -= 1
        position -= 1
    
    return result

# Reading input
import sys
input = sys.stdin.read
data = input().strip().split()

n = int(data[0])
nums = list(map(int, data[1:]))

# Finding the sorted squares
result = sorted_squares(nums)

# Printing the result
print(" ".join(map(str, result)))
