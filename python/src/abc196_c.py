N = input()
N_len = len(N)
ans = 0
for i in range(1, N_len//2+1):
    if (i) * 2 == N_len:
        left = int(N[:i])
        right = int(N[i:])
        # print(left, right)

        if left > right:
            left -= 1
        if len(str(left)) < i:
            continue

        # print('{}~{}, {}'.format(10**(i-1), int(N[:i]), int(N[:i]) - 10**(i-1) + 1))

        ans += left - 10**(i-1) + 1
    else:
        ans += 10**i-1 - 10**(i-1) + 1
print(ans)