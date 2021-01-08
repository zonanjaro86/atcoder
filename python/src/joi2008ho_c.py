import itertools
from bisect import bisect_left

N, M = map(int, input().split())
P = [int(input()) for _ in range(N)]

# N, M = 4, 50
# P = [3, 14, 15, 9]

P = [0] + P
points = sorted([sum(iter) for iter in itertools.combinations_with_replacement(P, 2)])
ans = 0
for p in points:
    i = bisect_left(points, M-p)
    if i > 0 and p + points[i-1] <= M:
        ans = max(ans, p + points[i-1])
print(ans)

# TLE
# P = [0] + P
# points = sorted([M - sum(iter) for iter in itertools.combinations_with_replacement(P, 3)])
# print(M - min([points[bisect_left(points, p)] - p for p in P]))


# TLE
# P = [0] + P
# points = max(sum(iter) for iter in itertools.combinations_with_replacement(P, 4) if sum(iter) <= M)
# print(points)