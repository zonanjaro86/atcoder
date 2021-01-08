# 後でやる

import sys
from collections import defaultdict

input = sys.stdin.readline
N, Q = map(int, input().split())
C = list(map(int, input().split()))
Query = [tuple(map(int, input().split())) for _ in range(Q)]

class UnionFind:
    def __init__(self, n, C):
        self.n = n
        self.parents = [-1] * n
        self.dict = [{c:1} for i, c in enumerate(C)]

    def find(self, x):
        '''
        xのルートを求める
        '''
        if self.parents[x] < 0:
            return x
        else:
            root = self.find(self.parents[x])
            self.parents[x] = root
            return root

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

        for key, value in self.dict[y].items():
            if self.dict[x].get(key):
                self.dict[x][key] += value
            else:
                self.dict[x][key] = value

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

uf = UnionFind(N, C)
for k, a, b in Query:
    if k == 1:
        uf.union(a-1, b-1)
    elif k == 2:
        d = uf.dict[uf.find(a-1)]
        if d.get(b):
            print(d[b])
        else:
            print(0)

