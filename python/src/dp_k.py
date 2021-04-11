N, K = map(int, input().split())
A = tuple(map(int, input().split()))

# dp[i]: 石がi個のときに直後の手番の人が勝てるか
dp = [False] * (K+1)
for i in range(K+1):
    dp[i] = any([not dp[i-a] for a in A if i-a >= 0])
print("First" if dp[K] else "Second")
