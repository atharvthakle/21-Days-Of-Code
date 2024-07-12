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


