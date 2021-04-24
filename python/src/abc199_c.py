N = int(input())
S = list(input())
Q = int(input())

is_change = False
for _ in range(Q):
    T, A, B = map(int, input().split())
    if T == 1:
        if is_change:
            if A <= N:
                A += N
            else:
                A -= N
            if B <= N:
                B += N
            else:
                B -= N
        S[A-1], S[B-1] = S[B-1], S[A-1]
    else:
        is_change = not is_change

if is_change:
    print(''.join(S[N:]) + ''.join(S[:N]))
else:
    print(''.join(S))