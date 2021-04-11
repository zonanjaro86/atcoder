import itertools
H, W, K = map(int, map(int, input().split()))
C = [['.'] * W for _ in range(H)]
for _ in range(K):
    h, w, c = input().split()
    h, w = int(h), int(w)
    C[h-1][w-1] = c
print(C)

dp = [[0] * W for _ in range(H)]
dp[0][0] = 1
for i in range(W-1):
    if C[0][i] == 'D':
        dp[0][i+1] = 0
        break
    dp[0][i+1] = 1
for i in range(1, H):
    for j in range(W):
        d, r = 0, 0
        d = dp[i-1][j]
        if j > 0:
            r = dp[i][j-1]
        dp[i][j] = d + r
print(dp)


