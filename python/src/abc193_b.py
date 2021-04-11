N = int(input())
APX = [tuple(map(int, input().split())) for _ in range(N)]

canbuy = False
ans = 10**9+1
for A, P, X in APX:
    if X-A > 0:
        ans = min(ans, P)
        canbuy = True
if canbuy:
    print(ans)
else:
    print(-1)