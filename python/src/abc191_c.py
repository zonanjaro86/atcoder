H, W = map(int, input().split())
S = [input() for _ in range(H)]

ans = 0
for i in range(H-1):
    line_flag = False
    for j in range(W):
        if S[i][j] != S[i+1][j]:
            if line_flag == False:
                line_flag = True
        else:
            if line_flag == True:
                line_flag = False
                ans += 1
for j in range(W-1):
    line_flag = False
    for i in range(H):
        if S[i][j] != S[i][j+1]:
            if line_flag == False:
                line_flag = True
        else:
            if line_flag == True:
                line_flag = False
                ans += 1
print(ans)

