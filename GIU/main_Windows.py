import sys
from random import sample

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from pyqt5_plugins.examplebutton import QtWidgets
from pyqt5_plugins.examplebuttonplugin import QtGui

from ClassCript import CripDesplazamiento, CripSustitucion, CripVigenere


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
        self.bVigenere.clicked.connect(self.abrirCripVige)
        self.bSustitucion.clicked.connect(self.abrirCripSust)


    def abrirDesp(self):
        cripDesp = main_cripDesp()
        widget.addWidget(cripDesp)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def abrirCripVige(self):
        cripVige = main_cripVige()
        widget.addWidget(cripVige)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def abrirCripSust(self):
        cripSus = main_cripConveSustV()
        widget.addWidget(cripSus)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class main_cripConveSustV(QMainWindow):

    def __init__(self, parent = None):
        self.flush = []
        super(main_cripConveSustV, self).__init__()
        uic.loadUi("cripConveSust.ui", self)
        self.bGenerar.clicked.connect(self.generarV)
        self.bEncriptar.clicked.connect(self.encriptarV)
        self.bDesencriptar.clicked.connect(self.desEncriptarV)
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
            vent2 = main_errorDialogV(self)
            vent2.tipoError("No hay texto que cifrar")
            vent2.show()

    def desEncriptarV(self):
        self.lineEdit.setDisabled(False)
        data = self.textEdit_2.toPlainText().upper()
        data = data.replace('\n', "")
        self.textEdit_2.setPlainText(data)

        if len(data)!=0 :
            flush = self.lineEdit.text()
            b = list(flush)
            self.flush = b
            crip1 = CripSustitucion(data,b)
            dataEncrip = crip1.desencriptar()
            self.textEdit.setPlainText(dataEncrip)

        else :
            vent2 = main_errorDialogV(self)
            vent2.tipoError("No hay texto que cifrar")
            vent2.show()




    def salirV(self):
        vent2 = main_cripConve(self)
        vent2.show()
        self.hide()

class main_errorDialogV(QDialog):
    def __init__(self):
        super(main_errorDialogV, self).__init__()
        uic.loadUi("errorDialog.ui", self)
        self.bOk.clicked.connect(self.close)

        #forma de llamar este dialogo de error en sus ventanas
        '''vent2 = errorDialogV(self)
        vent2.tipoError("505")
        vent2.show()'''

    def tipoError(self, error):
        self.label.setText(error)


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


class main_cripVige(QMainWindow):

    def __init__(self):
        super(main_cripVige, self).__init__()
        uic.loadUi("cripVige.ui", self)
        self.cript = CripVigenere('', 'Password')
        self.decript = CripVigenere('', 'Password')
        self.cripAn.clicked.connect(self.abrirVigeC)
        self.encr.clicked.connect(self.encriptar)
        self.decr.clicked.connect(self.desencriptar)

    def abrirVigeC(self):
        cripVigeC = main_cripVigeC()
        widget.addWidget(cripVigeC)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def encriptar(self):
        self.cript.data = self.encrIn.toPlainText()
        self.cript.key = self.encrPwd.toPlainText()
        self.encrOut.setText(self.cript.encriptar())

    def desencriptar(self):
        self.decript.data = self.decrIn.toPlainText()
        self.decript.key = self.decrPwd.toPlainText()
        self.decrOut.setText(self.decript.desencriptar())


class main_cripVigeC(QMainWindow):

    def __init__(self):
        super(main_cripVigeC, self).__init__()
        uic.loadUi("cripVigeCriAn.ui", self)
        self.keys = []
        self.indexer = 0
        self.cript = CripVigenere('', 'pass')
        self.ciDes.clicked.connect(self.abrirVige)
        self.get_keys.clicked.connect(self.criptanalisis)
        self.decr.clicked.connect(self.desencriptar)
        self.next_key.clicked.connect(self.siguiente)

    def abrirVige(self):
        cripVige = main_cripVige()
        widget.addWidget(cripVige)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def criptanalisis(self):
        self.cript.data = self.caIn.toPlainText()
        self.keys = self.cript.criptanalisis()
        self.poss_key_l.setText(str(self.keys[0]))
        self.poss_key.setText(self.cript.criptanalisis_key(self.keys[0]))

    def siguiente(self):
        if self.indexer < len(self.keys)-1:
            self.indexer += 1
            self.poss_key_l.setText(str(self.keys[self.indexer]))
            self.poss_key.setText(self.cript.criptanalisis_key(self.keys[self.indexer]))


    def desencriptar(self):
        self.cript.data = self.caIn.toPlainText()
        temp = QtGui.QTextDocument()
        temp.setHtml(self.poss_key.text())
        self.cript.key = temp.toPlainText()
        self.caOut.setText(self.cript.desencriptar())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    mainW = main_Windows()
    widget.addWidget(mainW)
    widget.setFixedHeight(613)
    widget.setFixedWidth(1000)
    widget.show()
    sys.exit(app.exec())
