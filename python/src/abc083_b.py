N, A, B = map(int, input().split())
ans = 0
for n in range(1, N+1):
    sum = 0
    for i in str(n):
        sum += int(i)
    if A <= sum <= B:
        ans += n
print(ans)
