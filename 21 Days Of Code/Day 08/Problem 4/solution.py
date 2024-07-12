#Ramu often uses public transport. The transport in the city is of two types: cabs and rickshaws. The city has n rickshaws and m cabs, the rickshaws are numbered by integers from 1 to n, the cabs are numbered by integers from 1 to m.

Public transport is not free. There are 4 types of tickets:

A ticket for one ride on some rickshaw or cab. It costs c1 ruppees;
A ticket for an unlimited number of rides on some rickshaw or on some cab. It costs c2 ruppees;
A ticket for an unlimited number of rides on all rickshaws or all cabs. It costs c3 ruppees;
A ticket for an unlimited number of rides on all rickshaws and cabs. It costs c4 ruppees.

Ramu knows for sure the number of rides he is going to make and the transport he is going to use. He asked you for help to find the minimum sum of ruppees he will have to spend on the tickets.

Input Format
Each Test case has 4 lines which are as follows:

The first line contains four integers c1, c2, c3, c4 (1 ≤ c1, c2, c3, c4 ≤ 1000) — the costs of the tickets.
The second line contains two integers n and m (1 ≤ n, m ≤ 1000) — the number of rickshaws and cabs Ramu is going to use.
The third line contains n integers ai (0 ≤ ai ≤ 1000) — the number of times Ramu is going to use the rickshaw number i.
The fourth line contains m integers bi (0 ≤ bi ≤ 1000) — the number of times Ramu is going to use the cab number i.

Constraints
1 <= T <= 1000 , where T is no of testcases
1 ≤ c1, c2, c3, c4 ≤ 1000
1 ≤ n, m ≤ 1000
0 ≤ ai , bi ≤ 1000

Output Format
For each testcase , print a single number - the minimum sum of rupees Ramu will have to spend on the tickets in a new line.

Sample Input
2
1 3 7 19
2 3
2 5
4 4 4
4 3 2 1
1 3
798
1 2 3
Sample Output
12
1
Explanation
For the first testcase ,
The total cost of rickshaws = min( min(2 * 1, 3) + min(5 * 1, 3), 7) = min(5, 7) = 5
The total cost of cabs = min( min(4 * 1, 3) + min(4 * 1, 3) + min(4 * 1, 3) , 7) = min ( 9, 7) = 7
Total final cost = min( totalCabCost + totalRickshawCost , c4) = min( 5 + 7, 19) = min ( 12, 19) = 12
We print 12.#


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
