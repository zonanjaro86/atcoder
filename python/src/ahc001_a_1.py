import numpy as np

WIDTH = 10000
HEIGHT = 10000
num_iter = 1000

class Page:
    def __init__(self, xyr):
        self.xy = xyr[:,:2]
        self.rects = np.concatenate([self.xy, self.xy + 1], axis=1)
        self.r = xyr[:, 2]

        # すでに広告が占めているかどうか
        # used[i][j]がTrueの場合、(i, j)を左上頂点とするセルが使用済み
        self.used = np.array([[False] * WIDTH for _ in range(HEIGHT)])
        for x, y, _, _ in self.rects:
            self.used[y][x] = True

        self.calc_point()

    def debug_used(self):
        print(self.used)

    def calc_point(self):
        self.s = (self.rects[:,2] - self.rects[:,0]) * (self.rects[:,3] - self.rects[:,1])
        sr = np.stack([self.s, self.r])
        p = 1 - (1 - sr.min(axis=0) / sr.max(axis=0)) ** 2
        self.points = p

    def spread_right(self, i):
        """i番目の広告を右に1マス広げる
        """
        rect = self.rects[i]
        l,t,r,b = rect
        if r == WIDTH or np.any(self.used[t:b,r]):
            return
        rect += [0, 0, 1, 0]
        self.used[t:b,r] = True

    def spread_bottom(self, i):
        """i番目の広告を下に1マス広げる
        """
        rect = self.rects[i]
        l,t,r,b = rect
        if b == HEIGHT or np.any(self.used[b,l:r]):
            return
        rect += [0, 0, 0, 1]
        self.used[b,l:r] = True

    def spread_left(self, i):
        """i番目の広告を左に1マス広げる
        """
        rect = self.rects[i]
        l,t,r,b = rect
        if l == 0 or np.any(self.used[t:b,l-1]):
            return
        rect += [-1, 0, 0, 0]
        self.used[t:b,l-1] = True

    def spread_top(self, i):
        """i番目の広告を上に1マス広げる
        """
        rect = self.rects[i]
        l,t,r,b = rect
        if t == 0 or np.any(self.used[t-1,l:r]):
            return
        rect += [0, -1, 0, 0]
        self.used[t-1,l:r] = True

    def narrow_right(self, i):
        """i番目の広告の右辺を1マス狭める
        """
        rect = self.rects[i]
        l,t,r,b = rect
        if r-1 == self.xy[i][0]:
            return
        rect -= [0, 0, 1, 0]
        self.used[t:b,r-1] = False

    def narrow_bottom(self, i):
        """i番目の広告の下辺を1マス狭める
        """
        rect = self.rects[i]
        l,t,r,b = rect
        if b-1 == self.xy[i][1]:
            return
        rect -= [0, 0, 0, 1]
        self.used[b-1,l:r] = False

    def narrow_left(self, i):
        """i番目の広告の左辺を1マス狭める
        """
        rect = self.rects[i]
        l,t,r,b = rect
        if l == self.xy[i][0]:
            return
        rect -= [-1, 0, 0, 0]
        self.used[t:b,l] = False

    def narrow_top(self, i):
        """i番目の広告の上辺を1マス狭める
        """
        rect = self.rects[i]
        l,t,r,b = rect
        if t == self.xy[i][1]:
            return
        rect -= [0, -1, 0, 0]
        self.used[t,l:r] = False

    def loop(self, i):
        spread = [
            self.spread_bottom,
            self.spread_left,
            self.spread_right,
            self.spread_top,
        ]
        narrow = [
            self.narrow_bottom,
            self.narrow_left,
            self.narrow_right,
            self.narrow_top,
        ]
        for i, rect in enumerate(self.rects):
            for j in range(4):
                if self.s[i] < self.r[i]:
                    spread[j%4](i)
                elif self.s[i] > self.r[i]:
                    narrow[j%4](i)
        self.calc_point()

n = int(input())
xyr = np.array([list(map(int, input().split())) for _ in range(n)])

page = Page(xyr)

for i in range(num_iter):
    page.loop(i)

for rect in page.rects:
    print(*rect.tolist())

print(page.points)



