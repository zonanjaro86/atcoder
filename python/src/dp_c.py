N = int(input())
abc = [(0, 0, 0)] + [tuple(map(int, input().split())) for _ in range(N)]
a, b, c = zip(*abc)

# dp[i][k]:i日目にkの活動を行ったときのi日目までの幸福度の最大値
dp = [[0] * 3 for _ in range(N+1)]
for i in range(1, N+1):
    dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + a[i]
    dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + b[i]
    dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + c[i]
print(max(dp[N]))