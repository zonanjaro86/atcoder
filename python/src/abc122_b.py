
def main(s):
    max_len = 0
    for i in range(len(s)):
        if s[i] not in "ACGT":
            continue
        for j in range(i, len(s)):
            if s[j] not in "ACGT":
                break
            max_len = max(j-i+1, max_len)
            # print(s[i:j+1])
    print(max_len)


if __name__ == "__main__":
    s = input()
    main(s)
