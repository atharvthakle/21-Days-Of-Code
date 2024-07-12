# Read input
x, y = map(int, input().split())

# Generate and print the table
for i in range(1, y + 1):
    print(x * i)
