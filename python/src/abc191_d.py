import math
X, Y, R = map(float, input().split())
# ans = 0
# top = math.floor(Y + R)
# bottom = math.ceil(Y - R)
# for y in range(bottom, top + 1):
#     Rcos = math.sqrt(R**2 - (y-Y)**2)
#     left = math.ceil(X - Rcos)
#     right = math.floor(X + Rcos)
#     if left <= right:
#         ans += right - left + 1
# print(ans)

def getCeilFloor(x, r):
    low = math.ceil(x - r)
    high = math.floor(x + r)
    return (low, high)

num = 0
start, end = getCeilFloor(X, R)
if start <= end:
    for i in range(start, end + 1):
        p = math.sqrt(R**2 - (X - i)**2)
        bottom, top = getCeilFloor(Y, p)
        num += max(0, top - bottom + 1)
print(num)

