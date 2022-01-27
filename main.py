from ClassCript import CripHill2
from ClassDes64 import *
import imageio as iio
import imageio as iio2
import numpy as np
import matplotlib.pyplot as plt
#from skimage import img_as_ubyte
from ClassRSA import ClassRSA
from ProcIMG import ProcIMG
from AESIMG import ProcIMG, HillIMG

if __name__ == '__main__':

    crip = ClassRSA()
    print(crip.q*crip.p)