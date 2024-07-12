#Given an array of patterns containing only I’s and D’s. I for increasing and D for decreasing. Devise an algorithm to print the minimum number following that pattern. Digits from 1-9 and digits can’t repeat.

Input Format
The First Line contains an Integer N, size of the array. Next Line contains N Strings separated by space.

Constraints
1 ≤ T ≤ 100 1 ≤ Length of String ≤ 8

Output Format
Print the minimum number for each String separated by a new Line.

Sample Input
5
D I DD II IDI
Sample Output
21
12
321 
123
1324
Explanation
For the Given sample case, For a Pattern of 'D' print a decreasing sequence which is 2 1.#


def get_minimum_number(pattern):
    stack = []
    result = ""
    num = 1
    
    for char in pattern:
        stack.append(num)
        num += 1
        
        if char == 'I':
            while stack:
                result += str(stack.pop())
    
    stack.append(num)
    while stack:
        result += str(stack.pop())
    
    return result

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])
    patterns = data[1:]
    
    for pattern in patterns:
        print(get_minimum_number(pattern))

if __name__ == "__main__":
    main()
