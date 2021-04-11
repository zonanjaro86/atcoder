n = int(input())
a = list(map(int, input().split()))
a = sorted(a)[::-1]
print(sum(a[::2]) - sum(a[1::2]))