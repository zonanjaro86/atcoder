N = int(input())
balls = [tuple(map(int, input().split())) for _ in range(N)]
X, C = zip(*balls)
C_max = max(C)

# dp[i][x]: i色のボールまで取りきって、左端(x=0)か右端(x=1)かにいるときの最小経過時間
dp = [[-1]*2 for _ in range(C_max+1)]
dp[0][0] = 0
dp[0][1] = 0
left = 0
right = 0
for i in range(C_max):
    temp = []
    for j in range(N):
        if C[j] == i+1:
            temp.append(X[j])
    if len(temp) == 0:
        dp[i+1][0] = dp[i][0]
        dp[i+1][1] = dp[i][1]
    else:
        x_min = min(temp)
        x_max = max(temp)
        mid = (left + right) // 2
        if x_min <= mid:
            dp[i+1][0] = dp[i][1] + (right - left) + abs(x_min - left)
        else:
            dp[i+1][0] = dp[i][0] + (right - left) + abs(x_min - right)
        if x_max <= mid:
            dp[i+1][1] = dp[i][1] + (right - left) + abs(x_max - left)
        else:
            dp[i+1][1] = dp[i][0] + (right - left) + abs(x_max - right)
        left = x_min
        right = x_max
print(dp, left, right)