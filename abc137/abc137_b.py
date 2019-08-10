# -*- coding: utf-8 -*-

k, x = map(int, input().split())

min_x = max(x - k + 1, -1000000)

max_x = min(x + k - 1, 1000000)

ans = []
for i in range(min_x, max_x + 1):
    ans.append(str(i))

print(' '.join(ans))