N, Q = map(int, input().split())

A = tuple(map(int, input().split()))
B = []
B.append(A[0]-1)
for i in range(1, N):
    B.append(B[-1] + A[i] - A[i-1] - 1)

for _ in range(Q):
    K = int(input())
    # flg = True
    # for i in range(N):
    #     if K <= B[i]:
    #         print(A[i] - (B[i] - K + 1))
    #         flg = False
    #         break
    # if flg:
    #     print(A[-1] + (K - B[-1]))
    left = 0
    right = N
    while abs(left - right) > 1:
        mid = (left + right) // 2
        if K <= B[mid]:
            right = mid
        else:
            left = mid
    if K <= B[left]:
        print(A[left] - (B[left] - K + 1))
    elif right < N:
        print(A[right] - (B[right] - K + 1))
    else:
        print(A[-1] + (K - B[-1]))


