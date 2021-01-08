# -*- coding: utf-8 -*-

N, Ma, Mb = map(int, input().split())

d = []
for i in range(N):
    a, b, c = map(int, input().split())
    d.append((a, b, c))

# 全探索だとTLEなのでDPを用いる

# dp[i][ca][cb] := i-1番目までの組み合わせでAがca,Bがcbとなるときの最小コスト

INF = float('inf')
g_max = 10 * N
dp = [[[INF for cb in range(g_max+1)] for ca in range(g_max+1)] for i in range(N+1)]

dp[0][0][0] = 0

for i in range(N):
    for ca in range(g_max+1):
        for cb in range(g_max+1):
            if dp[i][ca][cb] == INF:
                continue
            a, b, c = d[i]
            # i番目の薬品を選ばない場合
            dp[i+1][ca][cb] = min(dp[i+1][ca][cb], dp[i][ca][cb])
            # i番目の薬品を選ぶ場合
            dp[i+1][ca+a][cb+b] = min(dp[i+1][ca+a][cb+b], dp[i][ca][cb]+c)

ans = -1
for ca in range(g_max+1):
    for cb in range(g_max+1):
        c = dp[N][ca][cb]
        if c == INF:
            continue
        if ca*Mb == cb*Ma and c > 0:
            if ans < 0 or c < ans:
                ans = c

print(ans)