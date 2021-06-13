N = int(input())
A = tuple(map(int, input().split()))

import collections
a = collections.Counter(range(1, N+1))
b = collections.Counter(A)
if a == b:
    print('Yes')
else:
    print('No')