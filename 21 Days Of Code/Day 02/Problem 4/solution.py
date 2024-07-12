#Take the following as input.
A number
A digit
Write a function that returns the number of times digit is found in the number. Print the value returned.

Input Format
Integer (A number) Integer (A digit)

Constraints
0 <= N <= 1000000000 0 <= Digit <= 9

Output Format
Integer (count of times digit occurs in the number)

Sample Input
5433231 
3
Sample Output
3
Explanation
The digit can be from 0 to 9. Assume decimal numbers.In the given case digit 3 is occurring 3 times in the given number.#

def count_digit_occurrences(number, digit):
    # Convert number to string to iterate over its digits
    number_str = str(number)
    digit_str = str(digit)
    
    # Count occurrences of the digit in the number
    return number_str.count(digit_str)

# Read input
number = int(input().strip())
digit = int(input().strip())

# Get the count of occurrences of the digit in the number
result = count_digit_occurrences(number, digit)

# Print the result
print(result)
