
from ClassRSA import ClassRSA
import math as m

if __name__ == '__main__':

    crip = ClassRSA()
    crip.generarKey()
    print(crip.p, crip.q,(crip.p-1)*(crip.q-1), crip.n, crip.e)
    c=crip.encriptar("1234523942341")
    print(c)
    c2 = (''.join(map(lambda x: str(x), c)))
    print(c2)
    print(crip.desencriptar(c))

