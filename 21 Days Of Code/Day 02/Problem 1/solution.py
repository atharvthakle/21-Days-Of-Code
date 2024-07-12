l1 = input().strip().split()
print(l1)
t = int(l1[0])
f = int(l1[1])
low = int(l1[2])
hig = int(l1[3])
no_input = int(l1[4])
q = []
for i in range(no_input):
    q.append(input().rstrip().split())
for i in range(len(q)):
    tower1 = int(q[i][0])
    tower2 = int(q[i][2])
    floor1 = int(q[i][1])
    floor2 = int(q[i][3])
    ans = abs(tower2 - tower1)
    mini = min(abs(floor1 - low), abs(floor1 - hig))
    ans += mini
    if abs(floor1 - low) == mini:
        ans += abs(floor2 - low)
    else:
        ans += abs(floor2 - hig)
    print(ans)
