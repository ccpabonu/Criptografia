import itertools
from random import sample
import numpy as np
from collections import Counter


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

class CripPermutacion():

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
        for i in range(2, len(self.data)//2+1) :
            if(len(self.data)/2)%i == 0 and i <=6 :
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

class CripDesplazamiento():

    def __init__(self, data, m):
        self.data = data
        self.m = m
        self.flush = []

    def encriptar(self):
        if not self.data.isalpha():
            return "Unacceptable input"
        word_ascii = np.array([ord(c) for c in self.data.replace(" ", "").lower()])
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

class CripVigenere():

    def __init__(self, data,key):
        self.data = data.replace(" ", "")
        self.key = key

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

    def ic(self, x):
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
        for i in range(20):
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
