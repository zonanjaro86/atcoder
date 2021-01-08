import numpy as np

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
c = np.array([input() for _ in range(R)])

vec = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0)
]

dir_map = np.full((R, C), -1)
dir_map[sy - 1][sx - 1] = 0
queue = [(sy - 1, sx - 1)]

while len(queue) > 0:
    y, x = queue.pop(0)
    dir = dir_map[y][x]
    for dy, dx in vec:
        ny, nx = y + dy, x + dx
        if c[ny][nx] == '.':
            if dir_map[ny][nx] == -1 or dir + 1 < dir_map[ny][nx]:
                dir_map[ny][nx] = dir + 1
                queue.append((ny, nx))

print(dir_map[gy - 1][gx - 1])