def gcd(m, n):
    while n:
        m, n = n, m % n
    return m

def egcd(a, b):
    """拡張ユークリッド互助法
    px + qy = gcd(p, q) = dを満たすdとxとyを返す
    """
    if a == 0:
        return b, 0, 1
    g, y, x = egcd(b % a, a)
    return g, x - (b // a) * y, y

def chineseRem(b1, m1, b2, m2):
    """中国剰余定理(2次元)
    x ≡ b1 mod m1 ∧ x ≡ b2 mod m2 <=> x ≡ r mod m
    となる(r, m)を返す
    解なしの場合は(0, -1)
    """
    d, p, q = egcd(m1, m2)
    if (b1 - b2) % d != 0:
        return 0, -1
    m = m1 * (m2 // d) # m = lcm(m1, m2)
    tmp = (b2-b1) // d * p % (m2 // d)
    r = (b1 + m1 * tmp) % m
    # print('a:{}, b:{}, C:{}, D:{}'.format(a, b, C, moDd2))
    # print('r:{}, lcm:{}'.format(r, lcm))
    return r, m


def solve():
    X, Y, P, Q = map(int, input().split())

    # 周期
    C = 2 * (X + Y)
    D = P + Q

    ans = float("inf")
    for a in range(X, X+Y):
        for b in range(P, P+Q):
            t, lcm = chineseRem(a, C, b, D)
            if lcm == -1:
                continue
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