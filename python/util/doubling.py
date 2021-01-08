# -*- coding: utf-8 -*-

# 繰り返し2乗法

# x**n O(n)
def pow(x, n):
    ans = 1
    for i in range(n):
        ans *= x
    return ans
# print(pow(3,3))

# x**n O(logN)

# 3(10) = 11(2)
# 3^1 * 3^2

# 10(10) = 1010(2)
# 3^2 * 3^8

def pow2(x, n):
    ans = 1
    while n > 0:
        if (n & 1) == 1:
            ans = ans * x
        x = x * x
        n >>= 1
    return ans
print(pow2(10,100))