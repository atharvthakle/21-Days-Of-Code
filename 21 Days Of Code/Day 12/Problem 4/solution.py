from collections import deque

def reverse_k_elements(queue, k):
    stack = []
    
    # Step 1: Dequeue first k elements from the queue and push them onto the stack
    for _ in range(k):
        stack.append(queue.popleft())
    
    # Step 2: Pop elements from the stack and enqueue them back into the queue
    while stack:
        queue.append(stack.pop())
    
    # Step 3: Move the remaining elements in the queue to the back to preserve order
    for _ in range(len(queue) - k):
        queue.append(queue.popleft())
    
    return queue

# Input
n = int(input())
elements = list(map(int, input().split()))
k = int(input())

# Initialize the queue
queue = deque(elements)

# Reverse the first k elements
queue = reverse_k_elements(queue, k)

# Output the resulting queue
print(" ".join(map(str, queue)))
