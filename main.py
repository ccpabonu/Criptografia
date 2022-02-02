
from ClassRSA import ClassRSA
import math as m

if __name__ == '__main__':

    crip = ClassRSA()
    #crip.generarKey()
    crip.kPublica = (307001,208091)
    crip.kPrivada = (307001, 188375)
    print(crip.p, crip.q,(crip.p-1)*(crip.q-1), crip.n, crip.e)
    c=crip.encriptar("12345678")
    print(c)
    print(type(c[0]))
    c2 = (''.join(map(lambda x: str(x), c)))
    print(c2)
    print(crip.desencriptar(c))

