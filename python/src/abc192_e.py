N, M, X, Y = map(int, input().split())
# 各町からの列車情報(to, T, K)
edges = [[] for _ in range(N)]
for _ in range(M):
    A, B, T, K = map(int, input().split())
    edges[A-1].append((B, T, K))
    edges[B-1].append((A, T, K))

# 各町への最短の到着時間
# 到着できない場合は-1
T_town = [-1 for _ in range(N)]

# BFS
T_town[X-1] = 0
stack = [X]
while stack:
    town = stack.pop()
    time = T_town[town-1]
    # print('town:{}, time:{}'.format(town, time))
    for to, T, K in edges[town-1]:
        wait = (K - time % K) % K
        # print('from:{}, to:{}, wait:{}, T:{}'.format(town, to, wait, T))
        if T_town[to-1] == -1 or T_town[to-1] > time + wait + T:
            T_town[to-1] = time + wait + T
            stack.append(to)
print(T_town[Y-1])

