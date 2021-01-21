N = int(input())
A = list(map(int, input().split()))
top = A.index(max(A))
mid = 2**(N-1)
if top < mid:
    print(A.index(max(A[mid:])) + 1)
else:
    print(A.index(max(A[:mid])) + 1)