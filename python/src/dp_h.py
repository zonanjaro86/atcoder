H, W = map(int, input().split())
a = ['#'* (W+1)] + ['#' + input() for _ in range(H)]

mod = 10**9+7

# m[i][j]: 点(i, j)への経路 mod 10**9+7
m = [[0] * (W+1) for _ in range(H+1)]
m[0][1] = 1

for i in range(1, H+1):
    for j in range(1, W+1):
        if a[i][j] == '#':
            continue
        m[i][j] = (m[i-1][j] + m[i][j-1]) % mod
print(m[H][W])