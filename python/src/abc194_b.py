N = int(input())
A, B, C = [],[],[]
for i in range(N):
    a, b = map(int, input().split())
    A.append((a, i))
    B.append((b, i))
    C.append(a+b)
A.sort()
B.sort()
if A[0][1] == B[0][1]:
    print(min(max(A[0][0], B[1][0]), max(A[1][0], B[0][0]), min(C)))
else:
    print(min(max(A[0][0], B[0][0]), min(C)))
