N = input()
max_commma = (len(N)-1)//3
ans = 0
for i in range(1, max_commma+1):
    ans += i*(min(10**((i+1)*3)-1, int(N)) - 10**(i*3) + 1)
print(ans)