import numpy as np
import itertools

# import matplotlib.pyplot as plt
# import matplotlib.patches as ptch

# def display(points, rects, size=10000):
#     fig, ax = plt.subplots(figsize=(10,10))
#     ax.set_xlim([0,size])
#     ax.set_ylim([0,size])
#     ax.set_aspect('equal')
#     X = points[:,1]+0.5
#     Y = points[:,2]+0.5
#     ax.scatter(X, Y, s=3)
#     for rect in rects:
#         a, b, c, d = rect
#         ax.add_patch(ptch.Rectangle((a,b), c-a, d-b, fill=False, lw=1))
#     plt.show()
#     plt.close(fig)

def duplicated(rect1, rect2):
    a1, b1, c1, d1 = rect1
    a2, b2, c2, d2 = rect2
    return a1 <= a2 < c1 and b1 <= b2 < d1 or a1 <= a2 < c1 and b1 < d2 <= d1 or a1 < c2 <= c1 and b1 <= b2 < d1 or a1 <= a2 < c1 and b1 < d2 <= d1

def calc_score(points, rects):
    x, y, r = points[:,1], points[:,2], points[:,3]
    a, b, c, d = rects[:,0], rects[:,1], rects[:,2], rects[:,3]
    s = (c - a) * (d - b)
    sr = np.stack([s, r])
    return 1 - (1 - sr.min(axis=0) / sr.max(axis=0)) ** 2

def narrow(points, rects):
    """重なっている部分の処理
    """
    for (i, x1, y1, r1, a1, b1, c1, d1), (j, x2, y2, r2, a2, b2, c2, d2) in itertools.permutations(np.concatenate([points, rects], axis=1),2):
        # 2つの点の位置関係が横方向なら横に、縦方向なら縦に縮める
        rect1 = [a1, b1, c1, d1]
        rect2 = [a2, b2, c2, d2]
        if duplicated(rect1, rect2):
            if abs(x1 - x2) >= abs(y1 - y2):
                if x1 > x2:
                    i, j = j, i
                middle = (x1 + x2 + 1)//2
                rects[i][2] = min(middle, rects[i][2])
                rects[j][0] = max(middle, rects[j][0])
            else:
                if y1 > y2:
                    i, j = j, i
                middle = (y1 + y2 + 1)//2
                rects[i][3] = min(middle, rects[i][3])
                rects[j][1] = max(middle, rects[j][1])

def spread(points, rects):
    """広げられる方向へ広げる
    """
    for i, x, y, r, a, b, c, d in np.concatenate([points, rects], axis=1):
        s = (c-a)*(d-b)
        # 上下方向へ伸ばす場合の最大長さ
        v_max = (r-s)//(c-a)
        up_spread = min(v_max, 10000-d) # 上限は超えない
        while up_spread > 0:
            can = True
            for j, rect in enumerate(rects):
                if i == j:
                    continue
                if duplicated([a, d, c, d+up_spread], rect):
                    can = False
                    break
            if can:
                break
            up_spread //= 2
        if up_spread > 0:
            rects[i][3] += up_spread
            break

        down_spread = min(v_max, b)
        while down_spread > 0:
            can = True
            for j, rect in enumerate(rects):
                if i == j:
                    continue
                if duplicated([a, d-down_spread, c, d], rect):
                    can = False
                    break
            if can:
                break
            down_spread //= 2
        if down_spread > 0:
            rects[i][1] -= down_spread

        h_max = (r-s)//(d-b)
        right_spread = min(h_max, 10000-c)
        while right_spread > 0:
            can = True
            for j, rect in enumerate(rects):
                if i == j:
                    continue
                if duplicated([c, b, c+right_spread, d], rect):
                    can = False
                    break
            if can:
                break
            right_spread //= 2
        if right_spread > 0:
            rects[i][2] += right_spread

        left_spread = min(h_max, a)
        while left_spread > 0:
            can = True
            for j, rect in enumerate(rects):
                if i == j:
                    continue
                if duplicated([a-left_spread, b, a, d], rect):
                    can = False
                    break
            if can:
                break
            left_spread //= 2
        if left_spread > 0:
            rects[i][0] -= left_spread

def main():

    # n= int(input())
    # points = [tuple(map(int, [i] + input().split())) for i in range(n)]

    n = 0
    points = []
    with open('sample.txt') as f:
        n = int(f.readline())
        for i in range(n):
            points.append(tuple(map(int, [i] + f.readline().split())))

    points = np.array(points)
    X = points[:,1]
    Y = points[:,2]
    R = points[:,3]

    # 初期化
    W = H = np.floor(R**0.5).astype('int')
    # rects = np.stack((X-W//2, Y-H//2, X+1+W//2, Y+1+H//2), axis=1)
    rects = np.stack((X-W//2, Y-H//2, X+W//2, Y+H//2), axis=1)

    # 端処理
    for rect in rects:
        a, b, c, d = rect
        if a < 0:
            rect[0] = 0
        if b < 0:
            rect[1] = 0
        if c > 10000:
            rect[2] = 10000
        if d > 10000:
            rect[3] = 10000

    # 重複部分を狭める
    narrow(points, rects)

    # 広げて狭めてを収束するまで繰り返す
    score = sum(calc_score(points, rects))/n*10**9
    prev_score = 0
    for _ in range(100):
        spread(points, rects)
        narrow(points, rects)
        prev_score = score
        score = sum(calc_score(points, rects))/n*10**9

        if prev_score == score:
            break
        # print(score)
    # print(score)
    # print(calc_score(points, rects))
    for rect in rects:
        print(*rect)
    # display(points, rects)

if __name__ == '__main__':
    main()