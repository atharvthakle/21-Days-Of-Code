# Problem 4

Given a Binary tree check if it is balanced i.e. depth of the left and right sub-trees of every node differ by 1 or less.

## Input Format

Enter the values of all the nodes in the binary tree in pre-order format where true suggest the node exists and false suggests it is NULL

### Constraints

1 <= No of nodes <= 10^5

## Output Format

Display the Boolean result

### Sample Input

10 true 20 true 40 false false true 50 false false true 30 true 60 false false true 73 false false

### Sample Output

true

## Explanation

The tree looks like

              10
           /       \
        20           30
     /     \       /     \
    40      50    60      73

The given tree is clearly balanced as depths of the left and right sub-trees of every node differ by 1 or less.
