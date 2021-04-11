N, M = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(M)]
K = int(input())
CD = [tuple(map(int, input().split())) for _ in range(K)]

ans = 0
for i in range(2**K):
    dishes = [0] * N
    for j in range(K):
        if ((i >> j) & 1):
            dishes[CD[j][0]-1] = 1
        else:
            dishes[CD[j][1]-1] = 1
    cnt = 0
    for A, B in AB:
        if dishes[A-1] and dishes[B-1]:
            cnt += 1
    ans = max(cnt, ans)
print(ans)