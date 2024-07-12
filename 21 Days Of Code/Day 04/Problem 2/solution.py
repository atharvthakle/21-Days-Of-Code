def print_pattern(N):
    for i in range(1, N + 1):
        # Print numbers and zeros in each row
        for j in range(1, i + 1):
            if j == 1 or j == i:
                print(i, end=' ')
            else:
                print('0', end=' ')
        print()  # Move to the next line after each row

# Example usage:
N = int(input().strip())
print_pattern(N)
