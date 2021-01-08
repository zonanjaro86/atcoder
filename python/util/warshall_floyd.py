# -*- coding: utf-8 -*-

# 全ての2頂点間の最短距離

# 頂点数
V = 3

# iからjへの最短経路
# d[i][j] = min(d[i][j], d[i][k] + d[k][j])

INF = float('inf')
d = [[INF for j in range(V)] for i in range(V)]

# input
d[0][1] = 1
d[1][0] = 1
d[0][2] = 1
d[2][0] = 1
d[1][2] = 3
d[2][1] = 3

for k in range(V):
    for i in range(V):
        for j in range(V):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])

print(d)