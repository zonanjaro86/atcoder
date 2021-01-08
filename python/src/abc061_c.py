N, K = map(int, input().split())

cnt = {}
for i in range(N):
    a, b = map(int, input().split())
    cnt[a] = cnt.get(a, 0) + b

cnt = sorted(cnt.items())

sum = 0
for a, b in cnt:
    sum += b
    if sum >= K:
        print(a)
        break
