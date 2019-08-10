# -*- coding: utf-8 -*-

N = int(input())

dict = {}
for i in range(N):
    s = ''.join(sorted(input()))
    if s in dict:
        dict[s] += 1
    else:
        dict[s] = 1


sum = 0
list1 = list(dict.values())
for i in list1:
    sum += int(i * (i-1) / 2)

print(sum)
