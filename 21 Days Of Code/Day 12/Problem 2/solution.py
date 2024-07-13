from collections import deque

def process_operations(operations):
    course_queues = {1: deque(), 2: deque(), 3: deque(), 4: deque()}
    order_queue = deque()
    result = []

    for operation in operations:
        op = operation.split()
        if op[0] == 'E':
            course = int(op[1])
            roll_number = int(op[2])
            if not course_queues[course]:
                order_queue.append(course)
            course_queues[course].append(roll_number)
        elif op[0] == 'D':
            course = order_queue[0]
            roll_number = course_queues[course].popleft()
            result.append(f"{course} {roll_number}")
            if not course_queues[course]:
                order_queue.popleft()

    return result

# Read input
q = int(input())
operations = [input().strip() for _ in range(q)]

# Process the operations
result = process_operations(operations)

# Print the result
for res in result:
    print(res)
