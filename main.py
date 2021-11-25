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
    efd = ['C', 'S', 'M', 'F', 'H', 'G', 'O', 'U', 'V', 'K', 'D', 'T', 'X', 'J', 'B', 'Q', 'W', 'N', 'Z', 'L', 'R', 'E', 'P', 'I', 'A', 'Y']
    s = "algorithmsarequitegeneraldefinitionsofarithmeticprocesses"
    s2 = "UBTCZMBXBZHZLCZSHS"
    s3 = "ROGLASMHTIUQERAEGETILARENNIFEDNOITIRAFOSEMHTIRPCITSSECOXXXSE"
    example = CripSustitucion(s, efd)
    example2 = CripSustitucion(s2, efd)
    example3 = CripPermutacion(s, 5 ,[4, 3, 2, 1, 0])
    example4 = CripPermutacion(s3, 5, [4, 3, 2, 1, 0])
    #print(example.encriptar())
    #print(example2.desencriptar())
    print(example3.encriptar())
    print(example4.desencriptar())
