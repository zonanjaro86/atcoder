import itertools

def solve():
    S1 = input()
    S2 = input()
    S3 = input()

    # ユニーク文字のリスト
    chars = list(set([*S1, *S2, *S3]))
    # 0-9のリスト
    numbers = list(map(str,range(0,10)))

    # 文字の種類が10種類を超える場合は不可
    if len(chars) > 10:
        print('UNSOLVABLE')
        return

    # どの文字列に何の数字を割り当てたか場合分け
    for nums in itertools.permutations(numbers,len(chars)):
        N1 = ''.join([nums[chars.index(s)] for s in S1])
        N2 = ''.join([nums[chars.index(s)] for s in S2])
        N3 = ''.join([nums[chars.index(s)] for s in S3])

        # 先頭が0の場合は無視
        if N1[0] == '0' or N2[0] == '0' or N3[0] == '0':
            continue

        # N3 = N1 + N2 を満たすものが答え
        if int(N3) == int(N1) + int(N2):
            print(N1)
            print(N2)
            print(N3)
            return

    # 満たすものが無かった場合
    print('UNSOLVABLE')

solve()