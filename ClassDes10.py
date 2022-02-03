import random


class ClassDes10:
    def __init__(self):
        # Mensaje
        self.text = ""
        self.textBin = ""  # =M
        self.IPm = [1, 5, 2, 0, 3, 7, 4, 6]
        self.textCod = ""
        # Llaves
        self.keyBin = []  # k
        self.IP = [2, 4, 1, 6, 3, 9, 0, 8, 7, 5]  # P10
        self.IPk = [5, 2, 6, 3, 7, 4, 9, 8]  # P8
        self.shift = [1, 3]
        self.keys = []
        for i in self.shift:
            self.keys.append([])

        # Cifrado
        self.C = ""
        self.D = ""
        self.EP = [3, 0, 1, 2, 1, 2, 3, 0]
        self.S0 = [['01', '00', '11', '10'], ['11', '10', '01', '00'], ['00', '10', '01', '11'],
                   ['11', '01', '11', '10']]
        self.S1 = [['00', '01', '10', '11'], ['10', '00', '01', '11'], ['11', '00', '01', '00'],
                   ['10', '01', '00', '11']]
        self.P4 = [1, 3, 2, 0]
        self.IP1 = [3, 0, 2, 4, 6, 1, 7, 5]

    def generarKey(self):
        prekey = ""
        for i in range(10):
            bit = random.randrange(0, 2, 1)
            prekey = prekey + str(bit)
        self.keyBin = list(prekey)
        # print(self.keyBin)
        self.keyHex = hex(int(prekey, 2))
        self.IPKey()
        return prekey

    def IPKey(self):
        # permutacion de la llave
        k = []  # Clave permutada
        for i in self.IP:
            k.append(self.keyBin[i])
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
                self.keys[i].append(save[j])

    def encriptar(self):
        while(len(self.text)>=8):
            self.textBin = self.text[:8]
            self.C += self.cifrado()
            self.text = self.text[8:]
        self.C += self.text

    def desencriptar(self):
        while (len(self.C) >= 8):
            self.textBin = self.C[:8]
            self.D += self.cifrado()
            self.C = self.C[8:]
        self.D += self.C

    def cifrado(self):
        listM = list(self.textBin)
        save = []
        for i in self.IPm:
            save.append(listM[i])
        d = 4
        R = save[:d]
        xor = save[d:]
        for K in self.keys:
            L = R
            R = xor
            R2 = []
            for i in self.EP:
                R2.append(R[i])
            r = "".join(R2)
            k = "".join(K)
            xor = bin(int(r, 2) ^ int(k, 2))
            xor = [i for i in str(xor)[2:]]
            xor = ['0'] * (len(R2) - len(xor)) + xor
            f = int(xor[0] + xor[3], 2)
            c = int(xor[1] + xor[2], 2)
            save = [i for i in self.S0[f][c]]
            f = int(xor[4] + xor[7], 2)
            c = int(xor[5] + xor[6], 2)
            save = save + [i for i in self.S1[f][c]]
            Save = []
            for i in self.P4:
                Save.append(save[i])
            l = "".join(L)
            save = "".join(Save)
            xor = bin(int(l, 2) ^ int(save, 2))
            xor = [i for i in str(xor)[2:]]
            xor = ['0'] * (len(l) - len(xor)) + xor
        save = xor + R
        C = []
        for i in self.IP1:
            C.append(save[i])
        c= "".join(C)
        return c

