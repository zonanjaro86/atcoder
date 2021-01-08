# TLE
# import numpy as np

# H, W, N, M = map(int, input().split())
# AB = [tuple(map(int, input().split())) for _ in range(N)]
# CD = [tuple(map(int, input().split())) for _ in range(M)]

# '''
# -1: ブロック
#  0: 暗い
# 1>: 明るい
# '''
# room = np.array([[-1] * (W + 2)] + [[-1] + [0] * W + [-1] for _ in range(H)] + [[-1] * (W + 2)])
# for C, D in CD:
#     room[C][D] = -1

# room_row = np.copy(room)
# room_col = np.copy(room)

# for A, B in AB:
#     room_row[A][B] = 1
#     # 横方向
#     for j in reversed(range(1, B)):
#         if room_row[A][j] == 0:
#             room_row[A][j] = 1
#         else:
#             break
#     for j in range(B+1, W+2):
#         if room_row[A][j] == 0:
#             room_row[A][j] = 1
#         else:
#             break
#     # 縦方向
#     for i in reversed(range(1, A)):
#         if room_col[i][B] == 0:
#             room_col[i][B] = 1
#         else:
#             break
#     for i in range(A+1, H+2):
#         if room_col[i][B] == 0:
#             room_col[i][B] = 1
#         else:
#             break

# print(np.count_nonzero(room_col + room_row > 0))

