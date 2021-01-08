N, M = map(int, input().split())
k = []
s = []
for _ in range(M):
    tmp = list(map(int, input().split()))
    k.append(tmp[0])
    s.append(tmp[1:])
p = list(map(int, input().split()))

ans = 0
for i in range(2**N):
    on = {j+1: (i >> j) & 1 for j in range(N)}
    ok = True
    for k in range(M):
        on_count = p[k]
        for switch in s[k]:
            on_count += on[switch]
        if not on_count % 2 == 0:
            ok = False
            break
    if ok:
        ans += 1
print(ans)
