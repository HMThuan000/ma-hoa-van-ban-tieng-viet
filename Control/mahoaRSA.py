import math
e=65537; n=4255903; d=2480777
#==============================
def MaHoa(p,e,n):
    ci = []
    for c in p:
        m = ord(c)
        kq = pow(m,e,n)
        ci.append(kq)
    return ci
#===============================
def GiaiMa(ci,d,n):
    s = ''
    for c in ci:
        kq = pow(c,d,n) 
        s+=chr(kq)
    return s
#===============================
def Run():
    p = input('Mời nhập chuỗi cần mã hoá: ')
    ci = MaHoa(p,e,n)
    print('Sau khi mã hoá: ',end='')
    for i in ci:
        print("%X" % i,end=' ')
    print('\n')
    s = GiaiMa(ci,d,n)
    print('Sau khi giải mã: %s'%s)
#===============================
if __name__ == '__main__':
    Run()
