# AC PyPy3
# TLE Python

N = int(input())
A = tuple(map(int, input().split()))

ans = 2**30 + 1
# 分け方は2**(N-1)通り
for i in range(2**(N-1)):
    i = bin(i)[2:]
    i = i.zfill(N-1)
    ref = 0
    temp = A[0]
    for j in range(N-1):
        if i[j] == '0':
            temp = temp|A[j+1]
        else:
            ref = ref^temp
            temp = A[j+1]
    ref = ref^temp
    ans = min(ans, ref)
print(ans)

