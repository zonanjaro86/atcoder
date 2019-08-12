# -*- coding: utf-8 -*-

from heapq import heappush, heappop

n, m = map(int, input().split())

# A日後、報酬B
# 日付ごとに報酬をリスト化
workList = {}
for i in range(n):
    a, b = map(int, input().split())
    if a not in workList:
        workList[a] = [b]
    else:
        workList[a].append(b)

hq = []
sum = 0
for i in range(1, m + 1):
    # 日付が短い順にheapに追加
    # 最大値を取り出すため正負は逆に
    if i in workList:
        for w in workList[i]:
            heappush(hq, -w)

    # 最大値を取り出し、正負を戻して加算
    if len(hq) > 0:
        val = heappop(hq)
        sum += -val

print(sum)
