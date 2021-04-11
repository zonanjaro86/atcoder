N = int(input())
A = tuple(map(int, input().split()))

from collections import Counter
import itertools
count = Counter(A)
AA = [0] * 401
for a, b in itertools.combinations(range(-200, 201), 2):
    if count[a] and count[b]:
        AA[abs(a-b)] += count[a] * count[b]

AAA = [i**2 for i in range(401)]
sum = 0
for i, cnt in enumerate(AA):
    sum += AAA[i] * cnt
print(sum)