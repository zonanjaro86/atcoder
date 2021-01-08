import math

P = float(input())

"""
x年後に計算を始めた場合のかかる時間は
x + P/(2**(x/1.5))
"""

def f(x):
    return x + P/(2**(x/1.5))

low = 0
high = 1000
for _ in range(500):
    c1 = (high - low)/3 + low
    c2 = (high - low)*2/3 + low
    if (f(c1) >= f(c2)):
        low = c1
    else:
        high = c2
print(f(high))
