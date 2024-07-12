#Given a binary tree find sum of all the nodes.

Input Format
Enter the value of the node then the Boolean choice i.e whether the node has a left child , then enter the left child's data . The input acts in a recursive manner i.e when the left child's children are made only then we move onto the parent's right child

Constraints
None

Output Format
Display the sum of all the nodes

Sample Input
50 true 25 true 12 false false false true 75 true 62 false false false

Sample Output
224
Explanation
If we enter the following values

50 true 25 true 12 false false false true 75 true 62 false false false

the tree would look like :

25 => 50 <= 75

12 => 25 <= END

END => 12 <= END

62 => 75 <= END

END => 62 <= END#


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
