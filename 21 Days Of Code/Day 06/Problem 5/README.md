# Problem 5

There are n students in a classroom, each studying a Two subject. Teacher, Mr. Block scratches his head as he faces a puzzling challenge: he's given an array with a length of 2n, which represent marks of each subject for each student. His task is to shuffle it so that the sum of the first n elements isn't the same as that of the last n elements. Mr. Block is lazy. Can you crack this puzzle for him.To make this problem more interesting you have to find the lexicographically minimum rearrangement .

An array x is lexicographically smaller than an array y if in the first position where x and y differ xi<yi or if |x|<|y| and y is a prefix of x (where |x| denotes the size of the array x).

## Input Format

The first line contains an integer n(1≤n≤1000), where 2n is the number of elements in the array a. The second line contains 2n space-separated integers a1, a2, …, a2n (1≤ai≤10^6) — the elements of the array a.

### Constraints

(1≤ n ≤1000) (1≤ ai ≤10^6)

## Output Format

If there's no solution, print "-1" (without quotes). Otherwise, print a single line containing 2n space-separated integers. They must form a reordering of a.

Note : While Taking Input and Output Ignore Test case Input No and Test Case Output No, These are for your understanding.

### Sample Input

Test Case Input 1 : 3 1 2 2 1 3 1

Test Case Input 2 : 1 1 1

### Sample Output

Test Case Output 1: 1 1 1 2 2 3
Test Case Output 2: -1
