# Problem 1

Mr. Block and Mayank were entrusted with the logistics of the Summer Informatics School's (SIS) new building. Their primary concern was optimizing travel time between different locations within the building. They meticulously analyzed the floor plan, which consisted of several towers, each with multiple floors.

Mr. Block, with his keen eye for detail, noticed that each tower was labeled from 1 to n, and each floor was labeled from 1 to h. Additionally, there were passages connecting adjacent towers on every floor within a certain range, from a to b. These passages were crucial for efficient movement between towers.

Mayank, being an expert in spatial organization, understood the importance of minimizing travel time between various areas of the building. He recognized that it took exactly one minute to traverse between any two adjacent floors within a tower, as well as between any two adjacent towers, provided there was a passage on that floor. They both acknowledged that leaving the building was not an option, so optimizing internal routes was paramount.

Together, they tackled the task of determining the minimum walking time between different pairs of locations within the building. For each pair (ta, fa) and (tb, fb), representing the floor and tower of the starting point and ending point respectively, they set out to calculate the shortest path, ensuring efficient movement throughout the SIS building.

## Input Format

The first line of the input contains following integers:

n : the number of towers in the building (1 ≤ n ≤ 10^8),

h : the number of floors in each tower (1 ≤ h ≤ 10^8),

a and b : the lowest and highest floor where it's possible to move between adjacent towers (1 ≤ a ≤ b ≤ h),

k : total number of queries (1 ≤ k ≤ 10^4).

Next k lines contain description of the queries. Each description consists of four integers ta, fa, tb, fb (1 ≤ ta, tb ≤ n, 1 ≤ fa, fb ≤ h). This corresponds to a query to find the minimum travel time between fa-th floor of the ta-th tower and fb-th floor of the tb-th tower.

## Constraints

1 ≤ n ≤ 10^8

1 ≤ h ≤ 10^8

1 ≤ a ≤ b ≤ h

1 ≤ k ≤ 104

## Output Format

For each query print a single integer: the minimum walking time between the locations in minutes.

## Sample Input

3 6 2 3 3

1 2 1 3

1 4 3 4

1 2 2 3

## Sample Output

1

4
2#
