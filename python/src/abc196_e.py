import numpy as np

N = int(input())
at = [tuple(map(int, input().split())) for _ in range(N)]
A, T = zip(*at)
Q = int(input())
X = tuple(map(int, input().split()))

def f(x, a, t):
    if t == 1:
        return x + a
    elif t == 2:
        return max(x, a)
    else:
        return min(x, a)

def fs(x):
    ans = x
    for i in range(N):
        ans = f(ans, A[i], T[i])
    return ans

max_x = 10**9
min_x = -10**9
dx = 0
for i in range(N):
    if T[i] == 1:
        max_x += A[i]
        min_x += A[i]
        dx += A[i]
    elif T[i] == 2:
        max_x = max(max_x, A[i])
        min_x = max(min_x, A[i])
    else:
        max_x = min(max_x, A[i])
        min_x = min(min_x, A[i])


ori_max_x = max_x - dx
ori_min_x = min_x - dx

for x in X:
    if x >= ori_max_x:
        print(max_x)
    elif x <= ori_min_x:
        print(min_x)
    else:
        print(x + dx)