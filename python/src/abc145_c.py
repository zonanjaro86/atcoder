import itertools
import numpy as np

N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

sum = 90
d_route = []
for route in itertools.permutations(points):
    d = 0
    for i in range(1, N):
        d += ((route[i][0] - route[i-1][0])**2 + (route[i][1] - route[i-1][1])**2)**0.5
    d_route.append(d)
print(np.mean(d_route))