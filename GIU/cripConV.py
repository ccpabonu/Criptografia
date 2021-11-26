import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from cripConve import *
from GIU.desp import *
from GIU.despCriAn import *

class cripConV(QMainWindow):

    def __init__(self):
        super(cripConV, self).__init__()
        uic.loadUi("cripConve.ui", self)
        self.bDesplazamiento.clicked.connect(self.abrir)
        self.show()


    def abrir (self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ui_cripDesp()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
        self.hide()

    def mostrar(self):
        self.show()