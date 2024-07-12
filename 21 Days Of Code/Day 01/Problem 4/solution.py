while True:
    # Read the operation character
    ch = input().strip()
    
    if ch == 'X' or ch == 'x':
        break
    
    if ch in '+-*/%':
        # Read the two numbers
        N1 = int(input().strip())
        N2 = int(input().strip())
        
        if ch == '+':
            print(N1 + N2)
        elif ch == '-':
            print(N1 - N2)
        elif ch == '*':
            print(N1 * N2)
        elif ch == '/':
            print(N1 // N2)  # Using integer division as expected in a simple calculator
        elif ch == '%':
            print(N1 % N2)
    else:
        print("Invalid operation. Try again.")
