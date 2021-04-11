S = input()

# 連続する2文字をサーチする
# 2文字以上連続する場合は最後の2文字
# その2文字の次の文字のインデックスを格納しておく
idx = []
same_char = ''
same_flg = False
for i in range(1, len(S)):
    if S[i] == S[i-1]:
        same_flg = True
    else:
        if same_flg:
            same_flg = False
            idx.append(i)

# print(idx)
idx.append(len(S))
excludes = []
# 連続する文字の次の区間まで、同じ文字が出ないかカウントする
# 次の連続する文字が同じの場合はその後ろも全て除外する
for i in range(len(idx)-1):
    a = idx[i]
    b = idx[i+1]
    exclude = S[a:b].count(S[a-1])
    if S[a-1] == S[b-1]:
        exclude += len(S) - b
    excludes.append(exclude)
# print(excludes)
ans = 0
for i in range(len(idx)-1):
    ans += len(S) - idx[i] - excludes[i]
print(ans)