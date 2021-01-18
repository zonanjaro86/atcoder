import collections
N, K = map(int, input().split())
a = list(map(int, input().split()))
c = collections.Counter(a)
ans = 0
max_a = max(a)
for k in range(K):
    for i in range(max_a+2):
        if c[i] > k:
            pass
        else:
            max_a = i-1
            ans += i
            break
print(ans)



