X = int(input())
ans = 100 - X % 100
if ans == 0:
    ans = 100
print(ans)