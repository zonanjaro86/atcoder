N, M = map(int, input().split())

rel = [[0]*N for i in range(N)]
for i in range(N):
    rel[i][i] = 1
for _ in range(M):
    x, y = map(int, input().split())
    rel[x-1][y-1] = 1
    rel[y-1][x-1] = 1

ans = 1
for i in range(2**N):
    check = [j for j in range(N) if (i>>j)&1]
    ok = True
    for j in check:
        for k in check:
            if not rel[j][k]: ok = False
    if ok:
        ans = max(ans, len(check))
print(ans)