#========================================
class CChuyenViHaiDong:
    def __init__(self,plaintext="",ciphertext=""):
        self.plaintext=plaintext
        self.ciphertext=ciphertext
    #========================================
    def MaHoa(self):
        self.ciphertext=self.plaintext[0]
        for i in range(1,len(self.plaintext),2):
            self.ciphertext+=self.plaintext[i]
        for i in range(2,len(self.plaintext),2):
            self.ciphertext+=self.plaintext[i]  
        return self.ciphertext
    #========================================
    def GiaiMa(self):
        self.plaintext = list(self.ciphertext)
        k=1
        for i in range(1,len(self.plaintext),2):
            self.plaintext[i]=self.ciphertext[k]
            k=k+1
        for i in range(2,len(self.plaintext),2):
            self.plaintext[i]=self.ciphertext[k]
            k=k+1
        return ''.join(x for x in self.plaintext)
#========================================
def main():
    p =  input("Moi nhap chuoi can ma hoa: ")
    obj = CChuyenViHaiDong(p)
    c = obj.MaHoa()
    print("Sau khi ma hoa= ", c)
    s= obj.GiaiMa()
    print("Sau khi giai ma= ",s)
#========================================
if __name__=="__main__": #entry point
    main() 



