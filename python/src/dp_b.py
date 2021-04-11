N, K = map(int, input().split())
h = list(map(int, input().split()))

# dp[i]: 足場i-1にたどり着くまでの最小のコスト
INF = 10**9
dp = [INF] * N
dp[0] = 0
for i in range(1, N):
    for k in range(1, min(K, i)+1):
        dp[i] = min(dp[i], dp[i-k] + abs(h[i] - h[i-k]))
print(dp[N-1])