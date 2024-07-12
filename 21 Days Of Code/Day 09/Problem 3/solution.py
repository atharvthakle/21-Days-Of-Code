#Sort just 0 and 1

Input Format
A line containing N number of 0s and 1s Next line follows a long sequence of 0 and 1 seperated by space

Constraints
N will not exceed 10^7

Output Format
Sorted Sequence

Sample Input
7
1 0 0 1 1 0 1
Sample Output
0 0 0 1 1 1 1#


def sort_zeros_and_ones(arr):
    count_zeros = arr.count(0)
    count_ones = len(arr) - count_zeros
    sorted_arr = [0] * count_zeros + [1] * count_ones
    return sorted_arr

# Read input
n = int(input())
arr = list(map(int, input().split()))

# Sort the array of 0s and 1s
sorted_arr = sort_zeros_and_ones(arr)

# Print the sorted array
print(' '.join(map(str, sorted_arr)))
