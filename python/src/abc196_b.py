X = input()

dot = X.find('.')
if dot >= 0:
    print(X[:dot])
else:
    print(X)