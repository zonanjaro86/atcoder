N = int(input())

"""
初項a, 項数n, 公差1の等差数列の和をNとすると
2N = n**2 + 2an -n
2a = 2N/n - n + 1
つまり、2N/nが整数かつ、2N/n - n + 1が偶数となればよい
nのとりかたは2Nの約数を考える
"""

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

cnt = 0
for n in make_divisors(N*2):
    if (N*2/n - n + 1) % 2 == 0:
        cnt += 1
print(cnt)