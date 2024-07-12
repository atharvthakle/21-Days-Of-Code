#Take N (number of rows - only odd numbers allowed), print the following pattern (for N = 5).

      *
   *  *  *  
*  *  *  *  *  
   *  *  *
      *
Input Format
Constraints
0 < N < 10 (only odd numbers allowed)

Output Format
Sample Input
5
Sample Output
      *
    * * *
  * * * * *
    * * *
      *
Explanation
Each '*' is separated from other by a tab.#


def print_pattern(N):
    # Upper half of the pattern
    for i in range(N):
        # Calculate the number of '*' in each row
        if i <= N // 2:
            num_stars = 2 * i + 1
            num_spaces = (N // 2) - i
        else:
            num_stars = 2 * (N - 1 - i) + 1
            num_spaces = i - (N // 2)

        # Print leading spaces
        print(' ' * (2 * num_spaces), end='')

        # Print '*' with tabs in between
        for j in range(num_stars):
            if j < num_stars - 1:
                print('*', end=' ')
            else:
                print('*')

# Example usage:
N = int(input().strip())
print_pattern(N)
