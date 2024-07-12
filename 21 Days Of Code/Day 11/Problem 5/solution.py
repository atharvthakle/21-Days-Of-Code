#Find the largest rectangular area possible in a given histogram where the largest rectangle can be made of a number of contiguous bars.


Input Format
First line contains a single integer N, denoting the number of bars in th histogram.
Next line contains N integers, ith of which, denotes the height of ith bar in the histogram.

Constraints
1<=N<=10^6
Height of each bar in histogram <= 10^10

Output Format
Output a single integer denoting the area of the required rectangle.

Sample Input
5
1 2 3 4 5
Sample Output
9
Explanation
The largest rectangle can be obtained of breadth=3 and length=3. Its starting index is 2 and ending index is 4 and it has a height of 3. Hence area = 3*3 = 9#


def largestRectangleArea(heights):
    stack = []
    max_area = 0
    index = 0
    
    while index < len(heights):
        # If the stack is empty or the current bar is higher than the bar at stack top
        if not stack or heights[stack[-1]] <= heights[index]:
            stack.append(index)
            index += 1
        else:
            # Pop the top
            top_of_stack = stack.pop()
            # Calculate the area with heights[top_of_stack] as the smallest (or minimum height) bar 'h'
            area = (heights[top_of_stack] * 
                   ((index - stack[-1] - 1) if stack else index))
            # Update max_area, if needed
            max_area = max(max_area, area)
    
    # Now, pop the remaining bars from stack and calculate area
    while stack:
        top_of_stack = stack.pop()
        area = (heights[top_of_stack] * 
              ((index - stack[-1] - 1) if stack else index))
        max_area = max(max_area, area)
    
    return max_area

# Input Reading
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
heights = list(map(int, data[1:N+1]))

# Calculate and print the largest rectangle area
print(largestRectangleArea(heights))
