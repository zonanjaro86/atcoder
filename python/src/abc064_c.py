N = int(input())
list = list(map(int, input().split()))

colors = set()
rainbow = 0
for a in list:
    color = a // 400
    if color >= 8:
        rainbow += 1
    else:
        colors.add(color)

if len(colors) == 0:
    print(1, rainbow)
else:
    print(len(colors), len(colors) + rainbow)