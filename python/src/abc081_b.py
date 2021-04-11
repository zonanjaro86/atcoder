N = int(input())
A = list(map(int, input().split()))
flg = True
cnt = 0
while flg:
    for i in range(N):
        if A[i] % 2 == 0:
            A[i] = A[i]//2
        else:
            flg = False
            break
    if flg:
        cnt += 1
print(cnt)