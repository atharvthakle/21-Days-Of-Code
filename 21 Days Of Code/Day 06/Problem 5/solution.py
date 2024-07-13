def fn(l, n):
    l.sort()
    sum1 = 0
    for i in range(n):
        sum1 += l[i]
    sum2 = 0
    for i in range(n, 2 * n):
        sum2 += l[i]
    if sum1 != sum2:
        s = ' '.join(map(str, l[0:n]))
        s += ' '
        s += ' '.join(map(str, l[n:2*n]))
        return s
    return -1

n = int(input())
l = list(map(int, input().split()))
print(fn(l, n))
