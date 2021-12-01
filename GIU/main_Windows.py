import sys
from random import sample

from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QTableWidgetItem


from ClassCript import *


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
        self.bPermutacion.clicked.connect(self.abrirCripPerm)
        self.bHill.clicked.connect(self.abrirHill)
        self.bAfin.clicked.connect(self.abrirAfin)

    def abrirDesp(self):
        cripDesp = main_cripDesp()
        widget.addWidget(cripDesp)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def abrirHill(self):
        cripHill = main_encrHill()
        widget.addWidget(cripHill)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def abrirAfin(self):
        cripAfin = main_encrAfin()
        widget.addWidget(cripAfin)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def abrirCripVige(self):
        cripVige = main_cripVige()
        widget.addWidget(cripVige)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def abrirCripSust(self):
        cripSus = main_cripConveSustV()
        widget.addWidget(cripSus)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def abrirCripPerm(self):
        ventana2 = main_cripConvePerm()
        widget.addWidget(ventana2)
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
        data = data.replace('\n', "")
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
        self.tableWidget.clear()
        data = self.textEdit_2.toPlainText().upper()
        data = data.replace('\n', "")
        data = data.replace(' ', "")
        flush = self.lineEdit.text()
        b = list(flush)
        crip1 = CripSustitucion(data, b)
        m = crip1.cripAnalisis()
        listCrip = list(m.items())
        fila = 0
        for i in listCrip:
            columna = 0
            self.tableWidget.insertRow(fila)
            for j in i:
                celda = QTableWidgetItem(str(j))
                self.tableWidget.setItem(fila, columna, celda)
                columna += 1
            fila += 1

class main_cripConvePerm(QMainWindow):
    def __init__(self):
        super(main_cripConvePerm, self).__init__()
        uic.loadUi("cripConvePerm.ui", self)
        self.bGenerar.clicked.connect(self.generarV)
        self.bEncriptar.clicked.connect(self.encriptarV)
        self.bDesencriptar.clicked.connect(self.desEncriptarV)
        self.bAtras.clicked.connect(self.salirV)
        self.bCriptoanalisis.clicked.connect(self.cripAnalisisV)


    def generarV(self):
        self.z=int(self.encrSpin.value())
        self.arr =[]
        for i in range(self.z):
            self.arr.append(int(i))
        self.arr = sample(self.arr,self.z)
        self.lineEdit.setText("-".join([str(_) for _ in self.arr]))

    def encriptarV(self):
        data = self.textEdit.toPlainText().lower()
        data = data.replace('\n', "")
        data = data.replace(' ', "")
        self.textEdit.setPlainText(data)
        self.z=int(self.encrSpin.value())
        d= self.lineEdit.text()
        d = d.replace('-',"")
        arg = list(d)
        arg = [int(x) for x in arg]
        cripPerm= CripPermutacion(data,self.z,arg)
        dataEncrip = cripPerm.encriptar()
        self.textEdit_2.setPlainText(dataEncrip)

    def desEncriptarV(self):

        data = self.textEdit_2.toPlainText().upper()
        data = data.replace('\n', "")
        data = data.replace(' ', "")
        self.textEdit_2.setPlainText(data)
        self.z = int(self.encrSpin.value())
        d = self.lineEdit.text()
        d = d.replace('-', "")
        arg = list(d)
        arg = [int(x) for x in arg]
        cripPerm = CripPermutacion(data, self.z,arg)
        dataDes= cripPerm.desencriptar()
        self.textEdit.setPlainText(dataDes)


    def cripAnalisisV(self):
        self.listWidget.clear()
        data = self.textEdit_2.toPlainText().upper()
        data = data.replace('\n', "")
        data = data.replace(' ', "")
        self.textEdit_2.setPlainText(data)
        self.z = int(self.encrSpin.value())
        d = self.lineEdit.text()
        d = d.replace('-', "")
        arg = list(d)
        arg = [int(x) for x in arg]
        crip1 = CripPermutacion(data,self.z,arg)
        liste = crip1.cripAnalisis()
        j=1
        for i in liste:
            self.listWidget.addItem(str(j)+"- "+i)
            j += 1


    def salirV(self):
        ventana2 = main_cripConve()
        widget.addWidget(ventana2)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class main_cripDesp(QMainWindow):

    def __init__(self):
        super(main_cripDesp, self).__init__()
        uic.loadUi("desp.ui", self)
        self.cript = CripDesplazamiento('', 0)
        self.decript = CripDesplazamiento('', 0)
        self.cripAn.clicked.connect(self.abrirDespC)
        self.encr.clicked.connect(self.encriptar)
        self.decr.clicked.connect(self.desencriptar)
        self.back.clicked.connect(self.backMenu)

    def abrirDespC(self):
        cripDespC = main_cripDespC()
        widget.addWidget(cripDespC)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def backMenu(self):
        cripConve = main_cripConve()
        widget.addWidget(cripConve)
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
        self.back.clicked.connect(self.backMenu)

    def abrirDesp(self):
        cripDesp = main_cripDesp()
        widget.addWidget(cripDesp)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def backMenu(self):
        cripConve = main_cripConve()
        widget.addWidget(cripConve)
        widget.setCurrentIndex(widget.currentIndex() + 1)

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
        self.back.clicked.connect(self.backMenu)

    def abrirVigeC(self):
        cripVigeC = main_cripVigeC()
        widget.addWidget(cripVigeC)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def backMenu(self):
        cripConve = main_cripConve()
        widget.addWidget(cripConve)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def encriptar(self):
        self.cript.data = self.encrIn.toPlainText().replace(" ", "").lower()
        self.cript.key = self.encrPwd.text().replace(" ", "").lower()
        self.encrOut.setText(self.cript.encriptar())

    def desencriptar(self):
        self.decript.data = self.decrIn.toPlainText().replace(" ", "").lower()
        self.decript.key = self.decrPwd.text().replace(" ", "").lower()
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
        self.back.clicked.connect(self.backMenu)

    def abrirVige(self):
        cripVige = main_cripVige()
        widget.addWidget(cripVige)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def backMenu(self):
        cripConve = main_cripConve()
        widget.addWidget(cripConve)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def criptanalisis(self):
        if len(self.caIn.toPlainText().replace(" ", "").lower())>0:
            self.cript.data = self.caIn.toPlainText().replace(" ", "").lower()
            self.cript.changeMax(self.amount.value())
            self.indexer = 0
            self.keys = self.cript.criptanalisis()
            self.poss_key_l.setText(str(self.keys[0]))
            self.poss_key.setText(self.cript.criptanalisis_key(self.keys[0]))

    def siguiente(self):
        if self.indexer < len(self.keys)-1:
            self.indexer += 1
            self.poss_key_l.setText(str(self.keys[self.indexer]))
            self.poss_key.setText(self.cript.criptanalisis_key(self.keys[self.indexer]))


    def desencriptar(self):
        self.cript.data = self.caIn.toPlainText().replace(" ", "").lower()
        temp = QtGui.QTextDocument()
        temp.setHtml(self.poss_key.text())
        self.cript.key = temp.toPlainText().replace(" ", "").lower()
        self.caOut.setText(self.cript.desencriptar())


class main_encrHill(QMainWindow):

    def __init__(self):
        super(main_encrHill, self).__init__()
        uic.loadUi("encrHillWindow.ui", self)
        self.cript = CripHill('', '')
        self.decript = CripHill('', '')
        self.keyBotton.clicked.connect(self.keysE)
        self.keyBottonD.clicked.connect(self.keysD)
        self.encriptar1.clicked.connect(self.encriptar)
        self.desencriptar1.clicked.connect(self.desencriptar)
        self.cripAn.clicked.connect(self.abrirHillC)
        self.back.clicked.connect(self.backMenu)

    def keysE(self):
        self.cript.key = self.keyInput.text()
        if len(self.cript.key) > 1:
            self.cript.setObject()
            if self.cript.boo == 1:
                self.encrOut.setText('Clave invalida, su matriz no es coprima con 26')
            else:
                self.encrOut.setText('')

    def keysD(self):
        self.decript.key = self.keyInputD.text()
        if len(self.decript.key) > 1:
            self.decript.setObject()
            if self.decript.boo == 1:
                self.decrOut.setText('Clave invalida, su matriz no es coprima con 26')
            else:
                self.decrOut.setText('')

    def backMenu(self):
        cripConve = main_cripConve()
        widget.addWidget(cripConve)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def abrirHillC(self):
        cripHillC = main_encrHillC()
        widget.addWidget(cripHillC)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def encriptar(self):
        if len(self.plainText.toPlainText())>0 and self.cript.n>0:
            if self.cript.boo==0:
                self.cript.data = self.plainText.toPlainText()
                self.encrOut.setText(self.cript.encriptar())


    def desencriptar(self):
        if len(self.plainTextD.toPlainText()) > 0 and self.decript.n>0:
            if self.decript.boo == 0:
                self.decript.data = self.plainTextD.toPlainText()
                self.decrOut.setText(self.decript.desencriptar())


class main_encrHillC(QMainWindow):

    def __init__(self):
        super(main_encrHillC, self).__init__()
        uic.loadUi("analisCriptHill.ui", self)
        self.decript = CripHill('', 'aa')
        self.cA.clicked.connect(self.criptoanalisis)
        self.ciDes.clicked.connect(self.abrirHill)
        self.back.clicked.connect(self.backMenu)

    def backMenu(self):
        cripConve = main_cripConve()
        widget.addWidget(cripConve)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def abrirHill(self):
        cripHill = main_encrHill()
        widget.addWidget(cripHill)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def criptoanalisis(self):
        if self.cIn.toPlainText().isalpha() and self.mValue.text().isnumeric() and self.cipher.toPlainText().isalpha():
            self.decript.data = self.cIn.toPlainText().lower()
            self.decript.setObject()
            self.cOut.setText(str(self.decript.criptanalisis(self.cipher.toPlainText(), int(self.mValue.text()))))
        else:
            self.cOut.setText('Incorrect input')



class main_encrAfin(QMainWindow):

    def __init__(self):
        super(main_encrAfin, self).__init__()
        uic.loadUi("sAfinWindow.ui", self)
        self.cript = CripAfin('', 0, 0)
        self.decript = CripAfin('', 0, 0)
        self.Encriptar.clicked.connect(self.encriptar)
        self.Desencriptar.clicked.connect(self.desencriptar)
        self.cripAn.clicked.connect(self.abrirAfinC)
        self.back.clicked.connect(self.backMenu)

    def backMenu(self):
        cripConve = main_cripConve()
        widget.addWidget(cripConve)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def encriptar(self):
        self.cript.a = self.eSpinA.value()
        self.cript.b = self.eSpinB.value()
        self.cript.data = self.eIn.toPlainText()
        self.eOut.setText(self.cript.encriptar())

    def abrirAfinC(self):
        cripAfinC = main_encrAfinC()
        widget.addWidget(cripAfinC)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def desencriptar(self):
        self.decript.a = self.dSpinA.value()
        self.decript.b = self.dSpinB.value()
        self.decript.data = self.dIn.toPlainText()
        self.dOut.setText(self.decript.desencriptar())


class main_encrAfinC(QMainWindow):

    def __init__(self):
        super(main_encrAfinC, self).__init__()
        uic.loadUi("sAfinCriptoAnalisis.ui", self)
        self.decript = CripAfin('', 1, 0)
        self.cA.clicked.connect(self.criptoanalisis)
        self.ciDes.clicked.connect(self.abrirAfin)
        self.back.clicked.connect(self.backMenu)

    def backMenu(self):
        cripConve = main_cripConve()
        widget.addWidget(cripConve)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def abrirAfin(self):
        cripAfin = main_encrAfin()
        widget.addWidget(cripAfin)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def criptoanalisis(self):
        self.decript.data = self.eIn.toPlainText()
        words = ''
        listW = self.decript.criptanalisis()
        print(listW)
        for i in listW:
            words += i + '\n '
        print(words)
        self.eOut.setText(words)
        pass




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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    mainW = main_Windows()
    widget.addWidget(mainW)
    widget.setFixedHeight(613)
    widget.setFixedWidth(1000)
    widget.show()
    sys.exit(app.exec())
