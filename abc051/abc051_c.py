# -*- coding: utf-8 -*-

sx,sy,tx,ty = map(int, input().split())
ans = ['U'] * (ty - sy) + ['R'] * (tx - sx)
ans += ['D'] * (ty - sy) + ['L'] * (tx - sx)
ans += ['L'] + ['U'] * (ty - sy + 1) + ['R'] * (tx - sx + 1) + ['D']
ans += ['R'] + ['D'] * (ty - sy + 1) + ['L'] * (tx - sx + 1) + ['U']
print(''.join(ans))