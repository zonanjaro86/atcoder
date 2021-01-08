# -*- coding: utf-8 -*-
n= int(input())
h = [int(s) for s in input().split()]

yes = True
for i in reversed(range(len(h))):
    if i == len(h)-1:
        continue
    if h[i] <= h[i+1]:
        pass
    elif h[i] == h[i+1] + 1:
        h[i] -= 1
    else:
        yes = False
        break

if yes:
    print('Yes')
else:
    print('No')