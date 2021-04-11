S = input()
odd = S[::2]
even = S[1::2] if len(S) > 1 else 'A'
# print(odd, even)
if even.isupper() and odd.islower():
    print("Yes")
else:
    print("No")