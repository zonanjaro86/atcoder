N, W = map(int, input().split())
STP = [tuple(map(int, input().split())) for _ in range(N)]
usage = [0]*(2*(10**5)+1)
for S, T, P in STP:
    usage[S] += P
    usage[T] -= P
for i in range(1, len(usage)):
    usage[i] += usage[i-1]
if max(usage) > W:
    print("No")
else:
    print("Yes")


# STP = [(1, 3, 5), (2, 4, 4), (3, 10, 6), (2, 4, 1)]
# usage = [0]*11
# for S, T, P in STP:
#     usage[S] += P
#     usage[T] -= P
# print(usage)
# for i in range(len(usage)-1):
#     usage[i+1] += usage[i]
# print(usage)
