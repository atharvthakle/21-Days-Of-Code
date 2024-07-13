class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def create_tree():
    data = input().split()
    root = Node(int(data[0]))
    stack = [(root, data[1:])]
    while stack:
        node, data = stack.pop(0)
        has_left = data.pop(0) == 'true'
        if has_left:
            node.left = Node(int(data.pop(0)))
            stack.append((node.left, data))
        has_right = data.pop(0) == 'true'
        if has_right:
            node.right = Node(int(data.pop(0)))
            stack.append((node.right, data))
    return root

def sum_of_nodes(root):
    if root is None:
        return 0
    return root.data + sum_of_nodes(root.left) + sum_of_nodes(root.right)

root = create_tree()
print(sum_of_nodes(root))
