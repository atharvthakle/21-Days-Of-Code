def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Read input
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

# Sort the array using bubble sort
sorted_arr = bubble_sort(arr)

# Print the sorted array
for num in sorted_arr:
    print(num)
