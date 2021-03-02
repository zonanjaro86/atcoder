def gcd(m, n):
    while n:
        m, n = n, m % n
    return m

def extgcd(a, b):
    if b:
        d, y, x = extgcd(b, a % b)
        y -= (a // b) * x
        return d, x, y
    return a, 1, 0

def crt(a, b, mod1, mod2):
    # px + qy = d = gcd(p, q)
    d, p, _ = extgcd(mod1, mod2)
    if (b - a) % d != 0:
        return -1, 0
    lcm = mod1 * (mod2 // d)
    r = a + mod1 * ((b - a) // d) * p
    r %= lcm
    # print('a:{}, b:{}, mod1:{}, mod2:{}'.format(a, b, mod1, mod2))
    # print('r:{}, lcm:{}'.format(r, lcm))
    return r, lcm


def solve():
    X, Y, P, Q = map(int, input().split())

    ans = float("inf")
    for t1 in range(X, X+Y):
        for t2 in range(P, P+Q):
            # t = t1 mod 2*(X+Y)
            # t = t2 mod P+Q
            t, lcm = crt(t1, t2, 2*(X+Y), P+Q)
            if lcm == 0:
                continue
            if t < t1:
                t += lcm
            ans = min(ans, t)
    if ans == float("inf"):
        print("infinity")
    else:
        print(ans)

def main():
    T = int(input())
    for _ in range(T):
        solve()

if __name__ == '__main__':
    main()