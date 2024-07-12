#Read as input 5 Numbers and print the largest out of them

Input Format
5 Space Separated Numbers (both positive and negative)

Constraints
Output Format
Sample Input
2 4 7 -2 3
Sample Output
7
Explanation
In the given case 7 is largest among the given numbers.#


# Read input
numbers = list(map(int, input().split()))

# Find the largest number
largest_number = max(numbers)

# Print the largest number
print(largest_number)