#Given an array, print the Next Greater Element (NGE) for every element. The Next Greater Element for an element x is the first greater element on the right side of x in array. Elements for which no greater element exist, consider next greater element as -1.

Input Format
First line of the input contains a single integer T denoting the number of testcases. First line of each testcase contains an integer N denoting the size of array. Second line of each testcase contains N space seperated integers denoting the array.

Constraints
1 <= T <= 50 1 <= N <= 10^5

Output Format
For each index, print its array element and its next greater element seperated by a comma in a new line.

Sample Input
2
4
11 13 21 3
5
11 9 13 21 3
Sample Output
11,13
13,21
21,-1
3,-1
11,13
9,13
13,21
21,-1
3,-1
Explanation
For the first testcase , the next greater element for 11 is 13 , for 13 its 21 and 21 being the largest element of the array does not have a next greater element. Hence we print -1 for 21. 3 is the last element of the array and does not have any greater element on its right. Hence we print -1 for it as well.#


def printNGE(arr):
    n = len(arr)
    nge = [-1] * n
    stack = []

    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            nge[stack.pop()] = arr[i]
        stack.append(i)

    for i in range(n):
        print(f"{arr[i]},{nge[i]}")

# Read number of test cases
T = int(input())

for _ in range(T):
    # Read the size of the array
    N = int(input())
    # Read the array elements
    arr = list(map(int, input().split()))
    # Print the Next Greater Element for each element in the array
    printNGE(arr)
