# -*- coding: utf-8 -*-

# 参考
# https://qiita.com/wakimiko/items/69b86627bea0e8fe29d5

# 頂点の数
V = 6

# 始点終点
S = 0
G = 5

# {(from, to): cost}
edges = {
    (0, 1, 2),
    (0, 3, 4),
    (1, 2, 3),
    (2, 3, -2),
    (2, 5, 2),
    (3, 4, 2),
    (3, 5, 4),
    (4, 5, 1)
}

INF = float('inf')

# d[s][g] : sからgへのコスト、デフォルトを無限大にする
d = [[INF for g in range(V)] for s in range(V)]

# s=gのコストを0にする
for i in range(V):
    d[i][i] = 0

# 各
for s in range(V):
    for g in range(V):
        for f, t, cost in edges:
            if d[s][t] > d[s][f] + cost:
                d[s][t] = d[s][f] + cost
                if g == V-1:
                    print('negative loop')
                    break


print(d)
