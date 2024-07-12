#You will be given a number N. You have to code a hollow diamond looking pattern.

The output for N=5 is given in the following image.

Screen Shot 2016-06-09 at 2.47.18 pm.png

Input Format
The input has only one single integer N.

Constraints
Output Format
Output the given pattern.

Sample Input
5
Sample Output
*********
**** ****
***    ***
**      **
*         *
**      **
***    ***
**** ****
*********
Explanation
Write a code to print above given pattern. No space between any two characters.#


w = int(input())
count = w
k = 0

# Upper half
for i in range(w):
    print('*\t' * count, end='')
    print('\t' * k, end='')

    if i >= 1:
        k += 2
    else:
        k += 1

    if i == 0:
        print('*\t' * (w - 1), end='')
    else:
        print('*\t' * count, end='')

    count -= 1
    print()

# Lower half
count = 2
k = k - 4
for i in range(w, 1, -1):
    print('*\t' * count, end='')
    print('\t' * k, end='')

    if i == 3:
        k -= 1
    else:
        k -= 2

    if i == 2:
        print('*\t' * (w - 1), end='')
    else:
        print('*\t' * count, end='')

    count += 1
    print()