#Take N (number of rows), print the following pattern (for N = 5)
1
2 2
3 0 3
4 0 0 4
5 0 0 0 5

Input Format
There will be an integer in input.

Constraints
0 < N < 100

Output Format
Print the pattern.

Sample Input
5
Sample Output
1  
2	2  
3	0	3    
4	0	0	4  
5	0	0	0	5
Explanation
Each number is separated from other by a tab.If row number is n (>1), total character is n. First and last character is n and rest are 0.#


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
