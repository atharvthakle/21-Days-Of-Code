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
