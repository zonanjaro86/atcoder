import numpy as np
from collections import deque

H, W, N = map(int, input().split())
field = [input() for _ in range(H)]

vec = [(0, 1), (0, -1), (1, 0), (-1, 0)]

route = {}
for y in range(len(field)):
    for x in range(len(field[y])):
        if field[y][x] in 'S123456789':
            char = field[y][x]
            if char == 'S': char = '0'
            route[char] = (y, x)

ans = 0
for i in range(0, N):
    sy, sx = route[str(i)]
    gy, gx = route[str(i + 1)]
    dir_map = np.full((H, W), -1)
    dir_map[sy][sx] = 0
    queue = deque([(sy, sx)])
    while len(queue) > 0:
        y, x = queue.popleft()
        dir = dir_map[y][x]
        for dy, dx in vec:
            ny, nx = y + dy, x + dx
            if ny == gy and nx == gx:
                ans += dir_map[y][x] + 1
                break
            if ny <= -1 or ny >= H or nx <= -1 or nx >= W:
                continue
            if field[ny][nx] == 'X' or dir_map[ny][nx] >= 0:
                continue

            dir_map[ny][nx] = dir + 1
            queue.append((ny, nx))
        else: continue
        break

print(ans)