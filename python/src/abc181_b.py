def main(n, list):
    sum = 0
    for (a, b) in list:
        sum += (a + b) * (b - a + 1) / 2

    print(int(sum))

if __name__ == '__main__':
    n = int(input())
    list = []
    for i in range(n):
        a, b = map(int, input().split())
        list.append((a, b))

    main(n, list)
