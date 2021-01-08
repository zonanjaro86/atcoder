N = [int(n) for n in input()]

def calc():
    if sum(N) % 3 == 0:
        return 0

    # sum(N)が3k+1なら3k+1を1つor3k+2を2つ消す
    # sum(N)が3k+2なら3k+1を2つor3k+1を2つ消す
    cnt3k1 = 0
    cnt3k2 = 0
    for n in N:
        if n % 3 == 1: cnt3k1 += 1
        elif n % 3 == 2: cnt3k2 += 1

    if sum(N) % 3 == 1:
        # delete 1 of 3k+1 or 2 of 3k+2 (k = 0, 1, 2...)
        if cnt3k1 >= 1 and len(N) > 1:
            return 1
        elif cnt3k2 >= 2 and len(N) > 2:
            return 2
        else:
            return -1

    elif sum(N) % 3 == 2:
        # delete 1 of 3k+2 or 2 of 3k+1 (k = 0, 1, 2...)
        if cnt3k2 >= 1 and len(N) > 1:
            return 1
        elif cnt3k1 >= 2 and len(N) > 2:
            return 2
        else:
            return -1
    return -1

if __name__ == "__main__":
    print(calc())
