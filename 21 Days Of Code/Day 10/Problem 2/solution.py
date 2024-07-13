class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_k_elements(head, k):
    current = head
    prev = None
    next_node = None
    count = 0
    
    # Reverse the first k nodes of the linked list
    while current is not None and count < k:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
        count += 1
    
    # Now next_node is pointing to (k+1)th node
    if next_node is not None:
        head.next = reverse_k_elements(next_node, k)
    
    # prev is now the new head of the reversed group
    return prev

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
    
    N = int(data[0])
    K = int(data[1])
    
    head = None
    for i in range(2, 2 + N):
        head = insert_node(head, int(data[i]))

    head = reverse_k_elements(head, K)
    print_linked_list(head)

if __name__ == "__main__":
    main()
