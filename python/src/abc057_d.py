from operator import mul
from functools import reduce

def combinations_count(n, r):
    r = min(r, n-r)
    numer = reduce(mul, range(n, n-r, -1), 1)
    denom = reduce(mul, range(1, r+1), 1)
    return numer // denom

n, a, b = map(int, input().split())
v = list(map(int, input().split()))
# n, a, b = map(int, "4 2 3".split())
# v = list(map(int, "10 10 10 10".split()))



# 大きい順にa個選ぶのが最大
# 最後に選んだものと同じものが残っているならその数だけ選び方がある

v.sort()
v.reverse()

va = v[:a]
vb = v[a:]
# print(va, vb)

ave = sum(va)/a
print("{:.6f}".format(ave))

ca = va.count(va[-1])
cb = vb.count(va[-1])
# print(ca, cb)

sum = 0
for i in range(ca, b):
    sum += combinations_count(ca+cb, i)
print(sum)

