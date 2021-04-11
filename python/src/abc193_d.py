# スコアの計算
def score(str):
    a = [0] * 10
    for s in str:
        a[int(s)] += 1
    score = 0
    for i in range(1, 10):
        score += i * 10 ** a[i]
    return score

def main():
    K = int(input())
    S = input()
    T = input()

    # 山札の各数字の残り枚数
    rest = [K] * 10
    for i in range(4):
        rest[int(S[i])] -= 1
        rest[int(T[i])] -= 1

    # 勝ちパターンを計算
    cnt = 0
    for i in range(1, 10):
        s_score = score(S[:4] + str(i))
        for j in range(1, 10):
            t_score = score(T[:4] + str(j))
            if s_score > t_score:
                if i == j:
                    cnt += rest[i] * (rest[i] - 1)
                else:
                    cnt += rest[i] * rest[j]

    # 全パターンで割って確率を計算
    total = (9 * K - 8) * (9 * K - 9)
    print(cnt / total)

if __name__ == '__main__':
    main()