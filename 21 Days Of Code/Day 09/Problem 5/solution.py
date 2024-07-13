def sort_012(arr):
    low, mid, high = 0, 0, len(arr) - 1
    
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[high], arr[mid] = arr[mid], arr[high]
            high -= 1

    return arr

# Read input
n = int(input())
arr = [int(input()) for _ in range(n)]

# Sort the array
sorted_arr = sort_012(arr)

# Print the sorted array
for num in sorted_arr:
    print(num)
