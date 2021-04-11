N = int(input())
p = tuple(map(float, input().split()))

# dp[i][j]: i枚目まで投げたときj枚表が出る確率
dp = [[0]*(N+1) for _ in range(N+1)]
dp[0][0] = 1

# 配るDP
for i in range(0, N):
    for j in range(i+1):
        dp[i+1][j] += dp[i][j] * (1-p[i])
        dp[i+1][j+1] += dp[i][j] * p[i]

# 表>裏となるのはdp[N][N//2+1]~dp[N][N]
print(sum(dp[N][N//2+1:]))