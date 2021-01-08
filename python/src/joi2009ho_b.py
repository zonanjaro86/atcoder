from bisect import bisect_left

d = [int(input())]
n = int(input())
m = int(input())
d = [0] + [int(input()) for _ in range(n-1)] + d
k = [int(input()) for _ in range(m)]

d.sort()

ans = 0
for ki in k:
    i = bisect_left(d, ki)
    ans += min(abs(d[i] - ki), abs(ki - d[i-1]))
print(ans)


# def get_min_d(d, k):
#     s = 0
#     t = len(d)
#     while True:
#         i = (s + t) // 2
#         if k > d[i]:
#             s = i
#         elif k < d[i-1]:
#             t = i
#         else:
#             return min(d[i] - k, k - d[i-1])

# ans = 0
# for ki in k:
#     ans += get_min_d(d, ki)
# print(ans)

