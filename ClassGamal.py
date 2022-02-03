import random
import math
class ClassGamal :
    def __init__(self):
        self.a = 1
        self.b = 3
        self.p = 31
        self.privK = random.randint(0,self.p-1)
        self.points = []
        self.textInt =[]
        self.keyPrivB = 17
        self.keyPrivA = 13
        #self.keyPriv2 = self.primesInRange()

    def puntosElip(self):
        points = []
        for x in range(self.p):
            y2 = ((x*x*x)+(self.a*x)+self.b)%self.p
            for i in range(10) :
                y= math.sqrt(y2)
                if y - math.floor(y) == 0 :
                    points.append([x, int(y)])
                y2 = y2 + self.p
        self.points = points

    def vMod(self , n, p):
        while (n<0):
            n = n + p
        return n % p

    def pDoubling(self,point):
        x1 = point[0]
        y1 = point[1]
        lam = ((((3 * x1 * x1)+self.a) % self.p) * pow((2*y1)%self.p, -1, self.p) ) % self.p
        x2 = self.vMod((lam*lam)-(2*x1),self.p)
        y2 = self.vMod(((x1-x2)*lam)-y1, self.p)
        dou = [x2, y2]
        return dou

    def proEscalar (self,points, beta):
        point = points
        bBeta = bin(beta)
        bBeta = bBeta[2:]
        save = []
        for i in range(len(bBeta)):
            pt = math.pow(2,len(bBeta)-i-1)
            if bBeta[i] == '1':
                al = point.copy()
                for j in range(len(bBeta)-i-1) :
                    if i == len(bBeta)-1:
                        al = point.copy()
                    else :
                        s = self.pDoubling(al)
                        al = s
                save.append(al)
        for k in range(len(save)-1):
            sum = self.sums(save[k+1],save[k])
            save[k+1] = sum

        return save[-1]

    def sums(self,p,q):
        x1s = p[0]
        y1s = p[1]
        x2s = q[0]
        y2s = q[1]
        lam = (self.vMod((y2s-y1s),self.p)*(self.vMod( pow(x2s-x1s, -1, self.p)  , self.p)) )%self.p;
        x3s = self.vMod((lam*lam)-x1s-x2s,self.p)
        y3s = self.vMod((lam*(x1s-x3s)-y1s),self.p)
        p3 = [x3s, y3s]
        return p3

    def textToInt(self,m):
        save = []
        for i in m :
            asc=ord(i)
            ascH= hex(asc)
            ascH= ascH[2:]
            save.append([int(ascH[0],16),int(ascH[1],16)])
        return save

    def intToText(self,s):
        save = []
        for i in s:
            m = i
            m1, m2 = hex(m[0]), hex(m[1])
            hx = [m1[2:], m2[2:]]
            h = "".join(hx)
            charInt = int(h,16)
            char = chr(charInt)
            save.append(char)
        return "".join(save)

    def primesInRange(self):
        prime_list = []
        for n in range(1, 1000):
            isPrime = True
            for num in range(2, n):
                if n % num == 0:
                    isPrime = False
            if isPrime:
                prime_list.append(n)
        randomPrime = random.choice(prime_list)
        return randomPrime

    def inAd(self,point):
        point = [point[0],self.vMod(-point[1],self.p)]
        return point

    def log(self,p1,p2):
        for i in range(1,16):
            d = i
            save = self.proEscalar(p2,d)
            if ((p1[0] - save[0]) == 0) and ((p1[1] - save[1]) == 0):
                sol= i
        return sol

    def cifrar(self,m):
        intText = self.textToInt(m)
        self.puntosElip()
        al = self.points[0].copy()
        betaB = self.proEscalar(al,self.keyPrivB)
        save = []
        for i in range(len(intText)):
            d1 = intText[i][0]
            d2 = intText[i][1]
            p1 = self.proEscalar(al,d1)
            p2 = self.proEscalar(al,d2)
            k = self.proEscalar(betaB, self.keyPrivA)
            c1 = self.sums(p1,k)
            c2 = self.sums(p2,k)
            save.append([c1,c2])
        return save

    def descifrar(self, c):
        self.puntosElip()
        al = self.points[0].copy()
        save = []
        y = self.proEscalar(al,self.keyPrivA)
        k = self.proEscalar(y, self.keyPrivB)
        for i in range(len(c)):
            p1 = self.sums(c[i][0], self.inAd(k))
            p2 = self.sums(c[i][1], self.inAd(k))
            d1 = self.log(p1, al)
            d2 = self.log(p2, al)
            c = [d1,d2]
            save.append(c)
        m = self.intToText(save)
        return m