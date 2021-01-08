# -*- coding: utf-8 -*-

N = int(input())

ans = float('inf')

a = 1
while a <= N**0.5:
    if N % a == 0:
        b = int(N/a)
        ans = min(ans, max(len(str(a)), len(str(b))))
    a += 1

print(ans)