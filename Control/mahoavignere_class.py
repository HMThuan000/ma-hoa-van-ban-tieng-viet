class CVignere:
    def __init__(self, plaintext="",key="",ciphertext=""):
        self.plaintext=plaintext
        self.key=key
        self.ciphertext=ciphertext
    #========================================
    def MaHoa(self):
        s=""
        for i in range(len(self.plaintext)):
            c = self.plaintext[i]
            vt_key=i% len(self.key)
            if c=='\n':
                s+=c
            elif c!=' ':
                so = ord(c) - 33;
                so_key=ord(self.key[vt_key])-33+1 #????
                so = (so+so_key) % 65500
                s+= chr(so+ 33)
            else:
                s+=self.key[vt_key]
        return s
    #========================================
    def GiaiMa(self):
        s = ""
        for i in range(len(self.ciphertext)):
            c=self.ciphertext[i]
            vt_key=i%len(self.key)
            if c=='\n':
                s+=c
            elif c != self.key[vt_key]:
                so = ord(c)- 33
                so_key=ord(self.key[vt_key])-33+1 #?????
                so = (so - so_key + 65500) % 65500
                s+= chr(so+33)
            else:
                s+=' '
        return s
#========================================
def main():
    p =  "Quê hương\nLà chùm\nkhế ngọt"
    key="huflit"
    cVignere= CVignere(p,key) 
    c = cVignere.MaHoa()
    print("Sau khi ma hoa= ", c)
    cVignere2= CVignere("",key,c)
    s= cVignere2.GiaiMa()
    print("Sau khi giai ma= ",s)
#========================================
if __name__=="__main__": #entry point
    main()





    


    
