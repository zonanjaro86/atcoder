import itertools

S1 = input()
S2 = input()
S3 = input()

chars = list(set([*S1, *S2, *S3]))
numbers = list(map(str,range(0,10)))

# 文字の種類が10種類を超える場合は不可
if len(chars) > 10:
    print('UNSOLVABLE')
else:
    is_solve = False
    for nums in itertools.permutations(numbers,len(chars)):
        N1 = ''.join([nums[chars.index(s)] for s in S1])
        N2 = ''.join([nums[chars.index(s)] for s in S2])
        N3 = ''.join([nums[chars.index(s)] for s in S3])

        # N3 = N1 + N2 を満たすか
        if int(N3) != int(N1) + int(N2):
            continue

        # 先頭に無駄な0がないか
        if N1[0] == '0' or N2[0] == '0' or N3[0] == '0':
            continue

        is_solve = True
        print(N1)
        print(N2)
        print(N3)
        break
    if not is_solve:
        print('UNSOLVABLE')
