K = int(input())

ans = 0
for A in range(1, K+1):
    for B in range(A, K+1):
        if A * B > K or K//(A*B) < B:
            break
        for C in range(B, K//(A*B)+1):
            if A == B and B == C:
                ans += 1
            elif A == B or B == C or C == A:
                ans += 3
            else:
                ans += 6
print(ans)
