from Class3Des64 import Class3Des64
from ClassDes64 import ClassDes64
import numpy as np


class ProcIMG:
    def __init__(self, img1, m, n):
        self.matriz = img1.copy()
        # self.textplano="000000001111111100000000111111110000000011111111000000001111111100000000111111110000000011111111"
        self.textplano = ""
        self.matrizsobr = []
        self.result = img1.copy()
        self.col = m
        self.row = n
        self.i = 0
        self.j = 0
        self.c = ClassDes64()
        self.c3 = Class3Des64()
        #self.key = self.c.generarKey()
        #self.key3des = self.c3.generarKey()
        self.saveCBC = ""
        self.saveCBF = ""
        self.saveOFB = ""
        self.bit=0

    def crearPixels(self, r):
        save = []
        while (len(r) != 0):
            pixel = []
            for i in range(3):
                saveRGB = int(r[:8], 2)
                pixel.append(saveRGB)
                r = r[8:]
            save.append(pixel)
        for k in save:
            if (self.j < self.col):
                self.result[self.i][self.j] = k
                self.j = self.j + 1
            else:
                self.j = 0
                self.i = self.i + 1
                self.result[self.i][self.j] = k
                self.j = self.j + 1

    # <editor-fold desc="ECB">
    def codificarDes64(self):
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
                    self.c.textBin = h8
                    result = result + self.c.encriptar()
                    h8 = text192[64:128]
                    self.c.textBin = h8
                    result = result + self.c.encriptar()
                    h8 = text192[128:]
                    self.c.textBin = h8
                    result = result + self.c.encriptar()
                    text192 = ""
                    self.crearPixels(result)
                    result = ""

    def darResultado(self):
        if (len(self.matrizsobr) != 0):
            np.append(self.result[-1], self.matrizsobr)
            self.matrizsobr = []
        self.i = 0
        self.j = 0
        return self.result

    def decodificarDes64(self):
        self.c.keys.reverse()
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

    def codificar3Des64(self):
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

    def decodificar3Des64(self):
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
    # </editor-fold>

    # <editor-fold desc="CBC">
    def codificarDes64CBC(self):
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
                if len(text192) == 192:
                    for i in range(3):
                        if self.saveCBC == "":
                            h8 = text192[:64]
                            self.c.textBin = h8
                            self.saveCBC = self.c.encriptar()
                            result = result + self.saveCBC
                            text192 = text192[64:]
                        else :
                            h8 = text192[:64]
                            xor = str(bin(int(h8, 2) ^ int(self.saveCBC, 2)))
                            xor = xor[2:]
                            for k in range(64 - len(xor)):
                                var = '0' + xor
                                xor = var
                            self.c.textBin = xor
                            self.saveCBC = self.c.encriptar()
                            result = result + self.saveCBC
                            text192 = text192[64:]
                    text192 = ""
                    self.crearPixels(result)
                    result = ""
        self.saveCBC=""

    def decodificarDes64CBC(self):
        self.c.keys.reverse()
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
                if len(text192) == 192 :
                    for i in range(3):
                        if self.saveCBC == "":
                            h8 = text192[:64]
                            self.c.textCod = h8
                            self.saveCBC = h8
                            result = result + self.c.desencriptar()
                            text192 = text192[64:]
                        else :
                            h8 = text192[:64]
                            self.c.textCod = h8
                            h9 = self.c.desencriptar()
                            xor = str(bin(int(h9, 2) ^ int(self.saveCBC, 2)))
                            xor = xor[2:]
                            for k in range(64 - len(xor)):
                                var = '0' + xor
                                xor = var
                            self.saveCBC = h8
                            result = result + xor
                            text192 = text192[64:]
                    text192 = ""
                    self.crearPixels(result)
                    result = ""

    def codificar3Des64CBC(self):
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
                if len(text192) == 192:
                    for i in range(3):
                        if self.saveCBC == "":
                            h8 = text192[:64]
                            self.c3.textBin = h8
                            self.saveCBC = self.c3.tripleDes()
                            result = result + self.saveCBC
                            text192 = text192[64:]
                        else :
                            h8 = text192[:64]
                            xor = str(bin(int(h8, 2) ^ int(self.saveCBC, 2)))
                            xor = xor[2:]
                            for k in range(64 - len(xor)):
                                var = '0' + xor
                                xor = var
                            self.c3.textBin = xor
                            self.saveCBC = self.c3.tripleDes()
                            result = result + self.saveCBC
                            text192 = text192[64:]
                    text192 = ""
                    self.crearPixels(result)
                    result = ""
        self.saveCBC=""

    def decodificar3Des64CBC(self):
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
                if len(text192) == 192 :
                    for i in range(3):
                        if self.saveCBC == "":
                            h8 = text192[:64]
                            self.c3.textBin = h8
                            self.saveCBC = h8
                            result = result + self.c3.desTripleDes()
                            text192 = text192[64:]
                        else :
                            h8 = text192[:64]
                            self.c3.textBin = h8
                            h9 = self.c3.desTripleDes()
                            xor = str(bin(int(h9, 2) ^ int(self.saveCBC, 2)))
                            xor = xor[2:]
                            for k in range(64 - len(xor)):
                                var = '0' + xor
                                xor = var
                            self.saveCBC = h8
                            result = result + xor
                            text192 = text192[64:]
                    text192 = ""
                    self.crearPixels(result)
                    result = ""
    # </editor-fold>

    # <editor-fold desc="CBF">
    def codificarDes64CBF(self):
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
                if len(text192) == 192:
                    for i in range(3):
                        if self.saveCBF == "":
                            self.c.textBin = "1111111111111111111111111111111111111111111111111111111100000000"
                            saveiv = self.c.encriptar()
                            h8 = text192[:64]
                            xor = str(bin(int(h8, 2) ^ int(saveiv, 2)))
                            xor = xor[2:]
                            for k in range(64 - len(xor)):
                                var = '0' + xor
                                xor = var
                            self.saveCBF = xor
                            result = result + xor
                            text192 = text192[64:]
                        else :
                            h8 = text192[:64]
                            self.c.textBin = self.saveCBF
                            saveiv= self.c.encriptar()
                            xor = str(bin(int(h8, 2) ^ int(saveiv, 2)))
                            xor = xor[2:]
                            for k in range(64 - len(xor)):
                                var = '0' + xor
                                xor = var
                            self.saveCBF = xor
                            result = result + xor
                            text192 = text192[64:]
                    text192 = ""
                    self.crearPixels(result)
                    result = ""
        self.saveCBF = ""

    def decodificarDes64CBF(self):
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
                    if len(text192) == 192:
                        for i in range(3):
                            if self.saveCBF == "":
                                self.c.textBin = "1111111111111111111111111111111111111111111111111111111100000000"
                                saveiv = self.c.encriptar()
                                h8 = text192[:64]
                                xor = str(bin(int(h8, 2) ^ int(saveiv, 2)))
                                xor = xor[2:]
                                for k in range(64 - len(xor)):
                                    var = '0' + xor
                                    xor = var
                                self.saveCBF = h8
                                result = result + xor
                                text192 = text192[64:]
                            else:
                                h8 = text192[:64]
                                self.c.textBin = self.saveCBF
                                saveiv = self.c.encriptar()
                                xor = str(bin(int(h8, 2) ^ int(saveiv, 2)))
                                xor = xor[2:]
                                for k in range(64 - len(xor)):
                                    var = '0' + xor
                                    xor = var
                                self.saveCBF = h8
                                result = result + xor
                                text192 = text192[64:]
                        text192 = ""
                        self.crearPixels(result)
                        result = ""
        self.saveCBF = ""

    def codificar3Des64CBF(self):
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
                    if len(text192) == 192:
                        for i in range(3):
                            if self.saveCBF == "":
                                self.c3.textBin = "1111111111111111111111111111111111111111111111111111111100000000"
                                saveiv = self.c3.tripleDes()
                                h8 = text192[:64]
                                xor = str(bin(int(h8, 2) ^ int(saveiv, 2)))
                                xor = xor[2:]
                                for k in range(64 - len(xor)):
                                    var = '0' + xor
                                    xor = var
                                self.saveCBF = xor
                                result = result + xor
                                text192 = text192[64:]
                            else:
                                h8 = text192[:64]
                                self.c3.textBin = self.saveCBF
                                saveiv = self.c3.tripleDes()
                                xor = str(bin(int(h8, 2) ^ int(saveiv, 2)))
                                xor = xor[2:]
                                for k in range(64 - len(xor)):
                                    var = '0' + xor
                                    xor = var
                                self.saveCBF = xor
                                result = result + xor
                                text192 = text192[64:]
                        text192 = ""
                        self.crearPixels(result)
                        result = ""
        self.saveCBF = ""

    def decodificar3Des64CBF(self):
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
                    if len(text192) == 192:
                        for i in range(3):
                            if self.saveCBF == "":
                                self.c3.textBin = "1111111111111111111111111111111111111111111111111111111100000000"
                                saveiv = self.c3.tripleDes()
                                h8 = text192[:64]
                                xor = str(bin(int(h8, 2) ^ int(saveiv, 2)))
                                xor = xor[2:]
                                for k in range(64 - len(xor)):
                                    var = '0' + xor
                                    xor = var
                                self.saveCBF = h8
                                result = result + xor
                                text192 = text192[64:]
                            else:
                                h8 = text192[:64]
                                self.c3.textBin = self.saveCBF
                                saveiv = self.c3.tripleDes()
                                xor = str(bin(int(h8, 2) ^ int(saveiv, 2)))
                                xor = xor[2:]
                                for k in range(64 - len(xor)):
                                    var = '0' + xor
                                    xor = var
                                self.saveCBF = h8
                                result = result + xor
                                text192 = text192[64:]
                        text192 = ""
                        self.crearPixels(result)
                        result = ""
        self.saveCBF = ""
    #</editor-fold>

    # <editor-fold desc="OFB">
    def codificarDes64OFB(self):
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
                if len(text192) == 192:
                    for i in range(3):
                        if self.saveOFB == "":
                            self.c.textBin = "1111111111111111111111111111111111111111111111111111111100000000"
                            saveiv = self.c.encriptar()
                            h8 = text192[:64]
                            xor = str(bin(int(h8, 2) ^ int(saveiv, 2)))
                            xor = xor[2:]
                            for k in range(64 - len(xor)):
                                var = '0' + xor
                                xor = var
                            self.saveOFB = saveiv
                            result = result + xor
                            text192 = text192[64:]
                        else :
                            h8 = text192[:64]
                            self.c.textBin = self.saveOFB
                            saveiv= self.c.encriptar()
                            xor = str(bin(int(h8, 2) ^ int(saveiv, 2)))
                            xor = xor[2:]
                            for k in range(64 - len(xor)):
                                var = '0' + xor
                                xor = var
                            self.saveOFB = saveiv
                            result = result + xor
                            text192 = text192[64:]
                    text192 = ""
                    self.crearPixels(result)
                    result = ""
        self.saveOFB = ""

    def decodificarDes64OFB(self):
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
                    if len(text192) == 192:
                        for i in range(3):
                            if self.saveOFB == "":
                                self.c.textBin = "1111111111111111111111111111111111111111111111111111111100000000"
                                saveiv = self.c.encriptar()
                                h8 = text192[:64]
                                xor = str(bin(int(h8, 2) ^ int(saveiv, 2)))
                                xor = xor[2:]
                                for k in range(64 - len(xor)):
                                    var = '0' + xor
                                    xor = var
                                self.saveOFB = saveiv
                                result = result + xor
                                text192 = text192[64:]
                            else:
                                h8 = text192[:64]
                                self.c.textBin = self.saveOFB
                                saveiv = self.c.encriptar()
                                xor = str(bin(int(h8, 2) ^ int(saveiv, 2)))
                                xor = xor[2:]
                                for k in range(64 - len(xor)):
                                    var = '0' + xor
                                    xor = var
                                self.saveOFB = saveiv
                                result = result + xor
                                text192 = text192[64:]
                        text192 = ""
                        self.crearPixels(result)
                        result = ""
        self.saveOFB = ""

    def codificar3Des64OFB(self):
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
                    if len(text192) == 192:
                        for i in range(3):
                            if self.saveOFB == "":
                                self.c3.textBin = "1111111111111111111111111111111111111111111111111111111100000000"
                                saveiv = self.c3.tripleDes()
                                h8 = text192[:64]
                                xor = str(bin(int(h8, 2) ^ int(saveiv, 2)))
                                xor = xor[2:]
                                for k in range(64 - len(xor)):
                                    var = '0' + xor
                                    xor = var
                                self.saveOFB = saveiv
                                result = result + xor
                                text192 = text192[64:]
                            else:
                                h8 = text192[:64]
                                self.c3.textBin = self.saveOFB
                                saveiv = self.c3.tripleDes()
                                xor = str(bin(int(h8, 2) ^ int(saveiv, 2)))
                                xor = xor[2:]
                                for k in range(64 - len(xor)):
                                    var = '0' + xor
                                    xor = var
                                self.saveOFB = saveiv
                                result = result + xor
                                text192 = text192[64:]
                        text192 = ""
                        self.crearPixels(result)
                        result = ""
        self.saveOFB = ""

    def decodificar3Des64OFB(self):
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
                    if len(text192) == 192:
                        for i in range(3):
                            if self.saveOFB == "":
                                self.c3.textBin = "1111111111111111111111111111111111111111111111111111111100000000"
                                saveiv = self.c3.tripleDes()
                                h8 = text192[:64]
                                xor = str(bin(int(h8, 2) ^ int(saveiv, 2)))
                                xor = xor[2:]
                                for k in range(64 - len(xor)):
                                    var = '0' + xor
                                    xor = var
                                self.saveOFB = saveiv
                                result = result + xor
                                text192 = text192[64:]
                            else:
                                h8 = text192[:64]
                                self.c3.textBin = self.saveOFB
                                saveiv = self.c3.tripleDes()
                                xor = str(bin(int(h8, 2) ^ int(saveiv, 2)))
                                xor = xor[2:]
                                for k in range(64 - len(xor)):
                                    var = '0' + xor
                                    xor = var
                                self.saveOFB = saveiv
                                result = result + xor
                                text192 = text192[64:]
                        text192 = ""
                        self.crearPixels(result)
                        result = ""
        self.saveOFB = ""
    # </editor-fold>

    # <editor-fold desc="CTR">
    def codificarDes64CTR(self):
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
                if len(text192) == 192:
                    for i in range(3):
                        self.c.textBin = '{:064b}'.format(self.bit)
                        saveiv = self.c.encriptar()
                        h8 = text192[:64]
                        xor = str(bin(int(h8, 2) ^ int(saveiv, 2)))
                        xor = xor[2:]
                        for k in range(64 - len(xor)):
                            var = '0' + xor
                            xor = var
                        result = result + xor
                        text192 = text192[64:]
                        self.bit=self.bit+1
                    text192 = ""
                    self.crearPixels(result)
                    result = ""
        self.bit=0

    def decodificarDes64CTR(self):
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
                    if len(text192) == 192:
                        for i in range(3):
                            self.c.textBin = '{:064b}'.format(self.bit)
                            saveiv = self.c.encriptar()
                            h8 = text192[:64]
                            xor = str(bin(int(h8, 2) ^ int(saveiv, 2)))
                            xor = xor[2:]
                            for k in range(64 - len(xor)):
                                var = '0' + xor
                                xor = var
                            result = result + xor
                            text192 = text192[64:]
                            self.bit = self.bit + 1
                        text192 = ""
                        self.crearPixels(result)
                        result = ""
        self.bit = 0

    def codificar3Des64CTR(self):
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
                if len(text192) == 192:
                    for i in range(3):
                        self.c3.textBin = '{:064b}'.format(self.bit)
                        saveiv = self.c3.tripleDes()
                        h8 = text192[:64]
                        xor = str(bin(int(h8, 2) ^ int(saveiv, 2)))
                        xor = xor[2:]
                        for k in range(64 - len(xor)):
                            var = '0' + xor
                            xor = var
                        result = result + xor
                        text192 = text192[64:]
                        self.bit = self.bit + 1
                    text192 = ""
                    self.crearPixels(result)
                    result = ""
        self.bit = 0

    def decodificar3Des64CTR(self):
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
                    if len(text192) == 192:
                        for i in range(3):
                            self.c3.textBin = '{:064b}'.format(self.bit)
                            saveiv = self.c3.tripleDes()
                            h8 = text192[:64]
                            xor = str(bin(int(h8, 2) ^ int(saveiv, 2)))
                            xor = xor[2:]
                            for k in range(64 - len(xor)):
                                var = '0' + xor
                                xor = var
                            result = result + xor
                            text192 = text192[64:]
                            self.bit = self.bit + 1
                        text192 = ""
                        self.crearPixels(result)
                        result = ""
        self.bit = 0

    # </editor-fold>
