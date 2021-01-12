if __name__ == "__main__":
    N = int(input())
    lines = [tuple(map(int, input().split())) for _ in range(N-1)]
    Q = int(input())
    queries = [tuple(map(int, input().split())) for _ in range(Q)]

    c = [0] * N
    for t, e, x in queries:
        a, b = lines[e-1]
        if t == 1:
            c[0] += x
            c[b-1] -= x
        else:
            c[b] += x
    print(c)

    visited = set()
    stack = [1]
    while stack:
        p = stack.pop()
        visited.add(p)
        cp = c[p-1]
        for a, b in lines:
            if p == a and b not in visited:
                c[b-1] += cp
                stack.append(b)
            elif p == b and a not in visited:
                c[a-1] += cp
                stack.append(a)
    print(c)
    # print(*c, sep='\n')