# 解説確認済み
X, Y = map(int, input().split())
memo = {}
# YをXにする操作で考える
def calc(y):
    '''
    yをXにするのに必要な回数を返す
    '''
    global memo, X
    if y <= X:
        return abs(X - y)
    elif y in memo.keys():
        return memo[y]
    elif y == 1:
        memo[y] = X - y
    elif y % 2 == 1:
        a = abs(X - y)
        b = calc((y+1)/2) + 2
        c = calc((y-1)/2) + 2
        memo[y] = min(a, b, c)
    else:
        a = abs(X - y)
        b = calc(y/2) + 1
        memo[y] = min(a, b)
    return memo[y]
print(int(calc(Y)))