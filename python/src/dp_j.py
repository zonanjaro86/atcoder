import sys
sys.setrecursionlimit(1000000)

N = int(input())
a = tuple(map(int, input().split()))

# dp[c1][c2][c3]: 1個の皿がc1枚、2個の皿がc2枚、3個の皿がc3枚あるときの全て食べるまでの操作の期待値
dp = [[[-1] * (N+1) for _ in range(N+1)] for _ in range(N+1)]
dp[0][0][0] = 0

def f(c1, c2, c3):
    if dp[c1][c2][c3] >= 0:
        return dp[c1][c2][c3]

    count = N

    if c1 > 0:
        count += f(c1-1, c2, c3) * c1
    if c2 > 0:
        count += f(c1+1, c2-1, c3) * c2
    if c3 > 0:
        count += f(c1, c2+1, c3-1) * c3
    count /= (c1+c2+c3)

    dp[c1][c2][c3] = count
    return count

print(f(a.count(1), a.count(2), a.count(3)))