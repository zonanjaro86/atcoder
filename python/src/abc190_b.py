def main():
    N, S, D = map(int, input().split())
    magics = [tuple(map(int, input().split())) for _ in range(N)]

    for X, Y in magics:
        if X < S and Y > D:
            print('Yes')
            return
    print('No')
main()