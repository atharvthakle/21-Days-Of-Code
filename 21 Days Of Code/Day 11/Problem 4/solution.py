#You are at a casino. There are N stacked cards on pile A0. Each card has a number written on it. Then there will be Q iterations. In ith iteration, you start picking up the cards in Ai-1th pile from the top one by one and check whether the number written on the card is divisible by the ith prime number. If the number is divisible, you stack that card on pile Bi. Otherwise, you stack that card on pile Ai. After Q iterations, cards can only be on pile B1, B2, B3, . . . BQ, AQ . Output numbers on these cards from top to bottom of each piles in order of B1, B2, B3, . . . BQ, AQ .

Input Format
First line contains N and Q. The next line contains N space separated integers representing the initial pile of cards i.e., A0. The leftmost value represents the bottom plate of the pile.

Constraints
N < 10^5
Q < 10^5
|Ai| < 10^9

Output Format
Output N lines, each line containing the number written on the card.

Sample Input
5 1
3 4 7 6 5
Sample Output
4
6
3
7
5
Explanation
Initially:

A0 = [3, 4, 7, 6, 5]<-TOP

After 1st iteration:

A0 = []<-TOP

A1 = [5, 7, 3]<-TOP

B1 = [6, 4]<-TOP

Now first print B1 from top to bottom then A1 from top to bottom.#


import math

def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, n + 1) if primes[p]]

def process_cards(cards, primes):
    piles = {'A0': cards}
    for i, prime in enumerate(primes):
        piles[f'B{i+1}'] = []
        piles[f'A{i+1}'] = []
        for card in piles[f'A{i}'][::-1]:
            if card % prime == 0:
                piles[f'B{i+1}'].append(card)
            else:
                piles[f'A{i+1}'].append(card)
        piles[f'A{i}'] = []
    return piles

def print_piles(piles, q):
    for i in range(1, q + 1):
        for card in piles[f'B{i}'][::-1]:
            print(card)
    for card in piles[f'A{q}'][::-1]:
        print(card)

n, q = map(int, input().split())
cards = list(map(int, input().split()))
primes = sieve_of_eratosthenes(1000000)[:q]
piles = process_cards(cards, primes)
print_piles(piles, q)
