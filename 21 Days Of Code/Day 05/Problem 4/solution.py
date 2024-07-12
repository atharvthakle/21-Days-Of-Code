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
