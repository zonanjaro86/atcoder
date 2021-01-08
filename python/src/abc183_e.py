mod = 10**9 + 7
H, W = map(int, input().split())
S = [input() for _ in range(H)]
'''
DP[y][x] := 点(0, 0)から(y, x)への移動方法の数
'''
DP = [[0] * W for _ in range(H)]
X = [[0] * W for _ in range(H)]
Y = [[0] * W for _ in range(H)]
Z = [[0] * W for _ in range(H)]
DP[0][0] = 1

for y in range(H):
    for x in range(W):
        if y == 0 and x == 0: continue
        if S[y][x] == '#': continue
        # 左
        if x > 0:
            X[y][x] = (X[y][x-1] + DP[y][x-1]) % mod
        # 上
        if y > 0:
            Y[y][x] = (Y[y-1][x] + DP[y-1][x]) % mod
        # 左上
        if x > 0 and y > 0:
            Z[y][x] = (Z[y-1][x-1] + DP[y-1][x-1]) % mod
        DP[y][x] = X[y][x] + Y[y][x] + Z[y][x]
print(DP[-1][-1] % mod)
