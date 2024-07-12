#Take as input N, a number. Take N more inputs and store that in an array. Write a recursive function which inverses the array. Print the values of inverted array

Input Format
Enter a number N and take N more inputs

Constraints
None

Output Format
Display the values of the inverted array in a space separated manner

Sample Input
5
0 2 4 1 3
Sample Output
0 3 1 4 2
Explanation
Swap element with index

for eg : element 4 at index 2 becomes element 2 at index 4#


def reverse_array(arr, start, end):
    if start >= end:
        return
    # Swap elements at start and end indices
    arr[start], arr[end] = arr[end], arr[start]
    # Recursive call with updated indices
    reverse_array(arr, start + 1, end - 1)

# Read input size of array
N = int(input().strip())

# Read array elements
array = list(map(int, input().strip().split()))

# Reverse the array recursively
reverse_array(array, 0, N - 1)

# Print the reversed array
print(' '.join(map(str, array)))
