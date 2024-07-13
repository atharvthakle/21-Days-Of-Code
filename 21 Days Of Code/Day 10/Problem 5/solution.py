class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def sortList(head):
    count = [0, 0, 0]  # To store the count of 0's, 1's, and 2's
    
    current = head
    while current:
        count[current.data] += 1
        current = current.next
    
    current = head
    i = 0
    while current:
        if count[i] == 0:
            i += 1
        else:
            current.data = i
            count[i] -= 1
            current = current.next

def createList(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for value in arr[1:]:
        current.next = Node(value)
        current = current.next
    return head

def printList(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

def main():
    N = int(input())
    elements = list(map(int, input().split()))
    
    head = createList(elements)
    sortList(head)
    printList(head)

if __name__ == "__main__":
    main()
