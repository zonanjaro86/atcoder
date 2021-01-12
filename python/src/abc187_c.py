def main():
    N = int(input())
    S = [input() for _ in range(N)]

    # Sを!で始まるものとそうでないものに分類し、相方がいるかチェックする
    S1 = set()
    S2 = set()
    for s in S:
        if s.startswith('!'):
            S1.add(s[1:])
        else:
            S2.add(s)
    for s in S1:
        if s in S2:
            print(s)
            return
    print("satisfiable")

if __name__ == "__main__":
    main()