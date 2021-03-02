from collections import Counter

K = int(input())
S = input()
T = input()

s_cnt = Counter(S[:4])
t_cnt = Counter(T[:4])

# 裏向きのカードを除いた各数字の点数
s_base = [i * 10 ** s_cnt[str(i)] for i in range(1, 10)]
t_base = [i * 10 ** t_cnt[str(i)] for i in range(1, 10)]

# 裏向きのカードが1～9のときの合計点数
s_point = [sum(s_base) + s_base[i-1]*9 for i in range(1, 10)]
t_point = [sum(t_base) + t_base[i-1]*9 for i in range(1, 10)]

# 裏向きのカードを除いた各数字の残り枚数
c = Counter({'1': K, '2': K, '3': K, '4': K, '5': K, '6': K, '7': K, '8': K, '9': K}) - s_cnt - t_cnt
# print(c)
# 2 * K - 8

p_win = 0
for i in range(1, 10):
    if c[str(i)] == 0:
        continue
    for j in range(1, 10):
        # もう残ってない場合は無視
        if c[str(i)] == 0 or c[str(j)] == 0:
            continue
        # 残り一枚で同じ数字を引いた場合も無視
        if i == j and c[str(i)] <= 1:
            continue
        # このパターンにたどり着く場合の数
        p = c[str(i)] * c[str(j)] if i != j else c[str(i)] * (c[str(i)]-1)
        # 勝ち負け判定
        if s_point[i-1] > t_point[j-1]:
            p_win += p

print(p_win / ((9*K-8)*(9*K-9)))