def min_time_to_complete_processes(n, calling_order, ideal_order):
    time_taken = 0
    while calling_order:
        if calling_order[0] == ideal_order[0]:
            calling_order.pop(0)
            ideal_order.pop(0)
            time_taken += 1
        else:
            calling_order.append(calling_order.pop(0))
            time_taken += 1
    return time_taken

n = int(input())
calling_order = list(map(int, input().split()))
ideal_order = list(map(int, input().split()))
print(min_time_to_complete_processes(n, calling_order, ideal_order))
