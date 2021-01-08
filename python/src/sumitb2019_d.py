N = int(input())
S = input()

cnt = 0
for i in range(0, 1000):
    pin = str(i).zfill(3)
    idx1 = S.find(pin[0])
    if idx1 < 0: continue
    idx2 = S.find(pin[1], idx1+1)
    if idx2 < 0: continue
    idx3 = S.find(pin[2], idx2+1)
    if idx3 < 0:continue
    cnt += 1
print(cnt)

# TLE
# pin = set()
# # 真ん中を選び左右の重複を無くして場合わけ
# for i in range(1, N-1):
#     s2 = S[i]
#     left = set(list(S[:i]))
#     right = set(list(S[i+1:]))
#     for s1 in left:
#         for s3 in right:
#             pin.add(s1 + s2 + s3)
# print(len(pin))

# TLE
# pin = set()
# for i in range(N-2):
#     for j in range(i+1, N-1):
#         for k in range(j+1, N):
#             pin.add(S[i] + S[j] + S[k])
# print(len(pin))