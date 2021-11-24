# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from random import sample

from ClassCript import *


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    s = "holascomosestasbeb"
    example = CripPermutacion(s, 5)
    print(example.encriptar())
    print(example.desencriptar())
    ex= CripDesplazamiento(s,5)
    print(ex.encriptar())
    ex2=CripDesplazamiento(ex.encriptar(), 5)
    print(ex2.desencriptar())
    print(ex2.criptanalisis())
    ex3=CripVigenere(s, 'cipher')
    print(ex3.encriptar())
    ex4=CripVigenere(ex3.encriptar(),'cipher')
    print(ex4.desencriptar())
    stri = 'CHREEVOAHMAERATBIAXXWTNXBEEOPHBSBQMQEQERBWRVXUOAKXAOSXXWEAHBWGJMMQMNKGRFVGXWTRZXWIAKLXFPSKAUTEMNDCMGTSXMXBTUIADNGMGPSRELXNJELXVRVPRTULHDNQWTWDTYGBPHXTFALJHASVBFXNGLLCHRZBWELEKMSJIKNBHWRJGNMGJSGLXFEYPHAGNRBIEQJTAMRVLCRREMNDGLXRRIMGNSNRWCHRQHAEYEVTAQEBBIPEEWEVKAKOEWADREMXMTBHHCHRTKDNVRZCHRCLQOHPWQAIIWXNRMGWOIIFKEE'
    crypta = CripVigenere(stri, '')
    print(crypta.criptanalisis())
    print(crypta.criptanalisis_key(crypta.criptanalisis()[0]))
    print(crypta.desencriptar())




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
