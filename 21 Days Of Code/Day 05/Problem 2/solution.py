#Take as input N, the size of array. Take N more inputs and store that in an array. Take as input “target”, a number. Write a function which prints all pairs of numbers which sum to target.

Input Format
The first line contains input N. Next N lines contains the elements of array and (N+1)th line contains target number.

Constraints
Length of the arrays should be between 1 and 1000.

Output Format
Print all the pairs of numbers which sum to target. Print each pair in increasing order.

Sample Input
5
1
3
4
2
5
5
Sample Output
1 and 4
2 and 3
Explanation
Find any pair of elements in the array which has sum equal to target element and print them.#

def find_pairs_with_sum(arr, target):
    seen = set()
    pairs = []
    
    for num in arr:
        complement = target - num
        if complement in seen:
            pairs.append((min(num, complement), max(num, complement)))
        seen.add(num)
    
    return pairs

# Reading input size of array
N = int(input().strip())

# Reading array elements
array = []
for _ in range(N):
    array.append(int(input().strip()))

# Reading the target number
target = int(input().strip())

# Finding pairs with sum equal to target
pairs = find_pairs_with_sum(array, target)

# Printing the pairs found
for pair in pairs:
    print(pair[0], "and", pair[1])
