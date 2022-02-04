from ClassGamal import ClassGamal
from ClassRSA import ClassRSA
import math as m

if __name__ == '__main__':

    crip = ClassGamal()
    #s = crip.proEscalar([24,5],13)
    #print(crip.textToInt("hola"))
    #
    crip.a = 50
    crip.b = 24
    crip.p = 61
    crip.keyPrivA = 967
    crip.keyPrivB = 17
    crip.privK= 252
    crip.puntosElip()
    print(crip.cifrar("ho"))
    print(crip.descifrar([[[38, 26], [53, 37]], [[38, 26], [11, 21]]]))
    #print(crip.descifrar([[[38, 26], [53, 37]], [[38, 26], [11, 21]], [[38, 26], [24, 46]], [[38, 26], [29, 11]]]))
    #print(((4*99*99*99)+27*2*2)%307)


