N = int(input())
ans = 0
for visited in range(1, N):
    ans += N/(N-visited)
print(ans)