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
