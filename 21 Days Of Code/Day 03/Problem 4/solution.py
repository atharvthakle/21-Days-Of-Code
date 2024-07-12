h = input()
l = list(h)
sum_even = 0
sum_odd = 0

for i in range(len(l)):
    if i % 2 == 0:
        sum_even += int(l[i])
    else:
        sum_odd += int(l[i])

print(sum_odd)
print(sum_even)
