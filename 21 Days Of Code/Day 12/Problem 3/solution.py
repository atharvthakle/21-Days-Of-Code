#The Game is as follows You have given a binary array, where 1 denotes push operation and 0 denotes a pop operation in a queue. The task is to check if the possible set of operations are valid or not.
Print Valid if the set of Operations are Valid Otherwise Print Invalid.

Input Format
The First Line contains an Integer T, as the number of Test cases.
The Next Line contains an Integer N, as the Size of the Array.
The Next Line contains N Binary numbers separated by space.

Constraints
Output Format
Print Valid If the set of operations are valid Otherwise Print Invalid for each Test Case separated by a new Line.

Sample Input
2
5
1 1 0 0 1
5
1 1 0 0 0 
Sample Output
Valid
Invalid#


def is_valid_operations(operations):
    count = 0
    for op in operations:
        if op == 1:
            count += 1
        elif op == 0:
            count -= 1
        if count < 0:
            return "Invalid"
    return "Valid"

def process_test_cases(test_cases):
    results = []
    for test_case in test_cases:
        n, operations = test_case
        results.append(is_valid_operations(operations))
    return results

# Read input
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    operations = list(map(int, input().split()))
    test_cases.append((n, operations))

# Process test cases
results = process_test_cases(test_cases)

# Print results
for result in results:
    print(result)
