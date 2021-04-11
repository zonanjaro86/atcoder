def main():
    N = int(input())
    t, x, y = 0, 0, 0
    for _ in range(N):
        nt, nx, ny = map(int, input().split())
        d = abs(nx - x) + abs(ny - y)
        dt = nt - t
        if d > dt or d % 2 != dt % 2:
            print('No')
            return
        else:
            t, x, y = nt, nx, ny
    print('Yes')
main()