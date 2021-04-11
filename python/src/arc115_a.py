"""
https://atcoder.jp/contests/arc115/tasks/arc115_a
あとでやる

"""
import itertools

N, M = map(int, input().split())
S = [input() for _ in range(N)]

# TLE
# ans = 0
# for s1, s2 in itertools.combinations(S, 2):
#     cnt = 0
#     for i in range(M):
#         if s1[i] != s2[i]:
#             cnt += 1
#     if cnt % 2 > 0:
#         ans += 1
# print(ans)

# S_bit = [int(s, 2) for s in S]
# ans = 0
# for s1, s2 in itertools.combinations(S_bit, 2):
#     # XORをとり1の数を数える
#     bin_num = bin(s1^s2)[2:]
#     count = 0
#     for i in bin_num:
#         count += int(i)
#     if count % 2 > 0:
#         ans += 1
# print(ans)
