# -*- coding: utf-8 -*-

n= int(input())

sum = 0

while (n > 0):
    n_len = len(str(n))
    cnt = n - 10 ** (n_len - 1) + 1

    if n_len % 2 == 1:
        sum += cnt

    n -= cnt

print(sum)

