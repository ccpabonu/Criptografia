import numpy as np
from pyfinite import ffield

from ClassAES import ClassAES


class ProcIMG:
    def __init__(self, img, key):
        self.f = ffield.FField(8, gen=0x11b, useLUT=0)
        self.mat = list(img)
        self.col, self.row, b = img.shape
        self.i = 0
        self.j = 0
        self.key = key
        self.crip = ClassAES([], key)

    def e_ecbAES(self):
        limit = (self.col * self.row)
        count = 0
        three = []
        for row in self.mat:
                for pixel in row:
                    count += 1
                    print(count)
                    for component in pixel:
                        if len(three) < 48:
                            three.append(component)
                        else:
                            self.crip.data = three[0: 16]
                            first = self.crip.encriptar()
                            self.crip.data = three[16: 32]
                            second = self.crip.encriptar()
                            self.crip.data = three[32: 48]
                            third = self.crip.encriptar()
                            for k in range(5):
                                self.mat[self.i][self.j] = [first[3*k],first[3*k+1],first[3*k+2]]
                                if self.j == self.col-1:
                                    self.j = 0
                                    self.i += 1
                                else:
                                    self.j +=1
                            self.mat[self.i][self.j] = [first[15], second[0], second[1]]
                            if self.j == self.col-1:
                                self.j = 0
                                self.i += 1
                            else:
                                self.j += 1
                            for k in range(4):
                                self.mat[self.i][self.j] = [second[3*k+2],second[3*k+3],second[3*k+4]]
                                if self.j == self.col-1:
                                    self.j = 0
                                    self.i += 1
                                else:
                                    self.j +=1
                            self.mat[self.i][self.j] = [second[14], second[15], third[0]]
                            if self.j == self.col-1:
                                self.j = 0
                                self.i += 1
                            else:
                                self.j += 1
                            for k in range(5):
                                self.mat[self.i][self.j] = [third[3*k+1],third[3*k+2],third[3*k+3]]
                                if self.j == self.col-1:
                                    self.j = 0
                                    self.i += 1
                                else:
                                    self.j += 1
                            three = [component]
                    if count == limit : break
        return self.mat

    def d_ecbAES(self):
        limit = (self.col * self.row)
        count = 0
        three = []
        for row in self.mat:
                for pixel in row:
                    count += 1
                    print(count)
                    for component in pixel:
                        if len(three) < 48:
                            three.append(component)
                        else:
                            self.crip.data = three[0: 16]
                            first = self.crip.desencriptar()
                            self.crip.data = three[16: 32]
                            second = self.crip.desencriptar()
                            self.crip.data = three[32: 48]
                            third = self.crip.desencriptar()
                            for k in range(5):
                                self.mat[self.i][self.j] = [first[3*k],first[3*k+1],first[3*k+2]]
                                if self.j == self.col-1:
                                    self.j = 0
                                    self.i += 1
                                else:
                                    self.j +=1
                            self.mat[self.i][self.j] = [first[15], second[0], second[1]]
                            if self.j == self.col-1:
                                self.j = 0
                                self.i += 1
                            else:
                                self.j += 1
                            for k in range(4):
                                self.mat[self.i][self.j] = [second[3*k+2],second[3*k+3],second[3*k+4]]
                                if self.j == self.col-1:
                                    self.j = 0
                                    self.i += 1
                                else:
                                    self.j +=1
                            self.mat[self.i][self.j] = [second[14], second[15], third[0]]
                            if self.j == self.col-1:
                                self.j = 0
                                self.i += 1
                            else:
                                self.j += 1
                            for k in range(5):
                                self.mat[self.i][self.j] = [third[3*k+1],third[3*k+2],third[3*k+3]]
                                if self.j == self.col-1:
                                    self.j = 0
                                    self.i += 1
                                else:
                                    self.j += 1
                            three = [component]
                    if count == limit : break
        return self.mat

    def e_cbcAES(self, four):
        limit = (self.col * self.row)
        count = 0
        three = []
        temp = np.reshape(four, (4, 4))
        for row in self.mat:
                for pixel in row:
                    count += 1
                    print(count)
                    for component in pixel:
                        if len(three) < 48:
                            three.append(component)
                        else:
                            self.crip.data = self.f.Add(np.reshape(three[0: 16], (4, 4)),temp).flatten()
                            first = self.crip.encriptar()
                            temp = np.reshape(first, (4, 4))
                            self.crip.data = self.f.Add(np.reshape(three[16: 32], (4, 4)),temp).flatten()
                            second = self.crip.encriptar()
                            temp = np.reshape(second, (4, 4))
                            self.crip.data = self.f.Add(np.reshape(three[32: 48], (4, 4)),temp).flatten()
                            third = self.crip.encriptar()
                            temp = np.reshape(third, (4, 4))
                            for k in range(5):
                                self.mat[self.i][self.j] = [first[3*k],first[3*k+1],first[3*k+2]]
                                if self.j == self.col-1:
                                    self.j = 0
                                    self.i += 1
                                else:
                                    self.j +=1
                            self.mat[self.i][self.j] = [first[15], second[0], second[1]]
                            if self.j == self.col-1:
                                self.j = 0
                                self.i += 1
                            else:
                                self.j += 1
                            for k in range(4):
                                self.mat[self.i][self.j] = [second[3*k+2],second[3*k+3],second[3*k+4]]
                                if self.j == self.col-1:
                                    self.j = 0
                                    self.i += 1
                                else:
                                    self.j +=1
                            self.mat[self.i][self.j] = [second[14], second[15], third[0]]
                            if self.j == self.col-1:
                                self.j = 0
                                self.i += 1
                            else:
                                self.j += 1
                            for k in range(5):
                                self.mat[self.i][self.j] = [third[3*k+1],third[3*k+2],third[3*k+3]]
                                if self.j == self.col-1:
                                    self.j = 0
                                    self.i += 1
                                else:
                                    self.j += 1
                            three = [component]
                    if count == limit : break
        return self.mat

    def d_cbcAES(self, four):
        limit = (self.col * self.row)
        count = 0
        three = []
        temp = np.reshape(four, (4, 4))
        for row in self.mat:
                for pixel in row:
                    count += 1
                    print(count)
                    for component in pixel:
                        if len(three) < 48:
                            three.append(component)
                        else:
                            self.crip.data = three[0: 16]
                            first = self.f.Add(np.reshape(self.crip.desencriptar(), (4, 4)),temp).flatten()
                            temp = np.reshape(three[0: 16], (4, 4))
                            self.crip.data = three[16: 32]
                            second = self.f.Add(np.reshape(self.crip.desencriptar(), (4, 4)), temp).flatten()
                            temp = np.reshape(three     [16: 32], (4, 4))
                            self.crip.data = three[32: 48]
                            third = self.f.Add(np.reshape(self.crip.desencriptar(), (4, 4)), temp).flatten()
                            temp = np.reshape(three[32: 48], (4, 4))
                            for k in range(5):
                                self.mat[self.i][self.j] = [first[3*k],first[3*k+1],first[3*k+2]]
                                if self.j == self.col-1:
                                    self.j = 0
                                    self.i += 1
                                else:
                                    self.j +=1
                            self.mat[self.i][self.j] = [first[15], second[0], second[1]]
                            if self.j == self.col-1:
                                self.j = 0
                                self.i += 1
                            else:
                                self.j += 1
                            for k in range(4):
                                self.mat[self.i][self.j] = [second[3*k+2],second[3*k+3],second[3*k+4]]
                                if self.j == self.col-1:
                                    self.j = 0
                                    self.i += 1
                                else:
                                    self.j +=1
                            self.mat[self.i][self.j] = [second[14], second[15], third[0]]
                            if self.j == self.col-1:
                                self.j = 0
                                self.i += 1
                            else:
                                self.j += 1
                            for k in range(5):
                                self.mat[self.i][self.j] = [third[3*k+1],third[3*k+2],third[3*k+3]]
                                if self.j == self.col-1:
                                    self.j = 0
                                    self.i += 1
                                else:
                                    self.j += 1
                            three = [component]
                    if count == limit : break
        return self.mat

    def e_cfbAES(self, four):
        limit = (self.col * self.row)
        count = 0
        three = []
        self.crip.data = four
        temp = np.reshape(self.crip.encriptar(), (4, 4))
        for row in self.mat:
                for pixel in row:
                    count += 1
                    print(count)
                    for component in pixel:
                        if len(three) < 48:
                            three.append(component)
                        else:
                            first = self.f.Add(np.reshape(three[0: 16], (4, 4)),temp).flatten()
                            self.crip.data = first
                            temp = np.reshape(self.crip.encriptar(), (4, 4))
                            second = self.f.Add(np.reshape(three[16: 32], (4, 4)), temp).flatten()
                            self.crip.data = second
                            temp = np.reshape(self.crip.encriptar(), (4, 4))
                            third = self.f.Add(np.reshape(three[32: 48], (4, 4)), temp).flatten()
                            self.crip.data = third
                            temp = np.reshape(self.crip.encriptar(), (4, 4))
                            for k in range(5):
                                self.mat[self.i][self.j] = [first[3*k],first[3*k+1],first[3*k+2]]
                                if self.j == self.col-1:
                                    self.j = 0
                                    self.i += 1
                                else:
                                    self.j +=1
                            self.mat[self.i][self.j] = [first[15], second[0], second[1]]
                            if self.j == self.col-1:
                                self.j = 0
                                self.i += 1
                            else:
                                self.j += 1
                            for k in range(4):
                                self.mat[self.i][self.j] = [second[3*k+2],second[3*k+3],second[3*k+4]]
                                if self.j == self.col-1:
                                    self.j = 0
                                    self.i += 1
                                else:
                                    self.j +=1
                            self.mat[self.i][self.j] = [second[14], second[15], third[0]]
                            if self.j == self.col-1:
                                self.j = 0
                                self.i += 1
                            else:
                                self.j += 1
                            for k in range(5):
                                self.mat[self.i][self.j] = [third[3*k+1],third[3*k+2],third[3*k+3]]
                                if self.j == self.col-1:
                                    self.j = 0
                                    self.i += 1
                                else:
                                    self.j += 1
                            three = [component]
                    if count == limit : break
        return self.mat

    def d_cfbAES(self, four):
        limit = (self.col * self.row)
        count = 0
        three = []
        self.crip.data = four
        temp = np.reshape(self.crip.encriptar(), (4, 4))
        for row in self.mat:
                for pixel in row:
                    count += 1
                    print(count)
                    for component in pixel:
                        if len(three) < 48:
                            three.append(component)
                        else:
                            first = self.f.Add(np.reshape(three[0: 16], (4, 4)),temp).flatten()
                            self.crip.data = three[0: 16]
                            temp = np.reshape(self.crip.encriptar(), (4, 4))
                            second = self.f.Add(np.reshape(three[16: 32], (4, 4)), temp).flatten()
                            self.crip.data = three[16: 32]
                            temp = np.reshape(self.crip.encriptar(), (4, 4))
                            third = self.f.Add(np.reshape(three[32: 48], (4, 4)), temp).flatten()
                            self.crip.data = three[32: 48]
                            temp = np.reshape(self.crip.encriptar(), (4, 4))
                            for k in range(5):
                                self.mat[self.i][self.j] = [first[3*k],first[3*k+1],first[3*k+2]]
                                if self.j == self.col-1:
                                    self.j = 0
                                    self.i += 1
                                else:
                                    self.j +=1
                            self.mat[self.i][self.j] = [first[15], second[0], second[1]]
                            if self.j == self.col-1:
                                self.j = 0
                                self.i += 1
                            else:
                                self.j += 1
                            for k in range(4):
                                self.mat[self.i][self.j] = [second[3*k+2],second[3*k+3],second[3*k+4]]
                                if self.j == self.col-1:
                                    self.j = 0
                                    self.i += 1
                                else:
                                    self.j +=1
                            self.mat[self.i][self.j] = [second[14], second[15], third[0]]
                            if self.j == self.col-1:
                                self.j = 0
                                self.i += 1
                            else:
                                self.j += 1
                            for k in range(5):
                                self.mat[self.i][self.j] = [third[3*k+1],third[3*k+2],third[3*k+3]]
                                if self.j == self.col-1:
                                    self.j = 0
                                    self.i += 1
                                else:
                                    self.j += 1
                            three = [component]
                    if count == limit : break
        return self.mat

    def e_ofbAES(self, four):
        limit = (self.col * self.row)
        count = 0
        three = []
        self.crip.data = four
        temp = np.reshape(self.crip.encriptar(), (4, 4))
        for row in self.mat:
                for pixel in row:
                    count += 1
                    print(count)
                    for component in pixel:
                        if len(three) < 48:
                            three.append(component)
                        else:
                            first = self.f.Add(np.reshape(three[0: 16], (4, 4)),temp).flatten()
                            self.crip.data = temp
                            temp = np.reshape(self.crip.encriptar(), (4, 4))
                            second = self.f.Add(np.reshape(three[16: 32], (4, 4)), temp).flatten()
                            self.crip.data = temp
                            temp = np.reshape(self.crip.encriptar(), (4, 4))
                            third = self.f.Add(np.reshape(three[32: 48], (4, 4)), temp).flatten()
                            self.crip.data = temp
                            temp = np.reshape(self.crip.encriptar(), (4, 4))
                            for k in range(5):
                                self.mat[self.i][self.j] = [first[3*k],first[3*k+1],first[3*k+2]]
                                if self.j == self.col-1:
                                    self.j = 0
                                    self.i += 1
                                else:
                                    self.j +=1
                            self.mat[self.i][self.j] = [first[15], second[0], second[1]]
                            if self.j == self.col-1:
                                self.j = 0
                                self.i += 1
                            else:
                                self.j += 1
                            for k in range(4):
                                self.mat[self.i][self.j] = [second[3*k+2],second[3*k+3],second[3*k+4]]
                                if self.j == self.col-1:
                                    self.j = 0
                                    self.i += 1
                                else:
                                    self.j +=1
                            self.mat[self.i][self.j] = [second[14], second[15], third[0]]
                            if self.j == self.col-1:
                                self.j = 0
                                self.i += 1
                            else:
                                self.j += 1
                            for k in range(5):
                                self.mat[self.i][self.j] = [third[3*k+1],third[3*k+2],third[3*k+3]]
                                if self.j == self.col-1:
                                    self.j = 0
                                    self.i += 1
                                else:
                                    self.j += 1
                            three = [component]
                    if count == limit : break
        return self.mat

    def d_ofbAES(self, four):
        limit = (self.col * self.row)
        count = 0
        three = []
        self.crip.data = four
        temp = np.reshape(self.crip.encriptar(), (4, 4))
        for row in self.mat:
                for pixel in row:
                    count += 1
                    print(count)
                    for component in pixel:
                        if len(three) < 48:
                            three.append(component)
                        else:
                            first = self.f.Add(np.reshape(three[0: 16], (4, 4)),temp).flatten()
                            self.crip.data = temp
                            temp = np.reshape(self.crip.encriptar(), (4, 4))
                            second = self.f.Add(np.reshape(three[16: 32], (4, 4)), temp).flatten()
                            self.crip.data = temp
                            temp = np.reshape(self.crip.encriptar(), (4, 4))
                            third = self.f.Add(np.reshape(three[32: 48], (4, 4)), temp).flatten()
                            self.crip.data = temp
                            temp = np.reshape(self.crip.encriptar(), (4, 4))
                            for k in range(5):
                                self.mat[self.i][self.j] = [first[3*k],first[3*k+1],first[3*k+2]]
                                if self.j == self.col-1:
                                    self.j = 0
                                    self.i += 1
                                else:
                                    self.j +=1
                            self.mat[self.i][self.j] = [first[15], second[0], second[1]]
                            if self.j == self.col-1:
                                self.j = 0
                                self.i += 1
                            else:
                                self.j += 1
                            for k in range(4):
                                self.mat[self.i][self.j] = [second[3*k+2],second[3*k+3],second[3*k+4]]
                                if self.j == self.col-1:
                                    self.j = 0
                                    self.i += 1
                                else:
                                    self.j +=1
                            self.mat[self.i][self.j] = [second[14], second[15], third[0]]
                            if self.j == self.col-1:
                                self.j = 0
                                self.i += 1
                            else:
                                self.j += 1
                            for k in range(5):
                                self.mat[self.i][self.j] = [third[3*k+1],third[3*k+2],third[3*k+3]]
                                if self.j == self.col-1:
                                    self.j = 0
                                    self.i += 1
                                else:
                                    self.j += 1
                            three = [component]
                    if count == limit : break
        return self.mat

    def e_ctrAES(self, four):
        limit = (self.col * self.row)
        count = 0
        three = []
        self.crip.data = four
        temp = np.reshape(four, (4, 4))
        for row in self.mat:
                for pixel in row:
                    count += 1
                    print(count)
                    for component in pixel:
                        if len(three) < 48:
                            three.append(component)
                        else:
                            first = self.f.Add(np.reshape(three[0: 16], (4, 4)),np.reshape(self.crip.encriptar(), (4, 4))).flatten()
                            temp[3][3] = self.f.Add(temp[3][3],1)
                            self.crip.data = temp
                            second = self.f.Add(np.reshape(three[16: 32], (4, 4)), np.reshape(self.crip.encriptar(), (4, 4))).flatten()
                            temp[3][3] = self.f.Add(temp[3][3], 1)
                            self.crip.data = temp
                            temp = np.reshape(self.crip.encriptar(), (4, 4))
                            third = self.f.Add(np.reshape(three[32: 48], (4, 4)), np.reshape(self.crip.encriptar(), (4, 4))).flatten()
                            temp[3][3] = self.f.Add(temp[3][3], 1)
                            self.crip.data = temp
                            for k in range(5):
                                self.mat[self.i][self.j] = [first[3*k],first[3*k+1],first[3*k+2]]
                                if self.j == self.col-1:
                                    self.j = 0
                                    self.i += 1
                                else:
                                    self.j +=1
                            self.mat[self.i][self.j] = [first[15], second[0], second[1]]
                            if self.j == self.col-1:
                                self.j = 0
                                self.i += 1
                            else:
                                self.j += 1
                            for k in range(4):
                                self.mat[self.i][self.j] = [second[3*k+2],second[3*k+3],second[3*k+4]]
                                if self.j == self.col-1:
                                    self.j = 0
                                    self.i += 1
                                else:
                                    self.j +=1
                            self.mat[self.i][self.j] = [second[14], second[15], third[0]]
                            if self.j == self.col-1:
                                self.j = 0
                                self.i += 1
                            else:
                                self.j += 1
                            for k in range(5):
                                self.mat[self.i][self.j] = [third[3*k+1],third[3*k+2],third[3*k+3]]
                                if self.j == self.col-1:
                                    self.j = 0
                                    self.i += 1
                                else:
                                    self.j += 1
                            three = [component]
                    if count == limit : break
        return self.mat
