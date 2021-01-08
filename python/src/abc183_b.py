Sx, Sy, Gx, Gy = map(int, input().split())
Gy *= -1

'''
直線の式: y-Sy = (x-Sx) * (Sy-Gy)/(Sx-Gx)
求めるのはy=0となるときのxなので
x = Sx - Sy*(Sx-Gx)/(Sy-Gy)
'''
print(Sx - Sy*(Sx-Gx)/(Sy-Gy))