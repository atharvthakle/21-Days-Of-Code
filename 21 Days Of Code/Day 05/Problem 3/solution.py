def product_except_self(arr):
    n = len(arr)
    
    # Arrays to store left and right products
    left_product = [1] * n
    right_product = [1] * n
    output = [0] * n
    
    # Compute left products
    for i in range(1, n):
        left_product[i] = left_product[i-1] * arr[i-1]
    
    # Compute right products
    for i in range(n-2, -1, -1):
        right_product[i] = right_product[i+1] * arr[i+1]
    
    # Compute output array
    for i in range(n):
        output[i] = left_product[i] * right_product[i]
    
    return output

# Reading input size of array
N = int(input().strip())

# Reading array elements
array = list(map(int, input().strip().split()))

# Calculate the output array
result = product_except_self(array)

# Print the result array
print(' '.join(map(str, result)))
