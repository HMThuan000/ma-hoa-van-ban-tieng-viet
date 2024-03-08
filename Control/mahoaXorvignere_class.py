class CXORVignere:
    def MaHoa(self, plaintext, key):
        s=""
        for i in range(len(plaintext)):
            c = plaintext[i]
            vt_key=i% len(key)
            if c=='\n':
                s+=c
            elif c!=' ':
                so = ord(c) - 33;
                so_key=ord(key[vt_key])-33+1 #????
                so = (so^so_key)# % 65500
                s+= chr(so+ 33)
            else:
                s+=key[vt_key]
        return s
    #========================================
    def GiaiMa(self, ciphertext, key ):
        s = ""
        for i in range(len(ciphertext)):
            c=ciphertext[i]
            vt_key=i%len(key)
            if c=='\n':
                s+=c
            elif c != key[vt_key]:
                so = ord(c)- 33
                so_key=ord(key[vt_key])-33+1 #?????
                so = so ^ so_key # + 65500) % 65500
                s+= chr(so+33)
            else:
                s+=' '
        return s
#========================================
def ReadFile(fileName):
    s = ''
    with open(fileName, "r", encoding = 'utf-8') as file:
        s = file.read()
    return s
#========================================
def WriteFile(fileName, s):
    with open(fileName, "w", encoding = 'utf-8') as file:
        file.write(s)
#========================================
def main():
    p =  ReadFile("QueHuong.txt")
    key="huflit"
    cXORVignere= CXORVignere() 
    c = cXORVignere.MaHoa(p,key)
    print("Sau khi ma hoa= ", c)
    WriteFile("FileMaHoaXORVignere.txt",c)
    WriteFile("FileMaHoaXORVignereKey.txt",key)
    cXORVignere2= CXORVignere()
    c=ReadFile("FileMaHoaXORVignere.txt")
    key=ReadFile("FileMaHoaXORVignereKey.txt")
    s= cXORVignere2.GiaiMa(c, key)
    print("Sau khi giai ma= ",s)
#========================================
if __name__=="__main__": #entry point
    main()





    


    
