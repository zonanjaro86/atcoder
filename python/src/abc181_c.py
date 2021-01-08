import itertools

def main(list):
    yes = False
    for (ax, ay), (bx, by), (cx, cy) in itertools.combinations(list, 3):

            if ax - bx == 0:
                if cx == ax:
                    yes = True
                    break
                continue

            # cy - ay = ((ay - by)/(ax - bx)) * (cx - ax)
            if ((ay - by)/(ax - bx)) * (cx - ax) - (cy - ay) == 0:
                yes = True
                break
    if yes:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    n = int(input())
    list = []
    for i in range(n):
        x, y = map(int, input().split())
        list.append((x, y))

    main(list)