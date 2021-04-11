N, K = map(int, input().split())
def f(x):
    n = str(x)
    g2 = int(''.join(sorted(n)))
    g1 = int(''.join(sorted(n, reverse=True)))
    return g1 - g2
for i in range(K):
    N = f(N)
print(N)