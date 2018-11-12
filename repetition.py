s = [int(i) for i in input().split()]
r = sorted(s)
a = []
for i in range(len(r) - 1):
    if r[i] == r[i+1] and r[i] not in a:
        a.append(r[i])
    else:
        continue
print(*a)
