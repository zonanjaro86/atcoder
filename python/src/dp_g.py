import sys
sys.setrecursionlimit(1000000)

# N:点の数、M:辺の数
N, M = map(int, input().split())

# x => yの有向グラフのリスト
edges = [tuple(map(int, input().split())) for _ in range(M)]

# memo化再帰:dp[i]=点iを始点とする有向パスの長さの最大値
flag = [False] * (N+1)
dp = [0] * (N+1)

# ys[i]=点iから辺が向かっている点のリスト
ys = [[] for _ in range(N+1)]
for x, y in edges:
    ys[x].append(y)

# 点xを始点とする有向パスの長さの最大を計算する
def f(x):
    if flag[x]:
        return dp[x]
    dp[x] = 0
    for y in ys[x]:
        dp[x] = max(dp[x], f(y) + 1)
    flag[x] = True
    return dp[x]
print(max([f(i) for i in range(1,N+1)]))
