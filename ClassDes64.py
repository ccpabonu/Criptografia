import random


class ClassDes64:
    def __init__(self):
        # Mensaje
        self.textBin = "0000000100100011010001010110011110001001101010111100110111101111"  # =M
        self.IPm = [58,50,42,34,26,18,10,2,60,52,44,36,28,20,12,4,62,54,46,38,30,22,14,6,64,56,48,40,32,24,16,8,57,49,41,33,25,17,9,1,59,51,43,35,27,19,11,3,61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7]
        self.textCod = ""

        # Llaves
        self.keyBin = ['0','0','0','1','0','0','1','1','0','0','1','1','0','1','0','0','0','1','0','1','0','1','1','1','0','1','1','1','1','0','0','1','1','0','0','1','1','0','1','1','1','0','1','1','1','1','0','0','1','1','0','1','1','1','1','1','1','1','1','1','0','0','0','1']  # k
        self.IP = [57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4]  # P10
        self.IPk = [14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,7,27,20,13,2,41,52,31,37,47,55,30,40,51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32]  # P8
        self.shift = [1, 2,4,6,8,10,12,14,15,17,19,21,23,25,27,28]
        self.keys = []
        for i in self.shift:
            self.keys.append([])

        # Cifrado
        self.C = []
        self.D = []
        self.EP = [32,1,2,3,4,5,4,5,6,7,8,9,8,9,10,11,12,13,12,13,14,15,16,17,16,17,18,19,20,21,20,21,22,23,24,25,24,25,26,27,28,29,28,29,30,31,32,1]
        self.S0 = [[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
                    [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
                    [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
                    [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]]
        self.S1 = [[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
                    [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
                    [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
                    [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]]
        self.S2 = [[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
                    [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
                    [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
                    [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]]
        self.S3 = [[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
                    [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
                    [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
                    [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]]
        self.S4 = [[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
                    [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
                    [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
                    [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]]
        self.S5 = [[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
                    [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
                    [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
                    [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]]
        self.S6 = [[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
                    [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
                    [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
                    [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]]
        self.S7 = [[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
                    [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
                    [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
                    [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]
        self.Si =[]
        self.Si.append(self.S0)
        self.Si.append(self.S1)
        self.Si.append(self.S2)
        self.Si.append(self.S3)
        self.Si.append(self.S4)
        self.Si.append(self.S5)
        self.Si.append(self.S6)
        self.Si.append(self.S7)
        self.SBox=[]

        self.P = [16,7,20,21,29,12,28,17,1,15,23,26,5,18,31,10,2,8,24,14,32,27,3,9,19,13,30,6,22,11,4,25]
        self.IP_1 = [40,8,48,16,56,24,64,32,39,7,47,15,55,23,63,31,38,6,46,14,54,22,62,30,37,5,45,13,53,21,61,29,36,4,44,12,52,20,60,28,35,3,43,11,51,19,59,27,34,2,42,10,50,18,58,26,33,1,41,9,49,17,57,25]

        # ---
        #self.IPKey()
        #self.encriptar(self.textBin)
        #self.desencriptar(self.C)
        #print('M:', list(self.textBin), '\nC:', self.C, '\nD:', self.D)

    def generarKey(self):
        prekey = ""
        for i in range(64):
            bit = random.randrange(0, 2, 1)
            prekey = prekey + str(bit)
        self.keyBin = list(prekey)
        # print(self.keyBin)
        self.keyHex = hex(int(prekey, 2))
        self.IPKey()
        return self.keyHex

    def IPKey(self):
        # permutacion de la llave
        k = []  # Clave permutada
        for i in self.IP:
            k.append(self.keyBin[i-1])
        # print('k=',k)
        # subllaves
        n = len(k)
        for i in range(len(self.shift)):
            s = self.shift[i]
            k1 = k[:int(n / 2)]
            k1 = k1[s:] + k1[:s]
            k2 = k[int(n / 2):]
            k2 = k2[s:] + k2[:s]
            save = k1 + k2
            for j in self.IPk:
                self.keys[i].append(save[j-1])


    def encriptar(self):
        self.cifrado()

    def desencriptar(self):
        self.keys.reverse()
        self.textBin =self.textCod
        self.cifrado()
        self.keys.reverse()

    def cifrado(self):
        listM = list(self.textBin)
        save = []
        for i in self.IPm:
            save.append(listM[i-1])
        d = 32
        R = save[:d]
        xor = save[d:]
        for K in self.keys:
            L = R
            R = xor
            R2 = []
            for i in self.EP:
                R2.append(R[i-1])
            r = "".join(R2)
            k = "".join(K)
            xor = bin(int(r, 2) ^ int(k, 2))
            xor = [i for i in str(xor)[2:]]
            xor = ['0'] * (len(R2) - len(xor)) + xor
            var3=[]
            var3.clear()
            for k in range(8):
                slr=int(xor[k*6]+xor[(k*6)+5],2)
                sc=int(xor[(k*6)+1]+xor[(k*6)+2]+xor[(k*6)+3]+xor[(k*6)+4],2)
                sav=self.Si[k]
                strg=str(bin(sav[slr][sc]))
                strg=strg[2:]
                if(len(strg)!=4):
                    for k in range(4-len(strg)):
                        var='0'+strg
                        strg=var
                var2=list(strg)
                var3=var3+var2
            f=[]
            for j in self.P:
                f.append(var3[j-1])
            #R_n = l_n-1 + f(R_n-1,K_n)
            Ln = "".join(L)
            Fn = "".join(f)
            xor = str(bin(int(Ln, 2) ^ int(Fn, 2)))
            xor=xor[2:]
            for k in range(32 - len(xor)):
                var = '0' + xor
                xor = var
        save3=[]
        R16L16=list(xor+R)
        for i in self.IP_1:
            save3.append(R16L16[i-1])
        self.textCod = "".join(save3)
        print( hex(int(self.textCod, 2)))



