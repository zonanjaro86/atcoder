N = int(input())
A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))

left = 1
right = 1000
for i in range(N):
    left = max(left, A[i])
    right = min(right, B[i])
print(max(right - left + 1, 0))