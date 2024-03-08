import math
class BitSet():
        value = 0
        length = 0
        @classmethod
        def from_sequence(cls, seq):
                n = 0
                for index, value in enumerate(reversed(seq)):
                        n += 2**index * bool(int(value))
                return BitSet(n)
        @classmethod
        def from_list(cls, lst): 
                n = 0
                for index, value in enumerate(reversed(lst)):
                        n+= 2**index * bool(int(value))
                return BitSet(n, len(lst))
        def __init__(self, value=0, length=0):
                self.value = value
                try: self.length = length or math.floor(math.log(value, 2)) + 1
                except Exception: self.length = 0
        def __and__(self, other):
                b = BitSet(self.value & int(other))
                b.length = max(self.length, b.length)
                return b
        def __or__(self, other):
                b = BitSet(self.value | int(other))
                b.length = max(self.length, b.length)
                return b
        def __invert__(self):
                b = BitSet(~self.value)
                b.length = max(self.length, b.length)
                return b
        def __xor__(self, other):
                b = BitSet(self.value ^ int(other))
                b.length = max(self.length, b.length)
                return b
        def __lshift__(self, value):
                b = BitSet(self.value << int(value))
                b.length = max(self.length, b.length)
                return b
        def __rshift__(self, value):
                b = BitSet(self.value >> int(value))
                b.length = max(self.length, b.length)
                return b
        def __eq__(self, other):
                try: return self.value == other.value
                except Exception: return self.value == other
        def __int__(self):
                return self.value
        def __str__(self):
                s=''
                for i in self[:]:
                        s += '1' if i else '0'
                return s
        def __repr__(self):
                return 'BitSet(%s)'%str(self)
        def __getitem__(self, s):
                try:
                        start, stop, step = s.indices(len(self))
                        results = []
                        for position in range(start, stop, step):
                                pos = len(self) - position - 1
                                results.append(bool(self.value & (1<<pos)))
                        return results
                except:
                        pos = len(self) - s -1
                        return bool(self.value & (1 <<pos))
        def __setitem__(self, s, value):
                try:
                        start, stop, step = s.indices(len(self))
                        for position in range(start, stop, step):
                                pos = len(self) - position - 1
                                if value: self.value |= (1 << pos)
                                else: self.value &= ~(1<<pos)
                        maximun_position = max(start + 1, stop, len(self))
                        self.length = maximun_position
                except:
                        pos = len(self) - s - 1
                        if value: self.value |= (1 << pos)
                        else: self.value &= ~(1<<pos)
                        if len(self) < pos: self.length = pos
                return self
        def __iter__(self):
                for i in self[:]:
                        yield i
        def __len__(self):
                return self.length
#=================================================
def Permutation(b, p):
        results = BitSet(0, len(p))
        vt = 0
        for item in p:
                results[vt] = b[item-1]
                vt+=1
        return results
#=================================================
def ShiftLeftCircle(b):
        t = b[0]
        b = b << 1
        if t:
                b[5] = t
                return BitSet.from_list(b[1:])
        return b
#=================================================
def Ghep(b1, b2):
        results = BitSet(int(b1), len(b1)+len(b2))
        results <<= len(b2)
        results |= b2
        return results
#=================================================
a10 = [3,5,2,7,4,10,1,9,8,6]
a8  = [6,3,7,4,8,5,10,9]
aIP = [2,6,3,1,4,8,5,7]
aEP = [4,1,2,3,2,3,4,1]
aS0 = [[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]]
aS1 = [[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]]
a4  = [2,4,3,1]
aIP_1 = [4,1,3,5,7,2,8,6]
#=================================================
def TaoKhoa(Key):
        p10 = Permutation(Key, a10)
        p10_L = BitSet.from_list(p10[:5]) 
        p10_L= ShiftLeftCircle(p10_L)
        p10_R = BitSet.from_list(p10[5:])
        p10_R= ShiftLeftCircle(p10_R)
        LS1= Ghep(p10_L,p10_R)
        K1 = Permutation(LS1, a8 ) #P8 chính là K1
        p10_L= ShiftLeftCircle(p10_L)
        p10_R= ShiftLeftCircle(p10_R)
        LS2= Ghep(p10_L,p10_R)
        K2 = Permutation(LS2, a8) #P8 lần 2 => K2
        return K1,K2
#=================================================
def S_Box(XOR, S0, S1): #slide 23
        XOR_L = BitSet.from_list(XOR[:4])
        row = BitSet(0,2)
        row[0]=XOR_L[0]
        row[1]=XOR_L[3]
        col = BitSet(0,2)
        col[0] = XOR_L[1]
        col[1] = XOR_L[2]
        n = S0[int(row)][int(col)]
        s0 = BitSet(n,2)
        XOR_R = BitSet.from_list(XOR[4:])
        row = BitSet(0,2)
        row[0]=XOR_R[0]
        row[1]=XOR_R[3]
        col = BitSet(0,2)
        col[0] = XOR_R[1]
        col[1] = XOR_R[2]
        n = S1[int(row)][int(col)]
        s1 = BitSet(n,2)
        return s0,s1
#=================================================
def Ffunction(L4, R4, K):
        EP = Permutation(R4, aEP)
        XOR = EP ^ K
        S0, S1= S_Box(XOR, aS0,aS1)
        S0 = Ghep(S0, S1) #slide 23
        P4 = Permutation(S0, a4)
        IP_L = BitSet.from_list(L4)
        XOR = P4 ^ IP_L
        return (XOR, R4)
#=================================================
def MaHoaDES(data, K1, K2):
        IP = Permutation(data, aIP )
        (XOR, R4) = Ffunction(IP[:4],IP[4:],K1) 
        (XOR, R4) = Ffunction(R4,XOR,K2)        
        FK2 = Ghep(XOR, R4) 
        IP_1 = Permutation(FK2, aIP_1)
        return IP_1 #slide 27
#=================================================
def GiaiMaDES(Ci, K1, K2):
        IP = Permutation(Ci, aIP)
        (XOR, R4) = Ffunction(IP[:4],IP[4:],K2) 
        (XOR, R4) = Ffunction(R4,XOR,K1)        
        FK2 = Ghep(XOR, R4) 
        IP_1 = Permutation(FK2, aIP_1)
        return IP_1 #slide 35
#=================================================
def MaHoa(s, k):
        sCi=''
        for i in range(len(s)):
                so = ord(s[i])
                        
                Key = BitSet(ord(k[i%len(k)]),10)
                K1,K2= TaoKhoa(Key)

                byteThap = so & 0xFF
                data = BitSet(byteThap, 8)
                CibyteThap= MaHoaDES(data, K1, K2)

                byteCao = so >> 8
                data = BitSet(byteCao, 8)
                CibyteCao= MaHoaDES(data, K1, K2)
                
                Ci = ((int(CibyteCao))<<8) | int(CibyteThap)
                sCi=sCi+chr(Ci)
        return sCi
#=================================================
def GiaiMa(s, k):
        sP=''
        for i in range(len(s)):
                so = ord(s[i])
                Key = BitSet(ord(k[i%len(k)]),10)
                K1,K2= TaoKhoa(Key)
                
                
                byteThap = so & 0xFF
                data = BitSet(byteThap, 8)
                P2= GiaiMaDES(data, K1, K2)

                byteCao = so>>8
                data = BitSet(byteCao, 8)
                P1= GiaiMaDES(data, K1, K2)
                sP+=chr(((int(P1)<<8) | int(P2)))
        return sP
#=================================================
def Run():
        s = input('Mời nhập chuỗi cần mã hoá: ')
        k = input('Mời nhập key: ')
        sCi=MaHoa(s, k)
        print('Ciphertext= %s'%sCi)
        sP=GiaiMa(sCi,k)
        print('Plaintext= %s'%sP)
#=================================================
if __name__ == '__main__':
        Run()
