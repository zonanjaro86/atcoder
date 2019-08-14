# -*- coding: utf-8 -*-

n= int(input())

sum = 0

i = 0
while True:
    min = 10 ** i
    max = 10 ** (i+1) - 1

    if n < min:
        break
    elif n < max:
        max = n

    sum += max - min + 1
    i += 2

print(sum)

