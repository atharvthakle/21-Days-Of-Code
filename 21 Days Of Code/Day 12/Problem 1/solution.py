#There are N processes to be completed. All the processes have a unique number assigned to them from 1 to N.

Now, we are given two things:

1)The calling order in which all the processes are called.
2)The ideal order in which all the processes should have been executed.

Executing a process takes 1 unit of time. Changing the position takes 1 unit of time.

We have to find out the unit of time required to complete all the process such that a process is executed from the ideal order only when it exists at the same index in the calling order. We can push the first term from the calling order to the last thus rotating the order.

Input Format
First line contains a single integer N.
Next line contains N space separated integers denoting the calling order.
Last line contains N space separated integers denoting the ideal order.

Constraints
1 <= N <= 10^6

Output Format
The total time required

Sample Input
5
5 4 2 3 1
5 2 1 4 3
Sample Output
7#


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
