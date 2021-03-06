import itertools
import math
from random import sample
from sympy import Matrix
import numpy as np
from collections import Counter
from random import sample
import math
import numpy as np
from pathlib import Path
#from pillow.Image import core as image
import matplotlib as plt
#import cv2


class CripSustitucion:

    def __init__(self, data, k):
        self.data = data
        self.abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z']
        self.flush = k

    def encriptar(self):
        flush = self.flush
        dataencrip = ""
        for i in self.data:
            j = self.search(i, self.abc)
            dataencrip += flush[j].upper()
        return dataencrip

    def desencriptar(self):
        dataDesencrip = ""
        for i in self.data:
            j = self.search(i, self.flush)
            dataDesencrip += self.abc[j]
        return dataDesencrip

    def search(self, a, t):
        ghi = t
        for i in range(25):
            if a == ghi[i]:
                return i
                break

    def cripAnalisis(self):
        data = self.data
        diccionario1 = {s: sum([1 for letter in data if letter == s]) for s in data}

        list =[]
        for i in range(len(data)-1):
            list.append(data[i]+data[i+1])
        diccionario2 = {m:0 for m in list}
        for letra in list:
            if diccionario2.fromkeys(letra):
                diccionario2[letra] = diccionario2[letra] + 1
            else:
                diccionario2[letra] = 1

        #return diccionario2

        list3 = []
        for i in range(len(data) - 2):
            list3.append(data[i] + data[i + 1] + data[i + 2])
        diccionario3 = {m: 0 for m in list3}

        for letra in list3:
            if diccionario3.fromkeys(letra):
                diccionario3[letra] = diccionario3[letra] + 1
            else:
                diccionario3[letra] = 1
        diccionario1.update(diccionario2)
        diccionario1.update(diccionario3)
        return diccionario1


        #print(count)


class CripPermutacion:

    def __init__(self, data, m, k):
        self.data = data
        self.dataEncri = []
        self.m = m
        self.listData = []
        self.listFlush = k

        if len(self.data) % self.m == 0:
            self.listData = self.separar(self.data, self.m)
        else:
            t = len(self.data)
            saveData = self.data
            while t % self.m != 0:
                saveData += 'x'
                t += 1
            self.listData = self.separar(saveData, self.m)

    def encriptar(self):
        #print(self.listFlush)
        listFinal = []
        for i in self.listData:
            a = "".join(self.encrParticion(i, self.listFlush)).upper()
            listFinal.append(a)
        self.dataEncri = listFinal
        return "".join(listFinal)

    def desencriptar (self):
        listDes =[]
        listsep= self.separar(self.data, self.m)
        d = ""
        for i in listsep:
            c = "".join(self.desencrParticion(i)).lower()
            listDes.append(c)
            listDes
        return d.join(listDes)

    def encrParticion(self, list1, listFlush):
        listFinal = []
        for i in listFlush:
            listFinal.append(list1[i])
        return listFinal

    def desencrParticion(self, list1):
        saveList=self.listFlush.copy()
        #print("f")
        #print(saveList)
        listFin=list1
        for i in range(self.m):
            for j in range(i,self.m):
                if saveList[j]<saveList[i] :
                    a = saveList[i]
                    saveList[i] = saveList[j]
                    saveList[j] = a
                    b = listFin[i]
                    listFin[i]=listFin[j]
                    listFin[j] = b
        return listFin

    def separar(self, dat, t):
        listfinal = []
        j = len(dat) / t
        j = int(j)
        for i in range(j):
            list1 = list(dat[i * t:(i + 1) * t])
            listfinal.append(list1)
        return listfinal

    def cripAnalisis(self):
        final = []
        sep = []
        divisores = []
        for i in range(1, (len(self.data)//2)+1) :
            if(len(self.data))%i == 0 and i <=6 :
                divisores.append(i)
        print(divisores)
        for j in divisores:
            list1=self.crearListPosiciones(j)
            sep = self.separar(self.data, j)
            permutations = list(itertools.permutations(list1))
            permutations.pop(0)
            #print(sep)
            for k in permutations :
                ayuda =""
                a =[]
                for l in sep :
                    a = self.encrParticion(l,k)
                    ayuda += "".join(a)+" "
                final.append(ayuda)
        return final

    def crearListPosiciones (self, i):
        list1 = []
        for j in range(i):
            list1.append(j)
        return list1

class CripDesplazamiento:

    def __init__(self, data, m):
        self.data = data.replace(" ", "")
        self.m = m
        self.flush = []

    def encriptar(self):
        if not self.data.isalpha():
            return "Unacceptable input"
        word_ascii = np.array([ord(c) for c in self.data.lower()])
        word_encryption = (((word_ascii - 97) + self.m) % 26) + 97
        encryption = [chr(c) for c in word_encryption]
        return ''.join(encryption).upper()

    def desencriptar(self):
        word_ascii = np.array([ord(c) for c in self.data.lower()])
        word_decryption = (((word_ascii - 97) - self.m) % 26) + 97
        decryption = [chr(c) for c in word_decryption]
        return ''.join(decryption)

    def criptanalisis(self):
        possible_words = []
        for i in range(26):
            self.m = i
            possible_words.append(self.desencriptar())
        return possible_words

class CripVigenere:

    def __init__(self, data, key):
        self.data = data.replace(" ", "")
        self.key = key
        self.max = 20

    def encriptar(self):
        if not self.data.isalpha():
            return "Unacceptable input"
        word_ascii = np.array([ord(c) for c in self.data.lower()])
        for i in range(len(self.key)):
            pos = i
            while pos < len(self.data):
                word_ascii[pos] = (((word_ascii[pos] - 97) + (ord(self.key.lower()[i]) - 97)) % 26) + 97
                pos += len(self.key)
        encryption = [chr(c) for c in word_ascii]
        return ''.join(encryption).upper()

    def desencriptar(self):
        word_ascii = np.array([ord(c) for c in self.data.lower()])
        for i in range(len(self.key)):
            pos = i
            while pos < len(self.data):
                word_ascii[pos] = (((word_ascii[pos] - 97) - (ord(self.key.lower()[i]) - 97)) % 26) + 97
                pos += len(self.key)
        encryption = [chr(c) for c in word_ascii]
        return ''.join(encryption)

    def changeMax(self, m):
        self.max = m

    def ic(self, x):
        if len(x) == 1 or len(x) == 0:
            return 0
        freq = Counter(x)
        sum = 0
        for i in freq:
            sum += freq[i] * (freq[i] - 1)
        return sum / (len(x) * (len(x) - 1))

    def ic_average(self, x, i):
        wordsAv = []
        for j in range(i):
            wordsAv.append(self.ic(x[j::i]))
        return np.mean(wordsAv)

    def mg(self, word, n):
        indices = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015,
                   0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,
                   0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,
                   0.00978, 0.02360, 0.00150, 0.01974, 0.00074]
        freq = {}
        for c in 'abcdefghijklmnopqrstuvwxyz':
            freq[c] = 0
        temp = Counter(''.join(word.lower()))
        for a in temp:
            freq[a] += temp[a]
        m = []
        for g in range(26):
            sum = 0
            for i in range(26):
                sum += indices[i] * freq[chr(((i + g) % 26) + 97)]
            m.append((g, abs(0.0667 - (sum / n))))
        return chr((sorted(m, key=lambda x: x[1])[0][0]) + 97)

    def criptanalisis(self):
        average = []
        for i in range(self.max):
            average.append((i + 1, abs(0.0667 - self.ic_average(self.data, i + 1))))
        possibles_ordered = sorted(average, key=lambda x: x[1])
        return [i[0] for i in possibles_ordered]

    def criptanalisis_key(self,m):
        possible_key = ''
        for i in range(m):
            y = self.data.lower()[i::m]
            possible_key += self.mg(y, len(self.data) / m)
        self.key = possible_key
        return possible_key


class CripHill:

    def __init__(self, data, key):
        self.data = data.replace(" ", "")
        self.key = key
        self.M = np.asmatrix([])
        self.n = 0
        self.path = str(Path.home() / "Downloads")+'/greyimg1.png'
        if len(self.key) > 1:
            self.setObject()

    def loadImag(self, path):
        img = Image.open(path)

        imgArray = np.asarray(img.convert('L'))
        message1 = imgArray.flatten()  # .tolist()

        print(message1)
        print(type(message1))
        # display the array of pixels as an image
        plt.pyplot.imshow(img)
        plt.pyplot.show()
        return message1

    def encryption(self, matrix, keyMatrix):
        encryption = np.matmul(self.makingTheMatrix(self.data, self.n), self.M)
        encryption = np.remainder(encryption, 26)
        message = encryption.flatten()
        while ((np.size(message) % 255) != 0):
            np.append(message, 0)
        #print(np.shape(message))
        return message


    def arrayToImg(self,arreg):
        gr_im = np.split(arreg, 256)
        # gr_im= Image.fromarray(arreg)
        plt.pyplot.imshow(gr_im)
        plt.pyplot.show()
        gr_im.save('secretIMG.png')


    def setObject(self):
        word_ascii = self.textToAscii()
        self.n = self.checkingTheSize()
        self.boo = self.makingTheKeyMatrix(word_ascii, self.n)


    def encriptar(self):
        encryption = np.matmul(self.makingTheMatrix(self.data, self.n), self.M)
        encryption = np.remainder(encryption, 26)
        message = encryption.flatten().tolist()
        #print(len(message[0]), type(message[0]), message[0])
        # l = "".join(map(chr(message + 96)))
        secret = ""
        for i in range(len(message[0])):
            secret = secret + secret.join(chr(message[0][i] + 97))
        # print(l)
        return secret

    def textToAscii(self):
        text = self.key.replace(" ", "")
        wordascii = np.array([ord(c) for c in text.lower()])- 97
        if len(self.key) == 0:
            raise Exception("La clave debe tener minimo dos caracteres")
        elif len(self.key) == 1:
            raise Exception("La clave debe tener minimo dos caracteres")
        #print(wordascii)
        return wordascii

    def makingTheMatrix(self, arr, n):
        i = 0
        coc = int(len(arr) / n)
        arr = np.array([ord(c) for c in arr.lower()])-97
        while (len(arr) % n != 0):
            arr = np.append(arr, i)
            i += 1
        arr = np.asmatrix(np.split(arr, coc))
        return arr

    def makingTheKeyMatrix(self, key, n):
        i = 0
        while(len(key) < n**2):
            key = np.append(key, i)
            i += 1
        M = np.asmatrix(np.split(key, n))
        if math.gcd(int(np.linalg.det(M)),26)!=1:
            return 1
        mAsList = M.flatten().tolist()
        mAsString = ""
        for i in range(len(mAsList[0])):
            mAsString = mAsString + mAsString.join(str(mAsList[0][i]))
        #print(M)
        #QtWidgets.QMessageBox.about(self, "Esta es la matriz clave", mAsString)     #Printing the keyMatrix
        self.M = M
        return 0

    def checkingTheSize(self):
        n = 2
        while (n*n < len(self.key)):
            n += 1
        return n

    def desencriptar(self):
        temp= Matrix(self.M)
        decryption = np.matmul(self.makingTheMatrix(self.data, self.n), temp.inv_mod(26))
        decryption = np.remainder(decryption, 26)
        message = decryption.flatten().tolist()
        # print(len(message[0]), type(message[0]), message[0])
        # l = "".join(map(chr(message + 96)))
        secret = ""
        for i in range(len(message[0])):
            secret = secret + secret.join(chr(message[0][i] + 97))
        # print(l)
        return secret

    def criptanalisis(self, ciphered,m):
        #matrPlain = np.array([ord(c) for c in self.data.lower()]) - 97
        #matrCipher = np.array([ord(c) for c in ciphered.lower()]) - 97
        X = self.makingTheMatrix(self.data, m)[np.ix_([0,1],[0,1])]
        invX = Matrix(X).inv_mod(26)
        print(invX)
        Y = self.makingTheMatrix(ciphered, m)[np.ix_([0,1],[0,1])]
        possibleKey = np.matmul(invX, Y)
        return np.mod(possibleKey,26)


class CripHill2:

    def __init__(self, data, key):
        self.data = data.replace(" ", "")
        self.key = key
        self.M = np.asmatrix([])
        self.n = 0
        if len(self.key) > 1:
            self.setObject()

    def encryption(self, matrix, keyMatrix):
        encryption = np.matmul(self.makingTheMatrix(self.data, self.n), self.M)
        encryption = np.remainder(encryption, 256)
        message = encryption.flatten()
        while ((np.size(message) % 255) != 0):
            np.append(message, 0)
        # print(np.shape(message))
        return message


    def setObject(self):
        word_ascii = self.textToAscii()
        self.n = self.checkingTheSize()
        self.boo = self.makingTheKeyMatrix(word_ascii, self.n)

    def encriptar(self):
        encryption = np.matmul(self.makingTheMatrix(self.data, self.n), self.M)
        encryption = np.remainder(encryption, 256)
        message = encryption.flatten().tolist()
        return message

    def textToAscii(self):
        text = self.key.replace(" ", "")
        wordascii = np.array([ord(c) for c in text.lower()]) - 97
        if len(self.key) == 0:
            raise Exception("La clave debe tener minimo dos caracteres")
        elif len(self.key) == 1:
            raise Exception("La clave debe tener minimo dos caracteres")
        # print(wordascii)
        return wordascii

    def makingTheMatrix(self, arr, n):
        i = 0

        arr = np.array([arr])
        while (len(arr) % n != 0):
            arr = np.append(arr, i)
            i += 1
        coc = len(arr) / n
        arr = np.asmatrix(np.split(arr, coc))
        return arr

    def makingTheKeyMatrix(self, key, n):
        i = 0
        while (len(key) < n ** 2):
            key = np.append(key, i)
            i += 1
        M = np.asmatrix(np.split(key, n))
        if math.gcd(int(np.linalg.det(M)), 256) != 1:
            return 1
        mAsList = M.flatten().tolist()
        mAsString = ""
        for i in range(len(mAsList[0])):
            mAsString = mAsString + mAsString.join(str(mAsList[0][i]))
        # print(M)
        # QtWidgets.QMessageBox.about(self, "Esta es la matriz clave", mAsString)     #Printing the keyMatrix
        self.M = M
        return 0

    def checkingTheSize(self):
        n = 2
        while (n * n < len(self.key)):
            n += 1
        return n

    def desencriptar(self):
        temp = Matrix(self.M)
        decryption = np.matmul(self.makingTheMatrix(self.data, self.n), temp.inv_mod(256))
        decryption = np.remainder(decryption, 256)
        message = decryption.flatten().tolist()
        return message


class CripAfin:

    def __init__(self, data, a, b):
        self.data = data.replace(" ", "")
        self.a = a
        self.b = b

    def encriptar(self):
        modword = self.data.replace(" ", "")
        if not modword.isalpha(): return "Unacceptable input"
        wordascii = np.array([ord(c)-97 for c in modword.lower()])
        wordencryption = (((wordascii * self.a) + self.b) % 26) +97
        encryption = [chr(c) for c in wordencryption]
        return ''.join(encryption)

    def desencriptar(self):
        modword = self.data.replace(" ", "")
        if not modword.isalpha(): return "Unacceptable input"
        wordascii = np.array([ord(c) - 97 for c in modword.lower()])
        wordencryption = (((wordascii - self.b)*pow(self.a, -1, 26)) % 26) + 97
        encryption = [chr(c) for c in wordencryption]
        return ''.join(encryption)

    def criptanalisis(self):
        inverses = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
        possible_words = []
        for i in range(26):
            for j in inverses:
                self.a = j
                self.b = i
                temp = self.desencriptar()
                possible_words.append(temp)
        return possible_words