
n = int(input())
p = [tuple(map(int, input().split())) for _ in range(n)]
pset = set(p)

# n = 10
# p = list(tuple(map(int, i.split())) for i in """9 4
# 4 3
# 1 1
# 4 2
# 2 4
# 5 8
# 4 0
# 5 3
# 0 5
# 5 2""".split('\n'))
# p.sort()
# print(p)

ans = 0
for i in range(n-1):
    x1, y1 = p[i][0], p[i][1]
    for j in range(i+1, n):
        x2, y2 = p[j][0], p[j][1]
        vecx = x2 - x1
        vecy = y2 - y1
        x3, y3 = x1 - vecy, y1 + vecx
        x4, y4 = x2 - vecy, y2 + vecx
        if (x3, y3) in pset and (x4, y4) in pset:
            ans = max(ans, vecx**2 + vecy**2)
print(ans)

# max_area = 0
# for a, b in itertools.combinations(p, 2):
#     # print(a, b)
#     c = (b[0] - b[1] + a[1], b[1] + b[0] - a[0])
#     d = (a[0] - b[1] + a[1], a[1] + b[0] - a[0])
#     if c in p and d in p:
#         area = (b[0] - a[0])**2 + (b[1] - a[1])**2
#         max_area = max(area, max_area)
# print(max_area)