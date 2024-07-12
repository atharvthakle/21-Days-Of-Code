# Problem 1

Once upon a time in Blocksville, Mr. Blocks, renowned for his noble deeds, takes charge of supporting the stewards. He's got a group of n stewards to assist this time, each with their own strength.

Now, Mr. Blocks has a particular preference when it comes to supporting stewards. He extends his support to a steward only if there exists at least one steward with strength lower than him and at least one steward with strength higher than him.

Can you unravel the mystery of how many stewards Mr. Blocks will lend his support to ?

## Input Format

First line consists of a single integer n (1 ≤ n ≤ 10^5) — the number of stewards with Mr. Blocks. Second line consists of n space separated integers a1, a2, …, an (0 ≤ ai ≤ 10^9) representing the values assigned to the stewards.

### Constraints

(1 ≤ n ≤ 10^5)

(0 ≤ ai ≤ 10^9

## Output Format

Output a single integer representing the number of stewards that Mr. Blocks will feed.

Note : While Taking Input and Output Ignore Test case Input No and Test Case Output No, These are for your understanding.

### Sample Input

Input Case 1 :

2

1 5

Input Case 2:

3

1 2 5

### Sample Output

Output Case 1:

0

Output Case 2:

1

## Explanation

In the first sample, Mr. Blocks cannot support steward with strength 1 because there is no steward with strength less than 1 and he cannot support steward with strength 5 because there is no steward with strength greater than 5.

In the second sample, Mr. Blocks can support steward with strength 2 because there are stewards with strength less than 2 and greater than 2.
