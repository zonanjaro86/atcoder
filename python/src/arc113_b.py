A, B, C = map(int, input().split())
mods = [
    [0],
    [1],
    [6, 2, 4, 8],
    [1, 3, 9, 7],
    [6, 4],
    [5],
    [6],
    [1, 7, 9, 3],
    [6, 8, 4, 2],
    [1, 9]
]

def power_func(a,n,p):
    bi = str(format(n,"b"))
    res = 1
    for i in range(len(bi)):
        res = (res*res) %p
        if bi[i] == "1":
            res = (res*a) %p
    return res

A_mods = mods[A%10]
n = len(A_mods)

if n == 1:
    print(A_mods[0])
else:
    print(A_mods[power_func(B, C, n)])