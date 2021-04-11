R, X, Y = map(int, input().split())
dist = (X**2 + Y**2)**0.5
if dist%R == 0:
    print(int(dist//R))
else:
    ans = int(dist//R + 1)
    if ans == 1:
        ans = 2
    print(ans)