#The coding blocks members went to the success party of their first ever online boot-camp at Murthal. They ordered P number of paranthas. The stall has L cooks and each cook has a rank R. A cook with a rank R can cook 1 parantha in the first R minutes 1 more parantha in the next 2R minutes, 1 more parantha in 3R minutes and so on(he can only cook a complete parantha) ( For example if a cook is ranked 2.. he will cook one parantha in 2 minutes one more parantha in the next 4 mins and one more in the next 6 minutes hence in total 12 minutes he cooks 3 paranthas. In 13 minutes also he can cook only 3 paranthas as he does not have enough time for the 4th parantha). Calculate the minimum time needed to cook all the paranthas.

Input Format
First line contains P, the number of pratha ordered. In the next line the first integer denotes the number of cooks L and L integers follow in the Next line each denoting the rank of a cook.

Constraints
P <= 1000
L <= 50
1 <= R <= 8

Output Format
Print an integer which tells the number of minutes needed to get the order done.

Sample Input
10
4 
1 2 3 4
Sample Output
12
Explanation
First cook with rank 1 cooks 4 paranthas in 10 minutes (1+2+3+4).
Second cook with rank 2 cooks 3 paranthas in 12 minutes (2+4+6)
Third cook with rank 3 cooks 2 paranthas in 9 minutes (3+6) Fourth cook with rank 4 only needs to cook one last remaining parantha. He can do that in 4 minutes.
Since these cooks cook parallely, the total time taken will be the maximum of the four i.e. 12 minutes.#


def is_possible(cooks, P, mid):
    total_paranthas = 0
    for cook in cooks:
        time = 0
        paranthas = 0
        while time + cook * (paranthas + 1) <= mid:
            paranthas += 1
            time += cook * paranthas
        total_paranthas += paranthas
        if total_paranthas >= P:
            return True
    return total_paranthas >= P

def min_time_to_cook_all_paranthas(P, L, ranks):
    start = 0
    end = (P * (P + 1)) // 2 * min(ranks)  # Max time
    result = end
    
    while start <= end:
        mid = (start + end) // 2
        if is_possible(ranks, P, mid):
            result = mid
            end = mid - 1
        else:
            start = mid + 1
    
    return result

# Input reading
import sys
input = sys.stdin.read
data = input().strip().split()

# First line contains P
index = 0
P = int(data[index])
index += 1

# Second line contains L (number of cooks)
L = int(data[index])
index += 1

# Next L integers denote the rank of each cook
ranks = list(map(int, data[index:index + L]))

# Calculate the minimum time required
min_time = min_time_to_cook_all_paranthas(P, L, ranks)
print(min_time)
