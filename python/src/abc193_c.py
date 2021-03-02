import math

N = int(input())
s = set()
for i in range(2, math.floor(math.sqrt(N))+1):
    for j in range(2, N):
        if i**j > N or i**j in s:
            break
        s.add(i**j)
print(N - len(s))