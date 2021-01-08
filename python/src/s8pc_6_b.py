N = int(input())
AB = [tuple(map(int, input().split())) for _ in range(N)]
A = [ab[0] for ab in AB]
B = [ab[1] for ab in AB]
A.sort()
B.sort()

s = A[N//2]
g = B[N//2]
ans = 0
for a, b in AB:
    ans += abs(s-a) + abs(b-a) + abs(g-b)
print(ans)