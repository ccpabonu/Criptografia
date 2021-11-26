import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from cripConve import *
from GIU.desp import *
from GIU.despCriAn import *

class main_Windows(QMainWindow):

    def __init__(self):
        super(main_Windows, self).__init__()
        uic.loadUi("mainWin.ui", self)
        self.bCripClasica.clicked.connect(self.abrir)

    def abrir(self):
        widget.setCurrentIndex(widget.currentIndex()+1)
        cripDesp = main_cripDesp()
        widget.addWidget(cripDesp)

#
#    def abrir (self):
#        self.ventana = QtWidgets.QMainWindow()
#        self.ui=Ui_cripConve()
#        self.ui.setupUi(self.ventana)
#        self.ventana.show()
#        self.ventana.bDesplazamiento.clicked.connect(self.abrirDesp)
#        self.close()


#    def abrirDesp(self):
#        self.ventana_d = QtWidgets.QMainWindow()
#        self.ui2=Ui_cripDesp()
#        self.ui2.setupUi(self.ventana_d)
#        self.ventana_d.show()
#        self.ventana.close()
class main_cripConve(QMainWindow):

    def __init__(self):
        super(main_cripConve, self).__init__()
        uic.loadUi("cripConve.ui", self)
        self.bDesplazamiento.clicked.connect(self.abrirDesp)


    def abrirDesp(self):
        widget.setCurrentIndex(widget.currentIndex()+1)
        cripDespC = main_cripDespC()
        widget.addWidget(cripDespC)


class main_cripDesp(QMainWindow):

    def __init__(self):
        super(main_cripDesp, self).__init__()
        uic.loadUi("desp.ui", self)
        self.cripAn.clicked.connect(self.abrirDespC)

    def abrirDespC(self):
        widget.setCurrentIndex(widget.currentIndex() + 1)
        #cripDespC = main_cripDespC()
        #widget.addWidget(cripDespC)


class main_cripDespC(QMainWindow):

    def __init__(self):
        super(main_cripDespC, self).__init__()
        uic.loadUi("despCriAn.ui", self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    mainW = main_Windows()
    cripC = main_cripConve()
    widget.addWidget(mainW)
    widget.addWidget(cripC)
    widget.setFixedHeight(613)
    widget.setFixedWidth(1000)
    widget.show()
    sys.exit(app.exec())