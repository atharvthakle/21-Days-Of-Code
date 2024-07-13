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
