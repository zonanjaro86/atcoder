N, X = map(int, input().split())
A = list(map(int, input().split()))
B = []
for a in A:
    if a != X:
        B.append(a)
print(*B)
