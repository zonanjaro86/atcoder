# -*- coding: utf-8 -*-

# TLE
from operator import itemgetter

n, m = map(int, input().split())

# A日後、報酬B
a = []
b = []
for i in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)

sum = 0
used = [False] * n
for i in range(1, m+1):
    # A <= iでBが最大となるjを探す(使用済み除く)
    max_b = 0
    use_j = None
    for j in range(n):
        # print('i:{}, j:{}'.format(i, j))
        if a[j] <= i:
            if not used[j]:
                if b[j] > max_b:
                    max_b = b[j]
                    use_j = j
    if not use_j == None:
        used[use_j] = True
        sum += max_b

print(sum)
