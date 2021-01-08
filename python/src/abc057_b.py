n, m = map(int, input().split())
a = []
b = []
for _ in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)
c = []
d = []
for _ in range(m):
    cj, dj = map(int, input().split())
    c.append(cj)
    d.append(dj)

for i in range(n):
    dist_min = 10 ** 9
    ans = 0
    for j in range(m):
        dist = abs(a[i] - c[j]) + abs(b[i] - d[j])
        if dist < dist_min:
            dist_min = dist
            ans = j+1
    print(ans)