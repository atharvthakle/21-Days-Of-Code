#Given two trees check if they are structurally identically. Structurally identical trees are trees that have same structure. They may or may not have the same data though.

Input Format
Enter the values of all the nodes in the binary tree in pre-order format where true suggest the node exists and false suggests it is NULL

Constraints
1 <= N <= 10^4

Output Format
Display the Boolean result

Sample Input
10 true 20 true 40 false false true 50 false false true 30 true 60 false false true 73 false false
10 true 20 true 40 false false true 50 false false true 30 true 60 false false true 73 false false

Sample Output
true
Explanation
The given two trees have the exact same structure and hence we print true.#


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def create_tree():
    data = input().split()
    root = Node(data[0])
    stack = [(root, data[1:])]
    while stack:
        node, data = stack.pop(0)
        has_left = data.pop(0) == 'true'
        if has_left:
            node.left = Node(data.pop(0))
            stack.append((node.left, data))
        has_right = data.pop(0) == 'true'
        if has_right:
            node.right = Node(data.pop(0))
            stack.append((node.right, data))
    return root

def are_structurally_identical(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    return are_structurally_identical(root1.left, root2.left) and are_structurally_identical(root1.right, root2.right)

root1 = create_tree()
root2 = create_tree()
print(str(are_structurally_identical(root1, root2)).lower())
