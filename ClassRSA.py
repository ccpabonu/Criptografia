import random
import math as m

class ClassRSA :
    def __init__(self):
        self.p = 0
        self.q = 0
        #self.p = 53
        #self.q = 61
        self.n = 0
        self.e = 0
        self.d = 0
        self.kPublica = ()
        self.kPrivada = ()

    def primesInRange(self):
        prime_list = []
        for n in range(100, 1000):
            isPrime = True

            for num in range(2, n):
                if n % num == 0:
                    isPrime = False
            if isPrime:
                prime_list.append(n)
        randomPrime = random.choice(prime_list)
        return randomPrime

    def generarKey (self):
        self.p = self.primesInRange()
        self.q = self.primesInRange()
        self.n = self.q * self.p
        fn = (self.p-1)*(self.q-1)
        while True:
            x = random.randint(self.n//2, self.n)
            if m.gcd(fn, x) == 1:
                self.e = x
                break
        self.d = pow(self.e, -1, fn)
        self.kPublica = (self.n, self.e)
        self.kPrivada = (self.n, self.d)

    def encriptar(self,m):
        n, key = self.kPublica
        c = [(ord(char) ** key) % n for char in m]
        return c


    def desencriptar(self,c):
        n, key = self.kPrivada
        m = [chr((char ** key) % n) for char in c]
        return ''.join(m)
