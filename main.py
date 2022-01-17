from ClassAES import ClassAES
from ClassDes64 import *
import imageio as iio
import imageio as iio2
import numpy as np
import matplotlib.pyplot as plt
from skimage import img_as_ubyte

from ProcIMG import ProcIMG
from AESIMG import ProcIMG

if __name__ == '__main__':
    # p=[[[0,255,0],[255,0,255],[230,1,2],[0, 255, 0]],
    #  [[0,255,0],[255,0,255],[1,1,1],[0, 255, 0]]]
    # m,n=4,2
    # p = iio.imread('test3.png')
    # q = iio.imread('result1.png')
    # iio.imsave('result2.jpg',img_as_ubyte(p))
    # n, m, b = p.shape
    # p=list(p)
    # crip = ProcIMG(p,m,n)
    # crip.codificarDes64()
    # q= crip.darResultado()
    # print(q)
    # iio.imsave('result3.png',q)
    # print("a decodificar")
    # crip.decodificarDes64()
    # r= crip.darResultado()
    # print(r==p)
    # iio2.imsave('test3-1.png',r)

    # new = ClassAES([0x54, 0x77, 0x6f, 0x20, 0x4f, 0x6e, 0x65, 0x20, 0x4e, 0x69, 0x6e, 0x65, 0x20, 0x54,
    #                0x77, 0x6f], 'Thats my Kung Fu')
    # print(new.encriptar())
    # new2 = ClassAES(new.encriptar(), 'Thats my Kung Fu')
    # print(new2.desencriptar())
    #p = iio.imread('test3.png')
    q = iio.imread('resultctr3.png')
    crip = ProcIMG(q, 'Thats my Kung Fu')
    iio.imsave('resultctrd3.png', crip.e_ctrAES([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]))

