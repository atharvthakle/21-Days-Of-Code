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
