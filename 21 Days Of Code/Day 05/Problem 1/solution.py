#Take as input N, the size of an array. Take N more inputs and store that in an array. Take another number’s input as M. Write a function which returns the index on which M is found in an array, in case M is not found -1 is returned. Print the value returned.

It reads a number N.
2.Take Another N numbers as an input and store them in an Array.
Take another number M as an input.
If M is found in the Array the index of M is returned else -1 is returned and print the value returned.
Input Format
Constraints
N cannot be Negative. Range of Numbers can be between -1000000000 to 1000000000. M can be between -1000000000 to 1000000000.

Output Format
Sample Input
5
2
4
6
9
17
17
Sample Output
4
Explanation
Given array = {2, 4, 6, 9, 17}. Target number = 17. Index = 4.#


def find_index_in_array(arr, target):
    # Iterate through the array
    for i in range(len(arr)):
        # Check if current element is equal to target
        if arr[i] == target:
            return i  # Return index if found
    
    # Return -1 if target is not found in the array
    return -1

# Reading input size of array
N = int(input().strip())

# Reading array elements
array = []
for _ in range(N):
    array.append(int(input().strip()))

# Reading the target number M
M = int(input().strip())

# Finding index of M in the array
index = find_index_in_array(array, M)

# Printing the index found or -1 if not found
print(index)


