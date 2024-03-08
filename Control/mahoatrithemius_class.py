#=============================================
class CTrithemius:
    def __init__(self, plaintext,ciphertext=""):
        self.plaintext=plaintext
        self.ciphertext=ciphertext
    #========================================
    def MaHoa(self):
        self.ciphertext=""
        for i in range(len(self.plaintext)):
            c = self.plaintext[i]
            if c=='\n':
                self.ciphertext += c
            elif c!=' ':
                so = ord(c) - 33;
                so = (so+(i%65500)) % 65500
                self.ciphertext += chr(so+ 33)
            else:
                self.ciphertext += ' '
        return self.ciphertext
    #========================================
    def GiaiMa(self):
        self.plaintext = ""
        for i in range(len(self.ciphertext)):
            c=self.ciphertext[i]
            if c=='\n':
                self.plaintext += c
            elif c != ' ':
                so = ord(c)- 33
                so = (so - (i%65500) + 65500) % 65500
                self.plaintext += chr(so+33)
            else:
                self.plaintext += ' '
        return self.plaintext
#========================================
def main():
    p =  "Mời nhập chuỗi\ncần mã hoá:\nQuê hương\nLà chùm\nKhế ngọt"
    cTrithemius= CTrithemius(p)
    c = cTrithemius.MaHoa()
    print("Sau khi ma hoa= ", c)
    s= cTrithemius.GiaiMa()
    print("Sau khi giai ma= ",s)
#========================================
if __name__=="__main__": #entry point
    main() 
