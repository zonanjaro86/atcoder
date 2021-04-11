N, W = map(int, input().split())
wv = [(0,0)] + [tuple(map(int, input().split())) for _ in range(N)]
w, v = zip(*wv)

# dp[i][j]: i番目の品物までの中で重さがj以下となる場合の価値の総和の最大値
dp = [[0] * (W+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(0, W+1):
        if j - w[i] >= 0:
            dp[i][j] = max(dp[i-1][j-w[i]] + v[i], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[N][W])