m = int(input())
VV = ''
if m < 100:
    VV = '00'
elif m <= 5000:
    VV = '{:0=2}'.format(int(m/100))
elif m <= 30000:
    VV = '{}'.format(int((m/1000) + 50))
elif m <= 70000:
    VV = '{}'.format(int((m/1000 - 30)/5 + 80))
else:
    VV = '89'
print(VV)