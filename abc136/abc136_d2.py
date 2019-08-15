# -*- coding: utf-8 -*-

# 入力
S= list(input())
N = len(S)

# 移動回数
cnt = 10**5
M = len(format(cnt, 'b'))

# jにいた子の2**i回移動後の座標をdp[i][j]に
dp = [[-1 for j in range(N)] for i in range(M+1)]

# i = 0
for j in range(N):
    if S[j] == 'L':
        dp[0][j] = j - 1
    else:
        dp[0][j] = j + 1

# i = 1~M+1
for i in range(M):
    for j in range(N):
        dp[i+1][j] = dp[i][dp[i][j]]
# print(dp)


# cnt回移動後の座標を求める
result = []
for j in range(N):
    i = 0
    n = cnt
    cur_j = j
    while n > 0:
        if ((n & 1) == 1):
            cur_j = dp[i][cur_j]
        n >>= 1
        i += 1
    result.append(cur_j)
# print(result)

# 解答出力
ans = [0] * N
for j in range(N):
    ans[result[j]] += 1
print(' '.join([str(n) for n in ans]))
