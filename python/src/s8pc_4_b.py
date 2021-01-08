import itertools

N, K = map(int, input().split())
a = list(map(int, input().split()))

ans = 10**18
# i番目の建物を伸ばすかどうかをビット全探索
for iter in itertools.product([0, 1], repeat=N):
    color_cnt = 1
    sum_cost = 0
    b = a.copy()
    max_height = b[0]
    for i in range(1, N):
        if b[i] > max_height:
            color_cnt += 1
            max_height = b[i]
        elif iter[i]:
            cost = max_height + 1 - b[i]
            b[i] += cost
            sum_cost += cost
            max_height = b[i]
            color_cnt += 1
    if color_cnt >= K:
        ans = min(sum_cost, ans)
print(ans)
