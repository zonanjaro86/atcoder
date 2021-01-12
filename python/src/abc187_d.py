# https://atcoder.jp/contests/abc187/editorial/486
# AC

N = int(input())

X = 0
x = []
for _ in range(N):
    A, B = map(int, input().split())
    X -= A
    x.append(A*2+B)
x.sort()
ans = 0
while X <= 0:
    X += x.pop()
    ans += 1
print(ans)
