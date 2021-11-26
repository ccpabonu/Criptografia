import sys
from random import sample


from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog

from ClassCript import *


class main_Windows(QMainWindow):

    def __init__(self):
        super(main_Windows, self).__init__()
        uic.loadUi("mainWin.ui", self)
        self.bCripClasica.clicked.connect(self.abrirCripClasica)


    def abrirCripClasica (self):
        self.hide()
        vent2 = cripConV(self)
        vent2.show()



class cripConV(QMainWindow):

    def __init__(self, parent = None):
        super(cripConV, self).__init__(parent)
        uic.loadUi("cripConve.ui", self)
        self.bDesplazamiento.clicked.connect(self.abrirCripDesp)
        self.bSustitucion.clicked.connect(self.abrirCripSust)

    def abrirCripDesp(self):
        self.hide()
        vent2 = cripDespV(self)
        vent2.show()

    def abrirCripSust(self):
        self.hide()
        vent2 = cripConveSustV(self)
        vent2.show()


class cripDespV(QMainWindow):

    def __init__(self, parent = None):
        super(cripDespV, self).__init__(parent)
        uic.loadUi("desp.ui", self)

class cripConveSustV(QMainWindow):

    def __init__(self, parent = None):
        self.flush = []
        super(cripConveSustV, self).__init__(parent)
        uic.loadUi("cripConveSust.ui", self)
        self.bGenerar.clicked.connect(self.generarV)
        self.bEncriptar.clicked.connect(self.encriptarV)
        #self.bDesencriptar.clicked.connect(self.desEncriptarV)
        self.bAtras.clicked.connect(self.salirV)


    def generarV(self):
        data = self.lineEdit.text()
        data2 = list(data)
        self.flush= sample(data2,26)
        self.lineEdit.setText("".join(self.flush))
        self.lineEdit.setDisabled(True)

    def encriptarV(self):
        data = self.textEdit.toPlainText().lower()
        data = data.replace('\n',"")
        self.textEdit.setPlainText(data)

        if len(data)!=0 :
            flush = self.lineEdit.text()
            b = list(flush)
            self.flush = b
            crip1 = CripSustitucion(data,b)
            dataEncrip = crip1.encriptar()
            self.textEdit_2.setPlainText(dataEncrip)
        else :
            vent2 = errorDialogV(self)
            vent2.tipoError("No hay texto que cifrar")
            vent2.show()

    def desEncriptaV(self):
        self.lineEdit.setDisabled(False)
        data = self.textEdit_2.toPlainText().upper()
        data = data.replace('\n', "")
        self.textEdit.setPlainText(data)

        if len(data)!=0 :
            flush = self.lineEdit.text()
            b = list(flush)
            self.flush = b
            crip1 = CripSustitucion(data,b)
            dataEncrip = crip1.desencriptar()
            self.textEdit.setPlainText(dataEncrip)

        else :
            vent2 = errorDialogV(self)
            vent2.tipoError("No hay texto que cifrar")
            vent2.show()




    def salirV(self):
        vent2 = cripConV(self)
        vent2.show()
        self.hide()

class errorDialogV(QDialog):
    def __init__(self, parent = None):
        super(errorDialogV, self).__init__(parent)
        uic.loadUi("errorDialog.ui", self)
        self.bOk.clicked.connect(self.close)

        #forma de llamar este dialogo de error en sus ventanas
        '''vent2 = errorDialogV(self)
        vent2.tipoError("505")
        vent2.show()'''

    def tipoError(self, error):
        self.label.setText(error)







if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = main_Windows()
    GUI.show()
    sys.exit(app.exec())