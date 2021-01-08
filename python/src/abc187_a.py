def S(str):
    sum = 0
    for i in str:
        sum += int(i)
    return sum

if __name__ == "__main__":
    A, B = input().split()
    print(max(S(A), S(B)))

