# -*- coding: utf-8 -*-

a, b, c = map(int, input().split())

ans = c - (a - b)
if ans < 0:
    ans = 0

print(ans)