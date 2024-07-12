#Given 2 sorted linked lists , merge the two given sorted linked list and print the final Linked List.

Input Format
First Line contains T the number of test cases.
For each test case :
Line 1 : N1 the size of list 1
Line 2 : N1 elements for list 1
Line 3 : N2 the size of list 2
Line 4 : N2 elements for list 2

Constraints
1 <= T <= 1000
0<= N1, N2 <= 10^6
-10^7 <= Ai <= 10^7

Output Format
For each testcase , print the node data of merged linked list.

Sample Input
1
4
1 3 5 7
3
2 4 6
Sample Output
1 2 3 4 5 6 7 
Explanation
The two lists after merging give the sorted output as [1,2,3,4,5,6,7]#


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge_two_sorted_lists(l1, l2):
    dummy = Node(0)
    current = dummy

    while l1 is not None and l2 is not None:
        if l1.data <= l2.data:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    if l1 is not None:
        current.next = l1
    elif l2 is not None:
        current.next = l2

    return dummy.next

def insert_node(head, data):
    if head is None:
        return Node(data)
    else:
        temp = head
        while temp.next is not None:
            temp = temp.next
        temp.next = Node(data)
        return head

def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    idx = 0
    T = int(data[idx])
    idx += 1

    for _ in range(T):
        N1 = int(data[idx])
        idx += 1
        head1 = None
        for i in range(N1):
            head1 = insert_node(head1, int(data[idx]))
            idx += 1

        N2 = int(data[idx])
        idx += 1
        head2 = None
        for i in range(N2):
            head2 = insert_node(head2, int(data[idx]))
            idx += 1

        merged_head = merge_two_sorted_lists(head1, head2)
        print_linked_list(merged_head)

if __name__ == "__main__":
    main()
