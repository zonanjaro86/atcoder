# input = """
# 1500 2000 1600 3 2
# """

def main(a, b, c, x, y):
    min_price = float('inf')
    # ABピザを何枚買うかで場合分け
    for ci in range(0, (max(x,y)+1)*2, 2):
        ai = max(0, x-ci/2)
        bi = max(0, y-ci/2)
        price = ai*a + bi*b + ci*c
        min_price = min(price, min_price)
    print(int(min_price))



if __name__ == "__main__":
    a, b, c, x, y = map(int, input().split())
    main(a, b, c, x, y)