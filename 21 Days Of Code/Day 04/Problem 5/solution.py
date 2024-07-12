n = int(input())

if n % 2 == 0:
    count = n + 1
else:
    count = n + 2

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end='\t')
    
    print('\t' * count, end='')
    count -= 2
    
    for j in range(i, 0, -1):
        if j != n:
            print(j, end='\t')
    
    print()
