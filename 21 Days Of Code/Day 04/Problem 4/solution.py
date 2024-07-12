def print_pattern(N):
    # Outer loop for rows
    for i in range(1, N + 1):
        # Print leading spaces
        print(' ' * (2 * (N - i)), end='')

        # Print increasing numbers
        for j in range(i, 2 * i):
            print(j, end=' ')

        # Print decreasing numbers
        for j in range(2 * i - 2, i - 1, -1):
            print(j, end=' ')

        # Move to the next line after each row
        print()

# Example usage:
N = int(input().strip())
print_pattern(N)
