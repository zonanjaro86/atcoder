import itertools
import numpy as np

R, C = map(int, input().split())
a = np.array([list(map(int, input().split())) for _ in range(R)])

ans = 0
for iter in itertools.product([0, 1], repeat=R):
    b = a.copy()
    for i in range(R):
        if iter[i]:
            b[i] ^= 1
    col_sum = b.sum(axis=0)
    sum = 0
    for x in col_sum:
        sum += max(x, R - x)
    ans = max(ans, sum)

print(ans)