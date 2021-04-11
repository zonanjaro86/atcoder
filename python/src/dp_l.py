N = int(input())
a = tuple(map(int, input().split()))

# dp[i][j]: [i:j]が残っているときの次の手番の人の得点-相手の得点の最大値
dp = [[-1] * N for _ in range(N)]
for l in range(N-1, -1, -1):
    for r in range(l, N):
        if l == r:
            dp[l][r] = a[l]
        else:
            dp[l][r] = max(a[l] - dp[l+1][r], a[r] - dp[l][r-1])

print(dp[0][N-1])