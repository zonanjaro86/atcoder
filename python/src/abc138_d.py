
N, Q = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(N-1)]
px = [tuple(map(int, input().split())) for _ in range(Q)]

tree = [[] for _ in range(N)]
for a, b in ab:
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)

cnts = [0] * N
visited = [0] * N
for p, x in px:
    cnts[p-1] += x

stack = [0]
while len(stack) > 0:
    n = stack.pop()
    visited[n] = 1
    children = tree[n]
    for child in children:
        if visited[child]:
            continue
        stack.append(child)
        cnts[child] += cnts[n]
print(*cnts)