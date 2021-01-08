N = int(input())
A = list(map(int, input().split()))

current = 0 # 前ステップ終了後の座標
sumA = 0 # A[i]までの合計
max_step = 0 # ステップ内で最も右に移動するときの距離
ans = 0
for a in A:
    sumA += a
    max_step = max(max_step, sumA)
    ans = max(ans, current + max_step)
    current += sumA
print(ans)