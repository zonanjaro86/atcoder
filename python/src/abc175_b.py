import itertools

n = int(input())
L = list(map(int, input().split()))
cnt = 0
for i, j, k in itertools.combinations(L, 3):
    if i == j or j == k or i == k:
        continue
    if i + j > k and j + k > i and k + i > j:
        cnt += 1
print(cnt)