#Take N (number of rows), print the following pattern (for N = 4).

                       1 
                     2 3 2
                   3 4 5 4 3
                 4 5 6 7 6 5 4
Input Format
Constraints
0 < N < 10

Output Format
Sample Input
4

Sample Output
            1
		2	3	2
	3	4	5	4	3
4	5	6	7	6	5	4#


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
