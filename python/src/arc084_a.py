from bisect import bisect_right, bisect_left

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()
B.sort()
C.sort()

ans = 0
for b in B:
    i = bisect_left(A, b)
    j = bisect_right(C, b)
    ans += i * (len(C)-j)
print(ans)

# TLE
# ans = 0
# for a in A:
#     i = bisect_right(B, a)
#     for b in B[i:]:
#         j = bisect_right(C, b)
#         ans += len(C[j:])
# print(ans)