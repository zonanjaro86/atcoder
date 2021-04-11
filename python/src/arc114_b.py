# N = int(input())
# f = tuple(map(int, input().split()))

N = 2
f = (2, 1)

mod = 998244353

class UnionFindTree:
    def __init__(self, n):
        self.size = [0]*n
        self.parents = [0]*n
        for i in range(n):
            self.make_tree(i)

    def make_tree(self, x):
        self.parents[x] = x
        self.size[x] = 1

    def is_same(self, x, y):
        return self.find_root(x) == self.find_root(y)

    def find_root(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find_root(self.parents[x])
        return parents[x]

    def unite(self, x, y):
        x = self.find_root(x)
        y = self.find_root(y)
        if x == y:
            return False
        if self.size[x] > self.size[y]:
            self.parents[y] = x
            size[x] += size[y]
        else:
            self.parents[x] = y
            size[y] += size[x]
        return True

    def tree_size(self, x):
        return self.size[self.find_root(x)]

tree = UnionFindTree(N)
for x, y in enumerate(f):
    tree.unite(x, y-1)