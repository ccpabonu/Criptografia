from Class3Des64 import Class3Des64
from ClassDes64 import ClassDes64
import numpy as np

class ProcIMG:
    def __init__(self, img1, m,n):
        self.matriz = img1.copy()
        #self.textplano="000000001111111100000000111111110000000011111111000000001111111100000000111111110000000011111111"
        self.textplano=""
        self.matrizsobr = []
        self.result = img1.copy()
        self.col=m
        self.row=n
        self.i=0
        self.j=0
        self.c = ClassDes64()
        self.c3 = Class3Des64()
        self.key = self.c.generarKey()

    def codificarDes64 (self):
        text192=""
        result = ""
        num=((self.col*self.row*24)%192)//24
        while (num != 0):
            if (num >= self.col):
                self.matrizsobr= self.matrizsobr + np.delete(self.matriz,-1).tolist()
                num = num - self.col
            else:
                for i in range(num):
                    self.matrizsobr= self.matrizsobr + np.delete(self.matriz[-1],-1).tolist()
                    num = num - 1
        savepixel = []

        for row in self.matriz:
            for pixel in row:
                for component in pixel:
                    s = bin(component)
                    s = s[2:]
                    for k in range(8 - len(s)):
                        var = '0' + s
                        s = var
                    self.textplano = self.textplano + s
                    savepixel.append(s)
                    text192 = text192+s
                if(len(text192) == 192):
                    h8= text192[:64]
                    self.c.textBin = h8
                    result = result + self.c.encriptar()
                    h8 = text192[64:128]
                    self.c.textBin = h8
                    result = result + self.c.encriptar()
                    h8 = text192[128:]
                    self.c.textBin = h8
                    result = result + self.c.encriptar()
                    text192=""
                    self.crearPixels(result)
                    result=""

    def crearPixels(self,r):
        save=[]
        while(len(r)!=0):
            pixel=[]
            for i in range(3):
                saveRGB=int(r[:8],2)
                pixel.append(saveRGB)
                r=r[8:]
            save.append(pixel)
        for k in save:
            if(self.j<self.col):
                self.result[self.i][self.j] = k
                self.j = self.j + 1
            else:
                self.j = 0
                self.i = self.i + 1
                self.result[self.i][self.j] = k
                self.j= self.j+1

    def darResultado(self):
        if(len(self.matrizsobr)!=0):
            np.append(self.result[-1],self.matrizsobr)
            self.matrizsobr = []
        self.i= 0
        self.j= 0
        return self.result

    def decodificarDes64 (self):
        self.c.keys.reverse()
        text192 = ""
        result = ""
        num = ((self.col * self.row * 24) % 192) // 24
        while (num != 0):
            if (num >= self.col):
                self.matrizsobr= self.matrizsobr + np.delete(self.matriz,-1).tolist()
                num = num - self.col
            else:
                for i in range(num):
                    self.matrizsobr= self.matrizsobr + np.delete(self.matriz[-1],-1).tolist()
                    num = num - 1
        savepixel = []
        for row in self.matriz:
            for pixel in row:
                for component in pixel:
                    s = bin(component)
                    s = s[2:]
                    for k in range(8 - len(s)):
                        var = '0' + s
                        s = var
                    self.textplano = self.textplano + s
                    savepixel.append(s)
                    text192 = text192 + s
                if (len(text192) == 192):

                    h8 = text192[:64]
                    self.c.textCod = h8
                    result = result + self.c.desencriptar()
                    h8 = text192[64:128]
                    self.c.textCod = h8
                    result = result + self.c.desencriptar()
                    h8 = text192[128:]
                    self.c.textCod = h8
                    result = result + self.c.desencriptar()
                    text192 = ""
                    self.crearPixels(result)
                    result = ""

    def codificar3Des64 (self):
        text192 = ""
        result = ""
        num = ((self.col * self.row * 24) % 192) // 24
        while (num != 0):
            if (num >= self.col):
                self.matrizsobr = self.matrizsobr + np.delete(self.matriz, -1).tolist()
                num = num - self.col
            else:
                for i in range(num):
                    self.matrizsobr = self.matrizsobr + np.delete(self.matriz[-1], -1).tolist()
                    num = num - 1
        savepixel = []

        for row in self.matriz:
            for pixel in row:
                for component in pixel:
                    s = bin(component)
                    s = s[2:]
                    for k in range(8 - len(s)):
                        var = '0' + s
                        s = var
                    self.textplano = self.textplano + s
                    savepixel.append(s)
                    text192 = text192 + s
                if (len(text192) == 192):
                    h8 = text192[:64]
                    self.c3.textBin = h8
                    result = result + self.c3.tripleDes()
                    h8 = text192[64:128]
                    self.c3.textBin = h8
                    result = result + self.c3.tripleDes()
                    h8 = text192[128:]
                    self.c3.textBin = h8
                    result = result + self.c3.tripleDes()
                    text192 = ""
                    self.crearPixels(result)
                    result = ""

    def decodificar3Des64 (self):
        text192 = ""
        result = ""
        num = ((self.col * self.row * 24) % 192) // 24
        while (num != 0):
            if (num >= self.col):
                self.matrizsobr = self.matrizsobr + np.delete(self.matriz, -1).tolist()
                num = num - self.col
            else:
                for i in range(num):
                    self.matrizsobr = self.matrizsobr + np.delete(self.matriz[-1], -1).tolist()
                    num = num - 1
        savepixel = []

        for row in self.matriz:
            for pixel in row:
                for component in pixel:
                    s = bin(component)
                    s = s[2:]
                    for k in range(8 - len(s)):
                        var = '0' + s
                        s = var
                    self.textplano = self.textplano + s
                    savepixel.append(s)
                    text192 = text192 + s
                if (len(text192) == 192):
                    h8 = text192[:64]
                    self.c3.textBin = h8
                    result = result + self.c3.desTripleDes()
                    h8 = text192[64:128]
                    self.c3.textBin = h8
                    result = result + self.c3.desTripleDes()
                    h8 = text192[128:]
                    self.c3.textBin = h8
                    result = result + self.c3.desTripleDes()
                    text192 = ""
                    self.crearPixels(result)
                    result = ""