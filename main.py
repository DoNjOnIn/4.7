import math
def main():
    x1 = float(input('x1='))
    x2 = float(input('x2='))
    d = float(input('d='))
    eps = float(input('eps='))
    x = x1
    while x <= x2:
        n = 1
        q = -x
        s = q
        while 1>0:
            R = -x * x * (2 * n - 1) / (2 * n + 1)
            q *= R
            if math.fabs(q)>=eps:
                s += q
                n += 1
            else:
                break
        print(str(x)+'      '+str(s)+'     '+str(n))
        x += d
if __name__=='__main__':
    main()