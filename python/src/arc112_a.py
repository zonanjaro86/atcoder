T = int(input())
cases = [tuple(map(int, input().split())) for _ in range(T)]

for L, R in cases:
    if L * 2 > R:
        print(0)
    else:
        n = R - L - L + 1
        print(int(n*(n+1)/2))
