# -*- coding: utf-8 -*-

from heapq import heappop, heappush

# 頂点数
V = 6


input = [
    [0,1,2],
    [0,2,4],
    [0,3,5],
    [1,2,3],
    [1,4,6],
    [2,3,2],
    [2,4,2],
    [3,5,6],
    [4,5,4]
]
# 辺
# edges[from] = [(to, cost), ...]
edges = [[] for i in range(V)]
for a,b,c in input:
    edges[a].append((b,c))
    edges[b].append((a,c))
# print(edges)


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

print(dijkstra(nodeCnt=V, start=0, edges=edges))

