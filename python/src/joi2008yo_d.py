m = int(input())
A = [tuple(map(int, input().split())) for _ in range(m)]
n = int(input())
B = [tuple(map(int, input().split())) for _ in range(n)]

# A = [
#     (8, 5),
#     (6, 4),
#     (4, 3),
#     (7, 10),
#     (0, 10)
# ]
# B = [
#     (10, 5),
#     (2, 7),
#     (9, 7),
#     (8, 10),
#     (10,2),
#     (1, 2),
#     (8, 1),
#     (6, 7),
#     (6, 0),
#     (0, 9)
# ]

vec = []
for i in range(1, len(A)):
    vec.append((A[i][0]-A[0][0], A[i][1]-A[0][1]))
for x, y in B:
    ok = True
    for vecx, vecy in vec:
        if (x + vecx, y + vecy) not in B:
            ok = False
    if(ok):
        print(x - A[0][0], y - A[0][1])
        break



