class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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

def add_same_size(head1, head2, carry):
    if head1 is None:
        return None, carry

    result_next, carry = add_same_size(head1.next, head2.next, carry)
    
    total = head1.data + head2.data + carry
    carry = total // 10
    result = Node(total % 10)
    result.next = result_next
    
    return result, carry

def add_remaining(head1, curr, carry):
    if head1 != curr:
        result_next, carry = add_remaining(head1.next, curr, carry)
        total = head1.data + carry
        carry = total // 10
        result = Node(total % 10)
        result.next = result_next
        return result, carry
    return None, carry

def add_lists(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    
    size1 = get_size(head1)
    size2 = get_size(head2)
    
    if size1 == size2:
        result, carry = add_same_size(head1, head2, 0)
    else:
        if size1 < size2:
            head1, head2 = head2, head1
        
        curr = head1
        for _ in range(abs(size1 - size2)):
            curr = curr.next
        
        result_rest, carry = add_same_size(curr, head2, 0)
        result_main, carry = add_remaining(head1, curr, carry)
        
        if result_main is None:
            result = result_rest
        else:
            temp = result_main
            while temp.next is not None:
                temp = temp.next
            temp.next = result_rest
            result = result_main
    
    if carry:
        temp = Node(carry)
        temp.next = result
        result = temp
    
    return result

def get_size(head):
    count = 0
    while head:
        count += 1
        head = head.next
    return count

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    idx = 0
    N = int(data[idx])
    M = int(data[idx + 1])
    idx += 2

    head1 = None
    for i in range(N):
        head1 = insert_node(head1, int(data[idx + i]))
    
    idx += N
    head2 = None
    for i in range(M):
        head2 = insert_node(head2, int(data[idx + i]))
    
    result = add_lists(head1, head2)
    print_linked_list(result)

if __name__ == "__main__":
    main()
