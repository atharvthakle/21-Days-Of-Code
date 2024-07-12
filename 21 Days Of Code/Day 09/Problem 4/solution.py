#You are given an unordered array consisting of consecutive integers [1, 2, 3, …, n] without any duplicates. You are allowed to swap any two elements. You need to find the minimum number of swaps required to sort the array in ascending order.

Input Format
The first line contains an integer, n, the size of the array . The second line contains n space-separated integers arr[i].

Constraints
1 <= n <= 10^5 1 <= arr[i] <= n

Output Format
Print the minimum number of swaps to sort the given array.

Sample Input
4
4 3 1 2
Sample Output
3#


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
