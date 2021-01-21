N = int(input())
A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))
sum = 0
for i in range(N):
    sum += A[i] * B[i]
if sum == 0:
    print("Yes")
else:
    print("No")