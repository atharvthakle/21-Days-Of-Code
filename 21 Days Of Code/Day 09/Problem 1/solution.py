def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Read input
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

# Sort the array using selection sort
sorted_arr = selection_sort(arr)

# Print the sorted array
for num in sorted_arr:
    print(num)
