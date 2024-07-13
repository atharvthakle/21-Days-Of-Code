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
