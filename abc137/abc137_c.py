# -*- coding: utf-8 -*-

N = int(input())

# それぞれの文字が何回現れたかを格納する
dict = {}

ans = 0
for i in range(N):
    s = ''.join(sorted(input()))

    # すでに出現していればこれまでに出現した回数を答えに足す
    if s in dict:
        ans += dict[s]
        dict[s] += 1

    # 1回も出現していなければ追加する
    else:
        dict[s] = 1

print(ans)
