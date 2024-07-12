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
