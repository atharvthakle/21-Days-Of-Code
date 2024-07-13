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
