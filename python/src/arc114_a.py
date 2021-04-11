import itertools
import numpy as np

N = int(input())
X = tuple(map(int, input().split()))

# Xのいずれとも約数を持つ
prime = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
arr = []
for i in range(1, len(prime)+1):
    for nums in itertools.combinations(prime, i):
        multi = 1
        for num in nums:
            multi *= num
        arr.append((multi, nums))
arr.sort()

for multi, primes in arr:
    if all([any([x % prime == 0 for prime in primes]) for x in X]):
        print(multi)
        break
