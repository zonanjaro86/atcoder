A = int(input())
B = int(input())
C = int(input())
X = int(input())
cnt = 0
for a in range(A+1):
    for b in range(B+1):
        c = (X - 500*a - 100*b) // 50
        if 0 <= c <= C:
            cnt += 1
print(cnt)