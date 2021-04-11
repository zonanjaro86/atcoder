import math

N = int(input())
p0 = tuple(map(int, input().split()))
pN2 = tuple(map(int, input().split()))

# 中点の座標
M = ((p0[0] + pN2[0])/2, (p0[1] + pN2[1])/2)

# 中点からみたx0のベクトル
v0 =(p0[0] - M[0], p0[1] - M[1])

# 2π/N度回転する
sin = math.sin(math.radians(360/N))
cos = math.cos(math.radians(360/N))
v1 = (v0[0]*cos - v0[1]*sin, v0[0]*sin + v0[1]*cos)

# 座標に戻す
p1 = (M[0] + v1[0], M[1] + v1[1])
print(*p1)