# Given a linked list with n nodes. Find the kth element from last without computing the length of the linked list.

Input Format
First line contains space separated integers representing the node values of the linked list. The list ends when the input comes as '-1'. The next line contains a single integer k.

Constraints
n < 10^5

Output Format
Output a single line containing the node value at the kth element from last.

Sample Input
1 2 3 4 5 6 -1
3
Sample Output
4
Explanation
The linked list is 1 2 3 4 5 6. -1 is not included in the list. So the third element from the last is 4 #


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

def kth_element_from_last(head, k):
    main_ptr = head
    ref_ptr = head

    # Move ref_ptr k nodes ahead
    for _ in range(k):
        if ref_ptr is None:
            return None  # If k is greater than the length of the list
        ref_ptr = ref_ptr.next

    # Move both pointers one step at a time
    while ref_ptr is not None:
        main_ptr = main_ptr.next
        ref_ptr = ref_ptr.next

    return main_ptr.data

def main():
    head = None

    while True:
        data = int(input())
        if data == -1:
            break
        head = insert_node(head, data)

    k = int(input())

    result = kth_element_from_last(head, k)
    if result is not None:
        print(result)
    else:
        print("k is greater than the length of the list")

if __name__ == "__main__":
    main()