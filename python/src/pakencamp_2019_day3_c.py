def main(n, m, a):
    max_point = 0
    for i in range(m-1):
        for j in range(i+1, m):
            # Ti, Tjを歌う
            point = 0
            for s in range(n):
                point += max(a[s][i], a[s][j])
            max_point = max(point, max_point)
    print(max_point)

if __name__ == "__main__":
    n, m = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))

    main(n, m, a)