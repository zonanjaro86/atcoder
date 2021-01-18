N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_max = 0
ans = 0
for n in range(N):
    a_max = max(a_max, a[n])
    ans = max(a_max*b[n], ans)
    print(ans)
