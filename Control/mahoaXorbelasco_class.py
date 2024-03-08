#========================================
class CXORBelasco:
    def MaHoa(self, s_in, k):
        s=""
        for i in range(len(s_in)):
            c = s_in[i]
            if c=='\n':
                s+=c
            elif c!=' ':
                row = ord(k[i%len(k)]) - 33;
                col = ord(c) - 33;
                so = row ^ col 
                s += chr(so+ 33)
            else:
                s+=' '
        return s
#========================================
def main():
    p =  input("Moi nhap chuoi can ma hoa: ")
    k =  input("Moi nhap chuoi key: ")
    cXORBelasco = CXORBelasco()
    c = cXORBelasco.MaHoa(p,k)
    print("Sau khi ma hoa= ", c)
    s= cXORBelasco.MaHoa(c,k)
    print("Sau khi giai ma= ",s)
#========================================
if __name__=="__main__": #entry point
    main() 
