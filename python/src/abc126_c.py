N, K = map(int, input().split())
sum = 0
for n in range(1, N+1):
    num = n
    p = 1
    while num < K:
        num *= 2
        p *= (1/2)
    sum += p
print(sum/N)