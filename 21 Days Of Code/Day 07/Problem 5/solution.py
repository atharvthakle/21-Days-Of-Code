#Given an array nums of length n. We define a running sum of an array as for every index runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of array for each i (0 <= i < n).

Input Format
First line contains an integer n representing number of elements. Next line contains n integers denoting array elements.

Constraints
1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6

Output Format
An integer representing running sum array of the given array

Sample Input
4
1 2 3 4
Sample Output
1 3 6 10
Explanation
Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].#


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
