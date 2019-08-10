# -*- coding: utf-8 -*-

a, b = map(int, input().split())

sum = a + b
sub = a - b
kake = a * b

print(max(sum, sub, kake))