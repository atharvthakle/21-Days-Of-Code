def find_winner(M, N):
    turn = 1
    while True:
        if turn % 2 != 0:  # Aayush's turn (1, 3, 5, ...)
            if M >= turn:
                M -= turn
            else:
                return "Harshit"
        else:  # Harshit's turn (2, 4, 6, ...)
            if N >= turn:
                N -= turn
            else:
                return "Aayush"
        turn += 1

# Input number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    M, N = map(int, input().split())
    print(find_winner(M, N))
