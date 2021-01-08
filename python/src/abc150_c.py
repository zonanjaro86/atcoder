import itertools

N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

arr = tuple(itertools.permutations(range(1, N+1)))
print(abs(arr.index(P) - arr.index(Q)))