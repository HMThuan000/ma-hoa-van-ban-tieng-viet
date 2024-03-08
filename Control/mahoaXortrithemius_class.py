#=============================================
class CXORTrithemius:
    def MaHoa(self, s_in):
        s=""
        for i in range(len(s_in)):
            c = s_in[i]
            if c=='\n':
                s+= c
            elif c!=' ':
                so = ord(c) - 33;
                so = (so^(i%65500))# % 65500
                s += chr(so+ 33)
            else:
                s += ' '
        return s
#========================================
def main():
    p =  input("Moi nhap chuoi can ma hoa: ")
    cXORTrithemius= CXORTrithemius()
    c = cXORTrithemius.MaHoa(p)
    print("Sau khi ma hoa= ", c)
    s= cXORTrithemius.MaHoa(c)
    print("Sau khi giai ma= ",s)
#========================================
if __name__=="__main__": #entry point
    main() 
