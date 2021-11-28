import sys
from random import sample

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QTableWidgetItem

from ClassCript import CripDesplazamiento, CripSustitucion
#from cripConve import *
#from GIU.desp import *
#from GIU.despCriAn import *


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
        self.bSustitucion.clicked.connect(self.abrirCripSust)


    def abrirDesp(self):
        cripDesp = main_cripDesp()
        widget.addWidget(cripDesp)
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
        self.bCriptoanalisis.clicked.connect(self.cripAnalisisV)


    def generarV(self):
        data = self.lineEdit.text()
        data2 = list(data)
        self.flush= sample(data2,26)
        self.lineEdit.setText("".join(self.flush))
        self.lineEdit.setDisabled(True)

    def encriptarV(self):
        data = self.textEdit.toPlainText().lower()
        data = data.replace('\n',"")
        data = data.replace(' ', "")
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
        data = data.replace(' ', "")
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
        ventana2 = main_cripConve()
        widget.addWidget(ventana2)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def cripAnalisisV(self):
        data = self.textEdit_2.toPlainText().upper()
        data = data.replace('\n', "")
        data = data.replace(' ', "")
        flush = self.lineEdit.text()
        b = list(flush)
        crip1 = CripSustitucion(data,b)
        m= crip1.cripAnalisis()
        listCrip=list(m.items())
        fila = 0
        for i in listCrip:
            columna = 0
            self.tableWidget.insertRow(fila)
            for j in i:
                celda = QTableWidgetItem(str(j))
                self.tableWidget.setItem(fila,columna,celda)
                columna += 1
            fila +=1





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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    mainW = main_Windows()
    widget.addWidget(mainW)
    widget.setFixedHeight(613)
    widget.setFixedWidth(1000)
    widget.show()
    sys.exit(app.exec())
