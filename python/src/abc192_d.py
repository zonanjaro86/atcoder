X = input()
M = int(input())

# Xをn進数として見たときの値を計算
def calc_nd(X, n):
    sum = 0
    for i, x in enumerate(X[::-1]):
        sum += int(x) * (n**i)
    return sum

d = int(max(X))

if len(X) == 1:
    # 何進数としても常に同じ値なので1種類、M超える場合は0
    ans = 1 if int(X) <= M else 0
else:
    # 何進数までならMを超えないかを二分探索
    left = 0
    right = M + 1
    while abs(left - right) > 1:
        mid = (left + right) // 2
        sum = calc_nd(X, mid)
        if sum > M:
            right = mid
        else:
            left = mid
    ans = max(0, left - d)
print(ans)