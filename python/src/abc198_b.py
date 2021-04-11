N = input()
N = N.rstrip('0')
rev = N[::-1]
if N == rev:
    print('Yes')
else:
    print("No")