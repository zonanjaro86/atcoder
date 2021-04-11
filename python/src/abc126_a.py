N, K = map(int, input().split())
S = input()
print('{}{}{}'.format(S[:K-1], S[K-1].lower(), S[K:]))