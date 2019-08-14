# -*- coding: utf-8 -*-
S= list(input())

isR = True
cnt_tmp = 0
cntList = []
for s in S:
    if s == 'R':
        if isR:
            cnt_tmp += 1
        else:
            cntList.append(cnt_tmp)
            isR = True
            cnt_tmp = 1
    else:
        if isR:
            cntList.append(cnt_tmp)
            isR = False
            cnt_tmp = 1
        else:
            cnt_tmp += 1

cntList.append(cnt_tmp)

ans = []

for i,cnt in enumerate(cntList):
    if i % 2 == 0:
        # R
        ans += [0] * (cnt - 1)
        q, mod = divmod(cnt, 2)
        ans += [q+mod, q]
    else:
        #L
        q, mod = divmod(cnt, 2)
        ans[len(ans)-2] += q
        ans[len(ans)-1] += (q+mod)
        ans += [0] * (cnt - 1)

print(' '.join([str(n) for n in ans]))