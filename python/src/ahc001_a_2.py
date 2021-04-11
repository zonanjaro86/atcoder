import sys
def input():
    return sys.stdin.readline()[:-1]

WIDTH = 10000
HEIGHT = 10000
num_iter = 1000

n = int(input())
xyr = [tuple(map(int, input().split())) for _ in range(n)]
# n = 2
# xyr = [
#     (1, 1, 9),
#     (3, 3, 3)
# ]

X, Y, R, rects = [], [], [], []
used = [[False] * WIDTH for _ in range(HEIGHT)]

for x, y, r in xyr:
    X.append(x)
    Y.append(y)
    R.append(r)
    rects.append([x, y, x+1, y+1])
    used[y][x] = True

def calc_point(rect, r):
    a, b, c, d = rect
    s = (c-a)*(d-b)
    return 1 - (1 - min(s,r) / max(s,r)) ** 2

def spread_right(rect):
    a,b,c,d = rect
    if c + 1 > WIDTH or any([used[i][c] for i in range(b, d)]):
        return
    rect[2] += 1
    for i in range(b, d):
        used[i][c] = True

def narrow_right(rect, i):
    a,b,c,d = rect
    if X[i] == c-1:
        return
    rect[2] -= 1
    for i in range(b, d):
        used[i][c-1] = False

def spread_bottom(rect):
    a,b,c,d = rect
    if d + 1 > HEIGHT or any([used[i][a-1] for i in range(b, d)]):
        return
    rect[3] += 1
    for j in range(a, c):
        used[d][j] = True

def narrow_bottom(rect, i):
    a,b,c,d = rect
    if Y[i] == d-1:
        return
    rect[3] -= 1
    for j in range(a, c):
        used[d-1][j] = False

def spread_left(rect):
    a,b,c,d = rect
    if a - 1 < 0 or any([used[i][a-1] for i in range(b, d)]):
        return
    rect[0] -= 1
    for i in range(b, d):
        used[i][a-1] = True

def narrow_left(rect, i):
    a,b,c,d = rect
    if X[i] == a:
        return
    rect[0] += 1
    for i in range(b, d):
        used[i][a] = False

def spread_top(rect):
    a,b,c,d = rect
    if b - 1 < 0 or any([used[b-1][j] for j in range(a, c)]):
        return
    rect[1] -= 1
    for j in range(a, c):
        used[b-1][j] = True

def narrow_top(rect, i):
    a,b,c,d = rect
    if Y[i] == b:
        return
    rect[1] += 1
    for j in range(a, c):
        used[b][j] = False

spread = [
    spread_bottom, spread_left, spread_right, spread_top
]
narrow = [
    narrow_bottom, narrow_left, narrow_right, narrow_top
]

for cnt in range(num_iter):
    for i, rect in enumerate(rects):
        a,b,c,d = rect
        s = (c-a)*(d-b)
        r = R[i]
        if s < r:
            spread[cnt%4](rect)
        elif s > r:
            narrow[cnt%4](rect, i)

# points = [calc_point(rects[i], R[i]) for i in range(n)]
# print(points)
# print(sum(points)/n * 10**9)

for rect in rects:
    print(*rect)
