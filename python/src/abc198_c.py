R, X, Y = map(int, input().split())
dist = (X**2 + Y**2)**0.5
if dist%R == 0:
    print(int(dist//R))
elif dist < R:
    print(2)
else:
    print(int(dist//R + 1))