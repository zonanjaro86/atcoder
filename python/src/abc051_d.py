# -*- coding: utf-8 -*-

from heapq import heappop, heappush

N, M = map(int, input().split())

# 隣接リスト
g = [[] for i in range(N)]
e = []
for i in range(M):
    a, b, c = map(int, input().split())
    g[a-1].append((b-1, c))
    g[b-1].append((a-1, c))
    e.append((a-1, b-1, c))

def dijkstra(nodeCnt, start, edges):

    # 始点からのコスト
    costs = [-1 for i in range(nodeCnt)]

    # 確定フラグ
    done = [False for i in range(nodeCnt)]

    # priority queue
    q = []

    costs[start] = 0
    heappush(q, (0, start))

    while len(q) > 0:
        # 確定ノードを取り出す
        doneNode = heappop(q)[1]

        # 確定フラグを立てる
        done[doneNode] = True

        # 接続先ノードの情報を更新
        for to,edge_cost in edges[doneNode]:
            cost = costs[doneNode] + edge_cost
            if costs[to] < 0 or cost < costs[to]:
                costs[to] = cost
                if to not in q:
                    heappush(q, (cost, to))

    return costs

dist = [dijkstra(N, i, g) for i in range(N)]
# print(dist)

# edge(i,j)が最短経路に含まれているとき、
# dist(s,i) + edge(i,j) = dist(s,j)を満たす
ans = 0
for i, j, cost in e:
    isUsed = False
    for s in range(N):
        if dist[s][i] + cost == dist[s][j]:
            isUsed = True
            break
    if not isUsed:
        ans += 1
print(ans)
