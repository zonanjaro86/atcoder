import itertools

def main():
    N = int(input())
    P = [tuple(map(int, input().split())) for _ in range(N)]

    if len(P) < 2:
        print(0)
        return
    cnt = 0
    for (x1, y1), (x2, y2) in itertools.combinations(P, 2):
        if x1 == x2: continue
        if -1 <= (y2 - y1) / (x2 - x1) <= 1:
            cnt += 1
    print(cnt)

if __name__ == "__main__":
    main()