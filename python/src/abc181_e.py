# TLE
def main(H, W):
    ans = 2 * 10**5
    for w in W:
        list = H + [w]
        list.sort()

        ans = min(sum(list[1::2]) - sum(list[::2]), ans)
    print(ans)

if __name__ == '__main__':
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    w = list(map(int, input().split()))
    main(h, w)