N = int(input())
price = (N*1.08)//1
if price < 206:
    print('Yay!')
elif price == 206:
    print('so-so')
else:
    print(':(')
