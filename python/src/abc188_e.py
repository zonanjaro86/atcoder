# 解説確認済み
from collections import deque
from operator import itemgetter

N, M = map(int, input().split())
A = list(map(int, input().split()))

edges = [deque() for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)

# 各町で売ったときの売上の最大値を格納
sales = {}

for start, buy in sorted(enumerate(A), key=itemgetter(1)):
    # 金額の小さな町から順に、行ける町を探索し売上を計算する
    d = deque([start])
    while(d):
        i = d.popleft()
        for j in edges[i]:
            # 未訪問の場合のみ、金額の計算とキューへ追加
            if not j in sales.keys():
                d.append(j)
                sales[j] = A[j] - buy
print(max(sales.values()))