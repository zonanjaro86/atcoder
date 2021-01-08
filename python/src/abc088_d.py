import numpy as np
from collections import deque

H, W = map(int, input().split())
s = [input() for _ in range(H)]
vec = [(0, 1), (0, -1), (1, 0), (-1, 0)]
'''
最短経路を求め、通らない白いマスの数=ポイントとなる
'''
queue = deque()
queue.append((0, 0))
dir_map = np.full((H, W), -1)
dir_map[0][0] = 0

while queue:
    y, x = queue.popleft()
    dir = dir_map[y][x]
    for dy, dx in vec:
        ny, nx = y + dy, x + dx

        if ny == H - 1 and nx == W - 1:
            dir_map[ny][nx] = dir + 1
            break

        if ny < 0 or ny >= H or nx < 0 or nx >= W:
            continue

        if s[ny][nx] == '#' or dir_map[ny][nx] >= 0:
            continue

        dir_map[ny][nx] = dir + 1
        queue.append((ny, nx))

    else: continue
    break

if dir_map[H - 1][W - 1] < 0:
    print(-1)
else:
    white = sum([row.count('.') for row in s])
    print(white - dir_map[H - 1][W - 1] - 1)


