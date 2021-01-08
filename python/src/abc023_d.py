N = int(input())
H = [0] * N
S = [0] * N
for i in range(N):
    H[i], S[i] = map(int, input().split())

# N = 4
# H = [5, 12, 14, 21]
# S = [6, 4, 7, 2]

"""
H + St <= X
t <= (X - H)/S
"""

def is_ok(X):
    T = sorted([(X - H[i]) // S[i] for i in range(N)])
    # print(T)
    f = True
    for i in range(N):
        if T[i] < i: f = False
    return f

low = 0
high = max(H) + max(S) * N

while abs(high - low) > 1:
    mid = (high + low)//2
    if is_ok(mid):
        high = mid
    else:
        low = mid
print(high)

