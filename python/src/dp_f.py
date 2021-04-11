s = input()
t = input()

# dp[i][j]: sのi文字目まで、tのj文字目まで使ったときの部分文字列の長さの最大
dp = [[0] * (len(t)+1) for _ in range(len(s)+1)]
for i in range(1, len(s)+1):
    for j in range(1, len(t)+1):
        if s[i-1] == t[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

k, l = len(s), len(t)
lcs_len = dp[k][l]
ans = ''
while len(ans) < lcs_len:
    if s[k-1] == t[l-1]:
        ans = s[k-1] + ans
        k -= 1
        l -= 1
    elif dp[k-1][l] == dp[k][l]:
        k -= 1
    elif dp[k][l-1] == dp[k][l]:
        l -= 1
print(ans)
