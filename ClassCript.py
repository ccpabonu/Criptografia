from random import sample


class CripSustitucion():

    def __init__(self, data):
        self.data = data
        self.abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z']
        self.flush = []

    def encriptar(self):
        flush = sample(self.abc, len(self.abc))
        self.flush = flush
        print(flush)
        dataencrip = ""
        for i in self.data:
            j = self.search(i)
            dataencrip += flush[j].upper()
        return dataencrip

    def desencriptar(self):
        return self.data

    def search(self, a):
        for i in range(25):
            if a == self.abc[i]:
                return i
                break


class CripPermutacion():

    def __init__(self, data, m):
        self.data = data
        self.dataEncri = []
        self.m = m
        self.list = []
        self.listData = []
        self.listFlush = []
        for i in range(m):
            self.list.append(i)

    def encriptar(self):
        self.listFlush = sample(self.list, self.m)
        print(self.listFlush)
        if len(self.data) % self.m == 0:
            self.listData = self.separar(self.data)
        else:
            t = len(self.data)
            saveData = self.data
            while t % self.m != 0:
                saveData += 'x'
                t += 1
            self.listData = self.separar(saveData)
        listFinal = []
        for i in self.listData:
            listFinal.append(self.encrParticion(i))
        self.dataEncri = listFinal
        return listFinal

    def desencriptar (self):
        listDes =[]
        for i in self.dataEncri:
            listDes.append(self.desencrParticion(i))
        return listDes


    def encrParticion(self, list1):
        listFinal = []
        for i in self.listFlush:
            listFinal.append(list1[i])
        return listFinal

    def desencrParticion(self, list1):
        saveList=self.listFlush.copy()
        print(saveList)
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

    def separar(self, dat):
        listfinal = []
        j = len(dat) / self.m
        j = int(j)
        for i in range(j):
            list1 = list(dat[i * self.m:(i + 1) * self.m])
            listfinal.append(list1)
        return listfinal
