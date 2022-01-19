from ClassDes64 import *
import imageio as iio
import imageio as iio2
import numpy as np
import matplotlib.pyplot as plt
from skimage import img_as_ubyte

from ProcIMG import ProcIMG

if __name__ == '__main__':

    #p=[[[0,255,0],[255,0,255],[230,1,2],[0, 255, 0]],
    #  [[0,255,0],[255,0,255],[1,1,1],[0, 255, 0]]]
    #m,n=4,2
    #p = iio.imread('test3.png')
    #q = iio.imread('result1.png')
    #n, m, b = p.shape
    #p=list(p)
    #crip = ProcIMG(p,m,n)
    #crip.codificar3Des64CTR()
    #q= crip.darResultado()
    #print(q)
    #iio.imsave('result3.png',q)
    #print("a decodificar")
    #crip.decodificar3Des64CTR()
    #r= crip.darResultado()
    #print(r)
    #iio2.imsave('test3-1.png',r)
    # iio2.imsave('test3-1.png',r)
    # p = iio.imread('test3.png')
    q = iio.imread('resultctr3.png')
    crip = ProcIMG(q, 'Thats my Kung Fu')
    iio.imsave('resultctrd3.png', crip.e_ctrAES([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]))