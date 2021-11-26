import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

from ClassCript import CripDesplazamiento
from cripConve import *
from GIU.desp import *
from GIU.despCriAn import *

class main_Windows(QMainWindow):

    def __init__(self):
        super(main_Windows, self).__init__()
        uic.loadUi("mainWin.ui", self)
        self.bCripClasica.clicked.connect(self.abrir)

    def abrir(self):
        cripC = main_cripConve()
        widget.addWidget(cripC)
        widget.setCurrentIndex(widget.currentIndex()+1)


class main_cripConve(QMainWindow):

    def __init__(self):
        super(main_cripConve, self).__init__()
        uic.loadUi("cripConve.ui", self)
        self.bDesplazamiento.clicked.connect(self.abrirDesp)


    def abrirDesp(self):
        cripDesp = main_cripDesp()
        widget.addWidget(cripDesp)
        widget.setCurrentIndex(widget.currentIndex()+1)


class main_cripDesp(QMainWindow):

    def __init__(self):
        super(main_cripDesp, self).__init__()
        uic.loadUi("desp.ui", self)
        self.cript = CripDesplazamiento('', 0)
        self.decript = CripDesplazamiento('', 0)
        self.cripAn.clicked.connect(self.abrirDespC)
        self.encr.clicked.connect(self.encriptar)
        self.decr.clicked.connect(self.desencriptar)

    def abrirDespC(self):
        cripDespC = main_cripDespC()
        widget.addWidget(cripDespC)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def encriptar(self):
        self.cript.data = self.encrIn.toPlainText()
        self.cript.m = self.encrSpin.value()
        self.encrOut.setText(self.cript.encriptar())

    def desencriptar(self):
        self.decript.data = self.decrIn.toPlainText()
        self.decript.m = self.decrSpin.value()
        self.decrOut.setText(self.decript.desencriptar())


class main_cripDespC(QMainWindow):

    def __init__(self):
        super(main_cripDespC, self).__init__()
        uic.loadUi("despCriAn.ui", self)
        self.cript = CripDesplazamiento('', 0)
        self.ciDes.clicked.connect(self.abrirDesp)
        self.criAn.clicked.connect(self.criptanalisis)

    def abrirDesp(self):
        cripDesp = main_cripDesp()
        widget.addWidget(cripDesp)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def criptanalisis(self):
        self.cript.data = self.caIn.toPlainText()
        words = ''
        for i in range(25):
            self.cript.m = i
            words += self.cript.desencriptar()+'\n '
        self.cript.m = 25
        words += self.cript.desencriptar()
        self.caOut.setText(words)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    mainW = main_Windows()
    widget.addWidget(mainW)
    widget.setFixedHeight(613)
    widget.setFixedWidth(1000)
    widget.show()
    sys.exit(app.exec())