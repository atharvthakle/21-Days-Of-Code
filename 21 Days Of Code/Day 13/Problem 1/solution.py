#Given a Binary Tree Print all the leaf nodes.

Input Format
Level order input of the binary tree

Constraints
Total no of nodes <1000

Output Format
All leaf nodes from left to right in single line

Sample Input
1
2 3
4 5
6 7
-1 -1
-1 -1
-1 -1
-1 -1
Sample Output
4 5 6 7#


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_tree(level_order):
    if not level_order:
        return None
    iter_order = iter(level_order)
    root_value = next(iter_order)
    if root_value == -1:
        return None
    root = TreeNode(root_value)
    queue = [root]
    while queue:
        current = queue.pop(0)
        if current is not None:
            left_value = next(iter_order, None)
            right_value = next(iter_order, None)
            if left_value is not None and left_value != -1:
                current.left = TreeNode(left_value)
                queue.append(current.left)
            if right_value is not None and right_value != -1:
                current.right = TreeNode(right_value)
                queue.append(current.right)
    return root

def print_leaf_nodes(root):
    if root is None:
        return
    if root.left is None and root.right is None:
        print(root.value, end=' ')
    if root.left:
        print_leaf_nodes(root.left)
    if root.right:
        print_leaf_nodes(root.right)

# Input handling
import sys
input = sys.stdin.read
data = input().split()
level_order = list(map(int, data))

root = build_tree(level_order)

# Print leaf nodes
print_leaf_nodes(root)
print()  # For a newline after printing all leaf nodes
