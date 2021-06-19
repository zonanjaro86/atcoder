N = int(input())
A = tuple(map(int, input().split()))
import collections
ans = 0
cnt = collections.Counter()
for i in range(N):
    if i > 0:
        ans += i - cnt[A[i]]
    cnt[A[i]] += 1
print(ans)