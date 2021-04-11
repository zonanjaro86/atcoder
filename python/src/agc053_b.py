N = int(input())
V = list(map(int, input().split()))


sum = 0
V1 = V[:N][::-1]
V2 = V[N:]
for i in range(N):
    sum += max(V1[i], V2[i])
print(sum)