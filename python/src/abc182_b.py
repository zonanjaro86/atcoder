N = int(input())
A = list(map(int, input().split()))

gcd_max = 1
ans = 0
for i in range(2, max(A) + 1):
    gcd = 0
    for a in A:
        if a % i == 0:
            gcd += 1
    if gcd >= gcd_max:
        gcd_max = gcd
        ans = i
print(ans)
