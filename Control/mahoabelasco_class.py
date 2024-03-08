#========================================
class CBelasco:
    def __init__(self,plaintext,key,ciphertext=""):
        self.plaintext=plaintext
        self.key=key
        self.ciphertext=ciphertext
    def MaHoa(self):
        self.ciphertext=""
        for i in range(len(self.plaintext)):
            c = self.plaintext[i]
            if c=='\n':
                self.ciphertext=self.ciphertext+c
            elif c!=' ':
                row = ord(self.key[i%len(self.key)]) - 33;
                col = ord(c) - 33;
                so = (row + col) % 65500
                self.ciphertext += chr(so+ 33)
            else:
                self.ciphertext=self.ciphertext+' '
        return self.ciphertext
    #========================================
    def GiaiMa(self):
        self.plaintext = ""
        for i in range(len(self.ciphertext)):
            c=self.ciphertext[i]
            if c=='\n':
                self.plaintext = self.plaintext+c
            elif c != ' ':
                row = ord(self.key[i%len(self.key)]) - 33;
                col = ord(c) - 33;
                so = (col - row + 65500) % 65500
                self.plaintext += chr(so+33)
            else:
                self.plaintext = self.plaintext+' '
        return self.plaintext
#========================================
def main():
    p =  input("Moi nhap chuoi can ma hoa: ")
    k =  input("Moi nhap chuoi key: ")
    cBelasco = CBelasco(p,k)
    c = cBelasco.MaHoa()
    print("Sau khi ma hoa= ", c)
    s= cBelasco.GiaiMa()
    print("Sau khi giai ma= ",s)
#========================================
if __name__=="__main__": #entry point
    main() 
