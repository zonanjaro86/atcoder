A, B, W = map(int, input().split())
n_min = 1001
n_max = 0
can = False
for n in range(0, 1001):
    # n: みかんの個数
    if A * n <= W*1000 <= B * n:
        if n < n_min:
            n_min = n
        if n > n_max:
            n_max = n
        can = True
if can:
    print(n_min, n_max)
else:
    print('UNSATISFIABLE')
