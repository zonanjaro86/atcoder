# 保留

# from copy import deepcopy

# def dfs(r, c, table, cnt):
#     global cnt_max
#     table[r][c] = 0
#     for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
#         if table[r+dr][c+dc]:
#             dfs(r+dr, c+dc, deepcopy(table), cnt+1)
#     if table[r-1][c] == 0 and table[r+1][c] == 0 and table[r][c-1] == 0 and table[r][c+1] == 0:
#         cnt_max = max(cnt_max, cnt+1)

# if __name__ == "__main__":
#     m = int(input())
#     n = int(input())
#     table = [[0] * (m+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(n)] + [[0] * (m+2)]

#     cnt_max = 0
#     for i in range(1, n+1):
#         for j in range(1, m+1):
#             if table[i][j]:
#                 dfs(i, j, deepcopy(table), 0)
#     print(cnt_max)