# Problem 2

Given a binary tree find sum of all the nodes.

## Input Format

Enter the value of the node then the Boolean choice i.e whether the node has a left child , then enter the left child's data . The input acts in a recursive manner i.e when the left child's children are made only then we move onto the parent's right child

## Output Format

Display the sum of all the nodes

### Sample Input

50 true 25 true 12 false false false true 75 true 62 false false false

### Sample Output

224

## Explanation

If we enter the following values

50 true 25 true 12 false false false true 75 true 62 false false false

the tree would look like :

25 => 50 <= 75

12 => 25 <= END

END => 12 <= END

62 => 75 <= END

END => 62 <= END
