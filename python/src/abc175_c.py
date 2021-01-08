
x, k, d = -10, 1, 2
# x, k, d = map(int, input().split())

if x < 0:
    x, d = -x, -d

k1 = x//abs(d)
if k <= k1:
    y = x - k * d
else:
    k -= k1
    y = x - k1 * d
    if k % 2 == 1:
        y -= d
print(y)
