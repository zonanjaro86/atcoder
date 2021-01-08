N, Q = map(int, input().split())
query = [tuple(map(int, input().split())) for _ in range(Q)]

class UnionFind:
    def __init__(self, n):
        # ルートの場合は負で絶対値は木のサイズを示す
        # それ以外は正で親の番号を示す
        self.parents = [-1] * n

    def find(self, x):
        '''
        xのルートを求める
        '''
        if self.parents[x] < 0:
            return x
        else:
            # 親のルートを探す
            root = self.find(self.parents[x])
            # 親のルートにつなぎ直す
            self.parents[x] = root
            return root

    def union(self, x, y):
        '''
        別グループの場合同じグループにする
        '''
        x = self.find(x)
        y = self.find(y)

        # 同じルートの場合何もしない
        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)

uf = UnionFind(N)
for P, A, B in query:
    if P == 0:
        uf.union(A, B)
    elif P == 1:
        if uf.same(A, B):
            print("Yes")
        else:
            print("No")

