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
