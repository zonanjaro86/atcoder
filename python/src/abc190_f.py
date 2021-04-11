N = int(input())
a = tuple(map(int, input().split()))

cnt = 0
for i in range(N):
    for j in range(i+1, N):
        if a[i] > a[j]:
            cnt += 1
print(cnt)