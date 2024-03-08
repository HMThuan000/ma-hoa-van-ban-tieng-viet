#========================================
class CXORCeasar:  
    def MaHoa(self, p, key):
        ci=""
        for c in p:
            if c == '\n':
                ci+=c
            elif c!=' ':
                so = ord(c) - 33;
                so = so ^ key
                ci += chr(so+ 33)
            else:
                ci += c
        return ci
#========================================
def main():
    p =  input("Moi nhap chuoi can ma hoa: ")
    key=3
    cXORCeasar = CXORCeasar()
    c= cXORCeasar.MaHoa(p, key)
    print("Sau khi ma hoa= ", c)
    s= cXORCeasar.MaHoa(c,key)
    print("Sau khi giai ma= ",s)
#========================================
if __name__=="__main__": #entry point
    main()


    
