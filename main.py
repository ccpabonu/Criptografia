from ClassDes64 import *
import imageio as iio
import numpy as np
import matplotlib.pyplot as plt
from skimage import img_as_ubyte

from ProcIMG import ProcIMG

if __name__ == '__main__':
    p=[[[0,255,0],[255,0,255],[230,1,2]],
      [[0,255,0],[255,0,255],[1,1,1]],
       [[0, 255, 0], [255, 0, 255], [230, 1, 2]]]
    m,n=3,3
    #p = iio.imread('test3.png')
    #q = iio.imread('result1.png')
    #iio.imsave('result2.jpg',img_as_ubyte(p))
    #n, m, b = p.shape
    crip = ProcIMG(p,m,n)
    crip.codificar3Des64()
    q= crip.darResultado()
    print(q)
    #iio.imsave('result3.png',q)
    crip.decodificar3Des64()
    r= crip.darResultado()
    print(r)
    #iio.imsave('test3-1.png',r)