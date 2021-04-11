# TODO:後で直す
H, W, X, Y = map(int, input().split())
S = [input() for _ in range(H)]

ans = 1

Y_left = Y - 1
while Y_left > 0:
    if S[X-1][Y_left-1] == '#':
        break
    ans += 1
    Y_left -= 1

Y_right = Y + 1
while Y_right <= W:
    if S[X-1][Y_right-1] == '#':
        break
    ans += 1
    Y_right += 1

X_up = X - 1
while X_up > 0:
    if S[X_up-1][Y-1] == '#':
        break
    ans += 1
    X_up -= 1

X_down = X + 1
while X_down <= H:
    if S[X_down-1][Y-1] == '#':
        break
    ans += 1
    X_down += 1

print(ans)