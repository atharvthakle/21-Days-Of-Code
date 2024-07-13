def calculate_minimum_cost(c1, c2, c3, c4, n, m, rickshaw_rides, cab_rides):
    # Calculate the minimum cost for rickshaw rides
    total_rickshaw_cost = 0
    for rides in rickshaw_rides:
        total_rickshaw_cost += min(rides * c1, c2)
    total_rickshaw_cost = min(total_rickshaw_cost, c3)
    
    # Calculate the minimum cost for cab rides
    total_cab_cost = 0
    for rides in cab_rides:
        total_cab_cost += min(rides * c1, c2)
    total_cab_cost = min(total_cab_cost, c3)
    
    # Calculate the final minimum cost
    final_cost = min(total_rickshaw_cost + total_cab_cost, c4)
    
    return final_cost

# Read input
import sys
input = sys.stdin.read
data = input().strip().split()
index = 0
T = int(data[index])
index += 1

results = []
for _ in range(T):
    c1 = int(data[index])
    c2 = int(data[index+1])
    c3 = int(data[index+2])
    c4 = int(data[index+3])
    index += 4
    
    n = int(data[index])
    m = int(data[index+1])
    index += 2
    
    rickshaw_rides = list(map(int, data[index:index+n]))
    index += n
    cab_rides = list(map(int, data[index:index+m]))
    index += m
    
    result = calculate_minimum_cost(c1, c2, c3, c4, n, m, rickshaw_rides, cab_rides)
    results.append(result)

# Print results for each test case
for result in results:
    print(result)
