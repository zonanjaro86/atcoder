r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

def ok(a, b, c, d):
    return a+b == c+d or a-b == c-d or abs(a-c) + abs(b-d) <= 3

# 最大三手で必ずいける
if r1==r2 and c1==c2:
    print(0)
elif r1+c1 == r2+c2 or r1-c1 == r2-c2 or abs(r1-r2) + abs(c1-c2) <= 3:
    print(1)
elif (r1+r2+c1+c2)%2 == 0\
    or abs(r1-r2) + abs(c1-c2) <= 6\
    or r2-r1+3 >= c2-c1 and r2-r1-3 <= c2-c1\
    or r2-r1+3 >= c1-c2 and r2-r1-3 <= c1-c2:
    print(2)
else:
    print(3)