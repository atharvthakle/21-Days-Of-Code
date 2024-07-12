#Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Input Format
First line of input contains an integer n representing the length of array n. Next line contains n array elements.

Constraints
1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums is sorted in non-decreasing order.

Output Format
A sorted array representing squares of elements of nums array.

Sample Input
5
-4 -1 0 3 10
Sample Output
0 1 9 16 100
Explanation
After squaring, the array becomes [16,1,0,9,100]. After sorting, it becomes [0,1,9,16,100]#


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
