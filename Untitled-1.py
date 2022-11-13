import math


def dst(x,y):
    t = 0
    for i in range(0,len(x)):
        a = (abs(x[i]-y[i]))**2
        t += a
    return math.sqrt(t)



m = (123, 34, 21)
n = (342, 32, 34)
print(dst(m,n))