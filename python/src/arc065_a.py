# 後ろから
s = input()[::-1]
words = [str[::-1] for str in ['dream', 'dreamer', 'erase', 'eraser']]
canmake = True
while s and canmake:
    canmake = False
    for word in words:
        if s.startswith(word):
            s = s[len(word):]
            canmake = True
            break
if canmake:
    print("YES")
else:
    print("NO")

# DP
words = ['dream', 'dreamer', 'erase', 'eraser']
s = input()
dp = [0]*(len(s)+1) # dp[i]:i文字目で切れれば1、できなければ0
dp[0] = 1
for i in range(len(s)):
    if not dp[i]:
        continue
    for word in words:
        if s[i:i+len(word)] == word:
            dp[i+len(word)] = 1
print(dp)
print("YES" if dp[len(s)] else "NO")

# BFS
from collections import deque
words = ['dream', 'dreamer', 'erase', 'eraser']
s = input()
q = deque([0])
can = False
while q:
    i = q.popleft()
    if i == len(s):
        can = True
        break
    for word in words:
        if s[i:i+len(word)] == word:
            q.append(i+len(word))
print("YES" if can else "NO")