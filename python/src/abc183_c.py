import itertools

N, K = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]
# 都市1以外の都市を訪問する順番は(N-1)!通り
ans = 0
for route in itertools.permutations(range(1, N)):
    i = 0
    time = 0
    for j in route:
        time += T[i][j]
        i = j
    time += T[i][0]
    if time == K:
        ans += 1
print(ans)