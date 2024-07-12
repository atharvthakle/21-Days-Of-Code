import sys

# Read all input at once
input_data = sys.stdin.read()

# Split the input into lines
lines = input_data.splitlines()

# Initialize index and result list
i = 0
results = []

while i < len(lines):
    # Skip any lines that start with "Input Case"
    if lines[i].startswith("Input Case"):
        i += 1
        continue
    
    # Read the number of stewards
    n = int(lines[i].strip())
    i += 1
    
    # Read the strengths of the stewards
    strengths = list(map(int, lines[i].strip().split()))
    i += 1
    
    # Calculate the number of stewards Mr. Blocks will support
    min_strength = min(strengths)
    max_strength = max(strengths)
    count = 0
    
    for strength in strengths:
        if min_strength < strength < max_strength:
            count += 1
    
    # Append the result for this test case
    results.append(count)

# Print the results for each test case
for result in results:
    print(result)
