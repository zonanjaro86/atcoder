N = int(input())
S = input()
A = list(map(int, input().split()))

# k = min([abs(A[i] - A[i+1]) for i in range(N)])

B = [0] * (N+1)
for i in range(N):
    if S[i] == '<':
        B[i+1] = B[i] + 1

for i in range(N-1, -1, -1):
    if S[i] == '>':
        B[i] = max(B[i], B[i+1] + 1)

k = 1
while True:
    for i in range(N+1):
        A[i] -= B[i]
    if all([A[i] < A[i+1] for i in range(N) if S[i] == '<']) and all([A[i] > A[i+1] for i in range(N) if S[i] == '>']):
        k += 1
        continue
    else:
        for i in range(N+1):
            A[i] += B[i]
        break

print(k)
print(*A)
for _ in range(k-1):
    print(*B)


