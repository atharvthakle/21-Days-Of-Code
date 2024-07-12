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
