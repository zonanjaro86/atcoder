# -*- coding: utf-8 -*-

# import
from collections import namedtuple
from heapq import heappop, heappush

# input
S= list(input())
x, y = map(int, input().split())

# output
print(' '.join([str(n) for n in [1,2,3]]))

# 2進数文字列へ変換
bin = format(255, 'b')

# 2次元配列作成
array = [[-1 for j in range(3)] for i in range(2)]

# loop
for i in range(5):
    pass
for n in [1,2,3]:
    pass
for i,n in enumerate([1,2,3]):
    pass

# bit探索
n = 5
while n > 0:
    if ((n & 1) == 1):
        pass
    n >>= 1

# bit全探索
n = 3
for i in range(2**n):
    r = []
    for j in range(n):
        if (i >> j) & 1:
            r.append(j)
    print(r)

# 関数
def func(x,y):
    return x + y

# 約数をもとめる
def devisor(n):
    ret = []
    i = 1
    while i <= n**0.5:
        if n % i == 0:
            ret.append(i)
            if i**2 != n:
                ret.append(int(n / i))
        i += 1
    ret.sort()
    return ret