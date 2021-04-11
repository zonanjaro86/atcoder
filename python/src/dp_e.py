N, W = map(int, input().split())
wv = [(0,0)] + [tuple(map(int, input().split())) for _ in range(N)]
w, v = zip(*wv)

# dp[i][j]: i番目の品物までの中で価値がj以上となる場合の重さの最小値
INF = 10**9+1
dp = [[INF] * (10**5+1) for _ in range(N+1)]
dp[0][0] = 0
for i in range(1, N+1):
    for j in range(0, 10**5+1):
        if j - v[i] >= 0:
            dp[i][j] = min(dp[i-1][j-v[i]] + w[i], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
ans = 10**5
while dp[N][ans] > W:
    ans -= 1
print(ans)