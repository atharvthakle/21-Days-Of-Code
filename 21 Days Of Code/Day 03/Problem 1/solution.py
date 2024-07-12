#Once upon a time in Blockville, Mr. and Mrs. Blocks were getting ready for a new day in their busy lives.

It was currently hh:mm, displayed in the 24-hour format on their clock.

Now, Mrs. Blocks had a peculiar belief. She was fond of palindromes and firmly believed that waking up at a palindrome time brought good luck. For those who don't know, a palindrome is a string that reads the same forwards and backwards. For instance, 05:50 is a palindrome because it reads the same even when reversed.

So, the question arises: How long should Mrs. Blocks sleep to wake up at a palindrome time?

Imagine Mrs. Blocks pondering over this fascinating idea. She must ensure the clock shows a time that remains the same when read backwards. For example, 05:39 isn't a palindrome, as its reverse is 93:50, but 05:50 is indeed a palindrome since it remains unchanged when read backwards.

Now, can you help Mrs. Blocks determine the minimum number of minutes she should sleep to wake up at a palindrome time, thus ensuring a lucky start to her day in Blockville?

Input Format
The first and only line of input contains a single string in the format hh:mm (00 ≤  hh  ≤ 23, 00 ≤  mm  ≤ 59).

Constraints
hh:mm (00 ≤  hh  ≤ 23, 00 ≤  mm  ≤ 59)

Output Format
Output a single integer on a line by itself, the minimum number of minutes she should sleep, such that, when she wakes up, the time is a palindrome.
Note : Do not print Test Case Output No, Just Print a single Integer similarly Do take input directly as 05:39.

Sample Input
Test Case Input:  05:39
Sample Output
Test Case Output: 11
Explanation
In the first test case, the minimum number of minutes Mrs.Blocks should sleep for is 11. She can wake up at 05:50, when the time is a palindrome.

In the second test case, Mrs.Blocks can wake up immediately, as the current time, 13:31, is already a palindrome.

In the third test case, the minimum number of minutes Mrs.Blocks should sleep for is 1 minute. She can wake up at 00:00, when the time is a palindrome.#


time = input()
hour = time[0:2]
mint = time[3:]
# print(hour)
# print(mint)
rev_h = hour[::-1]
time_sleep = 0
if int(rev_h) == 32 and int(rev_h) - int(mint) < 0:
    time_sleep = 60 - int(mint)
    print(time_sleep)
    exit()
if int(rev_h) - int(mint) >= 0:
    time_sleep = int(rev_h) - int(mint)
    print(time_sleep)
else:
    time_sleep = int(rev_h) + 10 + 60 - int(mint)
    print(time_sleep)
