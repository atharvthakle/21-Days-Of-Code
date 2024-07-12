#In the land of Blocksburg, Mr. Blocks and his friend Mayank love to explore arrays of integers. They stumbled upon a fascinating concept called a unimodal array.

An array is considered unimodal if it follows these rules:

It starts with a strictly increasing sequence. Then, it maintains a constant sequence. Finally, it ends with a strictly decreasing sequence. However, it's perfectly fine if the first or last block is absent, or even both!

For instance, arrays like [5, 7, 11, 11, 2, 1], [4, 4, 2], and [7] are considered unimodal, while arrays like [5, 5, 6, 6, 1], [1, 2, 1, 2], and [4, 5, 5, 6] are not.

Now, Mr. Blocks and Mayank are intrigued to write a program that can determine if an array is unimodal. Can you help them in their quest?

Input Format
The first line contains integer n (1 ≤ n ≤ 100) — the number of elements in the array. The second line contains n integers a1, a2, …, an (1 ≤ ai ≤ 1000) — the elements of the array.

Constraints
(1 ≤ n ≤ 100),
(1 ≤ ai ≤ 1000)

Output Format
Print "YES" if the given array is unimodal. Otherwise, print "NO".
Note : While Taking Input and Output Ignore Test case Input No and Test Case Output No, These are for your understanding.

Sample Input
Input Case 1: 
6
1 5 5 5 4 2
Input Case 2: 
4
1 2 1 2
Sample Output
Output Case 1:  YES
Output Case 2:  NO#



def fn(l, n):
    if l[0] > l[1]:
        return 'NO'
    elif l[0] == l[1]:
        count = 0
        for i in range(1, n - 1):
            if l[i] == l[i + 1] and count == 0:
                continue
            elif l[i] > l[i + 1]:
                count += 1
            else:
                return 'NO'
        return 'YES'
    else:
        count = 0
        count1 = 1
        for i in range(1, n - 1):
            if l[i] == l[i + 1] and count == 0:
                count1 = 0
                continue
            elif l[i] > l[i + 1]:
                count1 += 1
                count += 1
            elif l[i] < l[i + 1] and count1 == 1:
                continue
            else:
                return 'NO'
        return 'YES'

n = int(input())
l = list(map(int, input().split()))
print(fn(l, n))
