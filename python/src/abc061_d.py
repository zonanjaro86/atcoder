N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]

INF =

def solve():
    cost = [0] * N
    for _ in range(N-1):
        for a, b, c in edges:
            if cost[a-1] - c > cost[b-1]:
                cost[b-1] = cost[a-1] - c
    ans = -cost[N-1]

    # 閉路の判定
    negative = [False] * N
    for _ in range(N):
        for a, b, c in edges:
            negative[b-1] = true

print(solve())