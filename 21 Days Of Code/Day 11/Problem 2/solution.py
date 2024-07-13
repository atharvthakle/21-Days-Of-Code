def calculateSpan(prices, n):
    span = [0] * n
    stack = []
    span[0] = 1
    stack.append(0)
    for i in range(1, n):
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()
        span[i] = i + 1 if not stack else i - stack[-1]
        stack.append(i)
    return span

def main():
    N = int(input().strip())
    prices = list(map(int, input().strip().split()))
    
    spans = calculateSpan(prices, N)
    print(" ".join(map(str, spans)) + " END")

if __name__ == "__main__":
    main()
