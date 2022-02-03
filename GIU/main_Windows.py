import sys
from random import sample
import random
import imageio as iio
import imageio as iio2
import cv2
import imutils
import math as m

from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QTableWidgetItem, QFileDialog

from PyQt5.QtCore import QThread

from Class3Des64 import Class3Des64
from ClassCript import *
from ClassDes10 import ClassDes10
from ClassDes64 import ClassDes64
from ClassGamal import ClassGamal
from ClassRSA import ClassRSA
from ProcIMG import ProcIMG
from AESIMG import HillIMG
from loadDialog import loadDialog


class main_Windows(QMainWindow):

    def __init__(self):
        super(main_Windows, self).__init__()
        uic.loadUi("mainWin.ui", self)
        self.bCripClasica.clicked.connect(self.abrirConv)
        self.bCripBloque.clicked.connect(self.abrirBloq)
        self.bCripAsime.clicked.connect(self.abrirAsime)

    def abrirConv(self):
        cripC = main_cripConve()
        widget.addWidget(cripC)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def abrirBloq(self):
        cripB = main_cripBloq()
        widget.addWidget(cripB)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def abrirAsime(self):
        cripA = main_cripAsime()
        widget.addWidget(cripA)
        widget.setCurrentIndex(widget.currentIndex() + 1)


# <editor-fold desc="Encriptadores">

class EncriptadorDES(QThread):
    def __init__(self, cImg, dialog, cBox):
        super().__init__()
        self.cImg = cImg
        self.dialog = dialog
        self.cBox = cBox

    def run(self):
        save = str(self.cBox.currentText())
        print(save)
        if save == 'ECB':
            self.cImg.codificarDes64()
            q = self.cImg.darResultado()
        if save == 'CBC':
            self.cImg.codificarDes64CBC()
            q = self.cImg.darResultado()
        if save == 'CBF':
            self.cImg.codificarDes64CBF()
            q = self.cImg.darResultado()
        if save == 'OFB':
            self.cImg.codificarDes64OFB()
            q = self.cImg.darResultado()
        if save == 'CTR':
            self.cImg.codificarDes64CTR()
            q = self.cImg.darResultado()
        iio.imsave('result3.png', q)
        self.dialog.hide()


class DesencriptadorDES(QThread):

    def __init__(self, cImg, dialog, cBox):
        super().__init__()
        self.cImg = cImg
        self.dialog = dialog
        self.cBox = cBox

    def run(self):
        save = str(self.cBox.currentText())
        print(save)
        if save == 'ECB':
            self.cImg.decodificarDes64()
            q = self.cImg.darResultado()
        if save == 'CBC':
            self.cImg.decodificarDes64CBC()
            q = self.cImg.darResultado()
        if save == 'CBF':
            self.cImg.decodificarDes64CBF()
            q = self.cImg.darResultado()
        if save == 'OFB':
            self.cImg.decodificarDes64OFB()
            q = self.cImg.darResultado()
        if save == 'CTR':
            self.cImg.decodificarDes64CTR()
            q = self.cImg.darResultado()
        iio.imsave('result3-1.png', q)
        self.dialog.hide()


class Encriptador3DES(QThread):
    def __init__(self, cImg, dialog, cBox):
        super().__init__()
        self.cImg = cImg
        self.dialog = dialog
        self.cBox = cBox

    def run(self):
        save = str(self.cBox.currentText())
        print(save)
        if save == 'ECB':
            self.cImg.codificar3Des64()
            q = self.cImg.darResultado()
        if save == 'CBC':
            self.cImg.codificar3Des64CBC()
            q = self.cImg.darResultado()
        if save == 'CBF':
            self.cImg.codificar3Des64CBF()
            q = self.cImg.darResultado()
        if save == 'OFB':
            self.cImg.codificar3Des64OFB()
            q = self.cImg.darResultado()
        if save == 'CTR':
            self.cImg.codificar3Des64CTR()
            q = self.cImg.darResultado()
        iio.imsave('result3.png', q)
        self.dialog.hide()


class Desencriptador3DES(QThread):

    def __init__(self, cImg, dialog, cBox):
        super().__init__()
        self.cImg = cImg
        self.dialog = dialog
        self.cBox = cBox

    def run(self):
        save = str(self.cBox.currentText())
        print(save)
        if save == 'ECB':
            self.cImg.decodificar3Des64()
            q = self.cImg.darResultado()
        if save == 'CBC':
            self.cImg.decodificar3Des64CBC()
            q = self.cImg.darResultado()
        if save == 'CBF':
            self.cImg.decodificar3Des64CBF()
            q = self.cImg.darResultado()
        if save == 'OFB':
            self.cImg.decodificar3Des64OFB()
            q = self.cImg.darResultado()
        if save == 'CTR':
            self.cImg.decodificar3Des64CTR()
            q = self.cImg.darResultado()
        iio.imsave('result3-1.png', q)
        self.dialog.hide()


# </editor-fold>

# <editor-fold desc="CriptBloques">

class main_cripBloq(QMainWindow):

    def __init__(self):
        super(main_cripBloq, self).__init__()
        uic.loadUi("cripBloque.ui", self)
        self.bSDES.clicked.connect(self.abrirSDES)
        self.bDES.clicked.connect(self.abrirDES)
        self.b3DES.clicked.connect(self.abrir3DES)
        # self.bGamma.clicked.connect(self.abrirGamma)
        self.bAES.clicked.connect(self.abrirAES)
        self.back.clicked.connect(self.salir)

    def abrirSDES(self):
        cripSDES = main_encrSDES()
        widget.addWidget(cripSDES)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def abrirDES(self):
        cripDES = main_encrDES()
        widget.addWidget(cripDES)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def abrir3DES(self):
        crip3DES = main_encr3DES()
        widget.addWidget(crip3DES)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    # def abrirGamma(self):
    #     cripGamma = main_encrGamma()
    #     widget.addWidget(cripGamma)
    #     widget.setCurrentIndex(widget.currentIndex()+1)

    def abrirAES(self):
        cripAES = main_encrAES()
        widget.addWidget(cripAES)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def salir(self):
        ventana2 = main_Windows()
        widget.addWidget(ventana2)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class main_encrSDES(QMainWindow):

    def __init__(self):
        super(main_encrSDES, self).__init__()
        self.keys = []
        uic.loadUi("cripSDES.ui", self)
        self.c = ClassDes10()
        self.bGenerarKey.clicked.connect(self.generarKey)
        self.encr.clicked.connect(self.encriptar)
        self.decr.clicked.connect(self.desencriptar)

    def generarKey(self):
        h = self.c.generarKey()
        self.keys = self.c.keys
        self.encrPwd.setText(h)
        self.decrPwd.setText(h)
        self.encrPwd.setDisabled(True)
        self.decrPwd.setDisabled(True)

    def encriptar(self):
        text = self.encrText.toPlainText()
        self.c.text=text
        self.c.C = ""
        self.c.encriptar()
        self.desencrText.setPlainText(self.c.C)

    def desencriptar(self):
        self.c.keys = self.keys.copy()
        self.c.keys.reverse()
        text = self.desencrText.toPlainText()
        self.c.C = text
        self.c.D = ""
        self.c.desencriptar()
        self.encrText.setPlainText(self.c.D)



class main_encrDES(QMainWindow):

    def __init__(self):
        super(main_encrDES, self).__init__()
        self.desencriptador = None
        self.dialog = loadDialog(self)
        self.encriptador = None
        self.keyBin = []
        self.tmp = None
        self.image = None
        self.filename = None
        uic.loadUi("cripDES.ui", self)
        self.cImg = None
        self.c = ClassDes64()
        self.encr.clicked.connect(self.encriptar)
        self.imEn.clicked.connect(self.cargarImagen1)
        self.imDe.clicked.connect(self.cargarImagen2)
        self.decr.clicked.connect(self.desencriptar)
        self.back.clicked.connect(self.salir)
        self.bGenerarKey.clicked.connect(self.generarKey)

    def generarKey(self):
        h = self.c.generarKey()
        self.keyBin = self.c.keyBin
        h = h.upper()
        self.encrPwd.setText(h)
        self.decrPwd.setText(h)
        self.encrPwd.setDisabled(True)
        self.decrPwd.setDisabled(True)

    def encriptar(self):
        self.dialog.show()
        p = iio.imread(self.filename)
        n, m, b = p.shape
        p = list(p)
        self.cImg = ProcIMG(p, m, n)
        self.cImg.c.keyBin = self.keyBin
        self.cImg.c.IPKey()
        self.encriptador = EncriptadorDES(self.cImg, self.dialog, self.cBoxModo)
        self.encriptador.finished.connect(self.termino)
        self.encriptador.start()

    def termino(self):
        image = cv2.imread('result3.png')
        image = imutils.resize(image, width=640)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        self.img2.setPixmap(QtGui.QPixmap.fromImage(image))
        self.filename = 'result3.png'

    def cargarImagen1(self):
        self.filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        self.image = cv2.imread(self.filename)
        self.setPhoto(self.image, 1)

    def cargarImagen2(self):
        self.filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        self.image = cv2.imread(self.filename)
        self.setPhoto(self.image, 2)

    def setPhoto(self, image, n):
        self.tmp = image
        image = imutils.resize(image, width=640)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        if n == 1:
            self.img1.setPixmap(QtGui.QPixmap.fromImage(image))
        if n == 2:
            self.img2.setPixmap(QtGui.QPixmap.fromImage(image))

    def desencriptar(self):
        self.dialog.show()
        p = iio.imread(self.filename)
        n, m, b = p.shape
        p = list(p)
        self.cImg = ProcIMG(p, m, n)
        self.cImg.c.keyBin = self.keyBin
        self.cImg.c.IPKey()
        self.desencriptador = DesencriptadorDES(self.cImg, self.dialog, self.cBoxModo)
        self.desencriptador.finished.connect(self.termino2)
        self.desencriptador.start()

    def termino2(self):
        image = cv2.imread('result3-1.png')
        image = imutils.resize(image, width=640)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        self.img1.setPixmap(QtGui.QPixmap.fromImage(image))
        self.filename = 'result3-1.png'

    def salir(self):
        ventana2 = main_cripBloq()
        widget.addWidget(ventana2)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class main_encr3DES(QMainWindow):

    def __init__(self):
        super(main_encr3DES, self).__init__()
        self.desencriptador = None
        self.dialog = loadDialog(self)
        self.encriptador = None
        self.keyBin = []
        self.tmp = None
        self.image = None
        self.filename = None
        uic.loadUi("crip3DES.ui", self)
        self.cImg = None
        self.c3 = Class3Des64()
        self.encr.clicked.connect(self.encriptar)
        self.imEn.clicked.connect(self.cargarImagen1)
        self.imDe.clicked.connect(self.cargarImagen2)
        self.decr.clicked.connect(self.desencriptar)
        self.back.clicked.connect(self.salir)
        self.bGenerarKey.clicked.connect(self.generarKey)

    def generarKey(self):
        self.encrPwd.clear()
        self.decrPwd.clear()
        h = self.c3.generarKey()
        self.keyBin = self.c3.keysBin
        h = h.upper()
        h = h[2:]
        self.encrPwd.insertPlainText(h)
        self.decrPwd.insertPlainText(h)
        self.encrPwd.setDisabled(True)
        self.decrPwd.setDisabled(True)

    def encriptar(self):
        self.dialog.show()
        p = iio.imread(self.filename)
        n, m, b = p.shape
        p = list(p)
        self.cImg = ProcIMG(p, m, n)
        self.cImg.c3.keysBin = self.keyBin
        self.encriptador = Encriptador3DES(self.cImg, self.dialog, self.cBoxModo)
        self.encriptador.finished.connect(self.termino)
        self.encriptador.start()

    def termino(self):
        image = cv2.imread('result3.png')
        image = imutils.resize(image, width=640)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        self.img2.setPixmap(QtGui.QPixmap.fromImage(image))
        self.filename = 'result3.png'

    def cargarImagen1(self):
        self.filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        self.image = cv2.imread(self.filename)
        self.setPhoto(self.image, 1)

    def cargarImagen2(self):
        self.filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        self.image = cv2.imread(self.filename)
        self.setPhoto(self.image, 2)

    def setPhoto(self, image, n):
        self.tmp = image
        image = imutils.resize(image, width=640)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        if n == 1:
            self.img1.setPixmap(QtGui.QPixmap.fromImage(image))
        if n == 2:
            self.img2.setPixmap(QtGui.QPixmap.fromImage(image))

    def desencriptar(self):
        self.dialog.show()
        p = iio.imread(self.filename)
        n, m, b = p.shape
        p = list(p)
        self.cImg = ProcIMG(p, m, n)
        self.cImg.c3.keysBin = self.keyBin
        self.desencriptador = Desencriptador3DES(self.cImg, self.dialog, self.cBoxModo)
        self.desencriptador.finished.connect(self.termino2)
        self.desencriptador.start()

    def termino2(self):
        image = cv2.imread('result3-1.png')
        image = imutils.resize(image, width=640)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        self.img1.setPixmap(QtGui.QPixmap.fromImage(image))
        self.filename = 'result3-1.png'

    def salir(self):
        ventana2 = main_cripBloq()
        widget.addWidget(ventana2)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class main_encrAES(QMainWindow):

    def __init__(self):
        super(main_encrAES, self).__init__()
        uic.loadUi("cripAES.ui", self)
        self.imaEn = None
        self.imaDe = None
        self.pathEn = ''
        self.pathDe = ''
        self.encr.clicked.connect(self.encriptar)
        self.imEn.clicked.connect(self.selectEn)
        self.imDe.clicked.connect(self.selectDe)
        self.decr.clicked.connect(self.desencriptar)
        self.back.clicked.connect(self.salir)

    def encriptar(self):
        if self.pathEn != '':
            if len(self.iv.text()) != 16:
                print('cero')
            if (len(self.iv.text())!=16 or len(self.pwd.text())!=16) and self.mode.currentText() != 'ECB':
                print('uno')
                self.encrOut.setText('La contraseña y el IV deben ser de 16 caracteres ASCII')
                return
            if self.mode.currentText() == 'ECB' and len(self.pwd.text())!=16:
                print('dos')
                self.encrOut.setText('La contraseña debe ser de 16 caracteres ASCII')
                return
            p = iio.imread(self.pathEn)
            crip = ProcIMG(p, self.pwd.text())
            save = self.mode.currentText()
            temp = None
            if save == 'ECB':
                temp = crip.e_ecbAES()
            else:
                iv = np.array([ord(c) for c in self.iv.text()])
            if save == 'CBC':
                temp = crip.e_cbcAES(iv)
            if save == 'CBF':
                temp = crip.e_cfbAES(iv)
            if save == 'OFB':
                temp = crip.e_ofbAES(iv)
            if save == 'CTR':
                temp = crip.e_ctrAES(iv)
            iio.imsave('resultEn.png',temp)
            image = cv2.imread('resultEn.png')
            imutils.resize(image, width=250)
            frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
            self.encrOut.setPixmap(QtGui.QPixmap.fromImage(image))

    def desencriptar(self):
        if self.pathDe != '':
            if (len(self.iv.text()) != 16 or len(self.pwd.text()) != 16) and self.mode.currentText() != 'ECB':
                print('uno')
                self.decrOut.setText('La contraseña y el IV deben ser de 16 caracteres ASCII')
                return
            if self.mode.currentText() == 'ECB' and len(self.pwd.text()) != 16:
                print('dos')
                self.decrOut.setText('La contraseña debe ser de 16 caracteres ASCII')
                return
            p = iio.imread(self.pathDe)
            crip = ProcIMG(p, self.pwd.text())
            save = self.mode.currentText()
            temp = None
            if save == 'ECB':
                temp = crip.d_ecbAES()
            else:
                iv = np.array([ord(c) for c in self.iv.text()])
            if save == 'CBC':
                temp = crip.d_cbcAES(iv)
            if save == 'CBF':
                temp = crip.d_cfbAES(iv)
            if save == 'OFB':
                temp = crip.d_ofbAES(iv)
            if save == 'CTR':
                temp = crip.e_ctrAES(iv)
            iio.imsave('resultDe.png', temp)
            image = cv2.imread('resultDe.png')
            imutils.resize(image, width=250)
            frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
            self.decrOut.setPixmap(QtGui.QPixmap.fromImage(image))

    def selectEn(self):
        self.pathEn = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        image = cv2.imread(self.pathEn)
        imutils.resize(image, width=250)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        self.encrIn.setPixmap(QtGui.QPixmap.fromImage(image))

    def selectDe(self):
        self.pathDe = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        image = cv2.imread(self.pathDe)
        imutils.resize(image, width=250)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        self.decrIn.setPixmap(QtGui.QPixmap.fromImage(image))

    def salir(self):
        ventana2 = main_cripBloq()
        widget.addWidget(ventana2)
        widget.setCurrentIndex(widget.currentIndex() + 1)


# </editor-fold>

# <editor-fold desc="CriptClasica">

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
        self.back.clicked.connect(self.salir)

    def abrirDesp(self):
        cripDesp = main_cripDesp()
        widget.addWidget(cripDesp)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def abrirHill(self):
        cripHill = main_encrHill()
        widget.addWidget(cripHill)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def abrirAfin(self):
        cripAfin = main_encrAfin()
        widget.addWidget(cripAfin)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def abrirCripVige(self):
        cripVige = main_cripVige()
        widget.addWidget(cripVige)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def abrirCripSust(self):
        cripSus = main_cripConveSustV()
        widget.addWidget(cripSus)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def abrirCripPerm(self):
        ventana2 = main_cripConvePerm()
        widget.addWidget(ventana2)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def salir(self):
        ventana2 = main_Windows()
        widget.addWidget(ventana2)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class main_cripConveSustV(QMainWindow):

    def __init__(self, parent=None):
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
        self.flush = sample(data2, 26)
        self.lineEdit.setText("".join(self.flush))
        self.lineEdit.setDisabled(True)

    def encriptarV(self):
        data = self.textEdit.toPlainText().lower()
        data = data.replace('\n', "")
        data = data.replace(' ', "")
        self.textEdit.setPlainText(data)

        if len(data) != 0:
            flush = self.lineEdit.text()
            b = list(flush)
            self.flush = b
            crip1 = CripSustitucion(data, b)
            dataEncrip = crip1.encriptar()
            self.textEdit_2.setPlainText(dataEncrip)
        else:
            vent2 = main_errorDialogV(self)
            vent2.tipoError("No hay texto que cifrar")
            vent2.show()

    def desEncriptarV(self):
        self.lineEdit.setDisabled(False)
        data = self.textEdit_2.toPlainText().upper()
        data = data.replace('\n', "")
        data = data.replace(' ', "")
        self.textEdit_2.setPlainText(data)

        if len(data) != 0:
            flush = self.lineEdit.text()
            b = list(flush)
            self.flush = b
            crip1 = CripSustitucion(data, b)
            dataEncrip = crip1.desencriptar()
            self.textEdit.setPlainText(dataEncrip)

        else:
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
        self.z = int(self.encrSpin.value())
        self.arr = []
        for i in range(self.z):
            self.arr.append(int(i))
        self.arr = sample(self.arr, self.z)
        self.lineEdit.setText("-".join([str(_) for _ in self.arr]))

    def encriptarV(self):
        data = self.textEdit.toPlainText().lower()
        data = data.replace('\n', "")
        data = data.replace(' ', "")
        self.textEdit.setPlainText(data)
        self.z = int(self.encrSpin.value())
        d = self.lineEdit.text()
        d = d.replace('-', "")
        arg = list(d)
        arg = [int(x) for x in arg]
        cripPerm = CripPermutacion(data, self.z, arg)
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
        cripPerm = CripPermutacion(data, self.z, arg)
        dataDes = cripPerm.desencriptar()
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
        crip1 = CripPermutacion(data, self.z, arg)
        liste = crip1.cripAnalisis()
        j = 1
        for i in liste:
            self.listWidget.addItem(str(j) + "- " + i)
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
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def backMenu(self):
        cripConve = main_cripConve()
        widget.addWidget(cripConve)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def criptanalisis(self):
        self.cript.data = self.caIn.toPlainText()
        words = ''
        for i in range(25):
            self.cript.m = i
            words += self.cript.desencriptar() + '\n '
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
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def backMenu(self):
        cripConve = main_cripConve()
        widget.addWidget(cripConve)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def criptanalisis(self):
        if len(self.caIn.toPlainText().replace(" ", "").lower()) > 0:
            self.cript.data = self.caIn.toPlainText().replace(" ", "").lower()
            self.cript.changeMax(self.amount.value())
            self.indexer = 0
            self.keys = self.cript.criptanalisis()
            self.poss_key_l.setText(str(self.keys[0]))
            self.poss_key.setText(self.cript.criptanalisis_key(self.keys[0]))

    def siguiente(self):
        if self.indexer < len(self.keys) - 1:
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
        self.encr.clicked.connect(self.encriptar)
        self.decr.clicked.connect(self.desencriptar)
        self.back.clicked.connect(self.backMenu)
        self.imEn.clicked.connect(self.selectEn)
        self.imDe.clicked.connect(self.selectDe)
        self.bCA.clicked.connect(self.abrirHillC)

    def selectEn(self):
        self.pathEn = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        image = cv2.imread(self.pathEn)
        imutils.resize(image, width=250)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        self.encrIn.setPixmap(QtGui.QPixmap.fromImage(image))

    def selectDe(self):
        self.pathDe = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        image = cv2.imread(self.pathDe)
        imutils.resize(image, width=250)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        self.decrIn.setPixmap(QtGui.QPixmap.fromImage(image))

    def keysE(self):
        self.cript.key = self.keyInput.text()
        self.decript.key = self.keyInput.text()
        if len(self.cript.key) > 1:
            self.cript.setObject()
            if self.cript.boo == 1:
                self.encrOut.setText('Clave invalida, su matriz no es coprima con 26')
                self.decrOut.setText('Clave invalida, su matriz no es coprima con 26')
            else:
                self.encrOut.setText('')
                self.decrOut.setText('')


    def backMenu(self):
        cripConve = main_cripConve()
        widget.addWidget(cripConve)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def abrirHillC(self):
        cripHillC = main_encrHillC()
        widget.addWidget(cripHillC)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def encriptar(self):
        if len(self.plainTextD.toPlainText()) > 0 and self.decript.n > 0:
            if self.decript.boo == 0:
                p = iio.imread(self.pathEn)
                crip = HillIMG(p, self.keyInput.text())
                iio.imsave('resultHill.png', crip.e_hill())
                image = cv2.imread('resultHill.png')
                imutils.resize(image, width=250)
                frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
                self.encrOut.setPixmap(QtGui.QPixmap.fromImage(image))


    def desencriptar(self):
        if len(self.plainTextD.toPlainText()) > 0 and self.decript.n > 0:
            if self.decript.boo == 0:
                p = iio.imread(self.pathDe)
                crip = HillIMG(p, self.keyInput.text())
                iio.imsave('resultHilld.png', crip.d_hill())
                image = cv2.imread('resultHilld.png')
                imutils.resize(image, width=250)
                frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
                self.decrOut.setPixmap(QtGui.QPixmap.fromImage(image))


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
        widget.setCurrentIndex(widget.currentIndex() + 1)

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
        widget.setCurrentIndex(widget.currentIndex() + 1)

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
        widget.setCurrentIndex(widget.currentIndex() + 1)

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

        # forma de llamar este dialogo de error en sus ventanas
        '''vent2 = main_errorDialogV(self)
        vent2.tipoError("505")
        vent2.show()'''

    def tipoError(self, error):
        self.label.setText(error)


# </editor-fold>

# <editor-fold desc="CriptAsimetrica">

class main_cripAsime(QMainWindow):

    def __init__(self):
        super(main_cripAsime, self).__init__()
        uic.loadUi("cripAsime.ui", self)
        self.bRsa.clicked.connect(self.abrirRsa)
        self.back.clicked.connect(self.salir)
        self.bGamal.clicked.connect(self.abrirGamal)

    def abrirGamal(self):
        cripGamal = main_cripAsimeGamal()
        widget.addWidget(cripGamal)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def abrirRsa(self):
        cripRsa = main_cripAsimeRsa()
        widget.addWidget(cripRsa)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def salir(self):
        ventana2 = main_Windows()
        widget.addWidget(ventana2)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class main_cripAsimeRsa(QMainWindow):

    def __init__(self):
        super(main_cripAsimeRsa, self).__init__()
        uic.loadUi("cripAsimeRsa.ui", self)
        self.crip = ClassRSA()
        self.bGuardar.setVisible(False)
        self.bAtras.clicked.connect(self.salir)
        self.bGenerar.clicked.connect(self.generarKeys)
        self.bEncriptar.clicked.connect(self.encriptar)
        self.bDesencriptar.clicked.connect(self.desencriptar)
        self.bEditar.clicked.connect(self.editar)
        self.bGuardar.clicked.connect(self.guardar)

    def generarKeys(self):
        self.bGuardar.setVisible(False)
        self.bEditar.setVisible(True)
        self.crip.generarKey()
        self.lineP.setText(str(self.crip.p))
        self.lineQ.setText(str(self.crip.q))
        self.lineN.setText(str(self.crip.n))
        self.lineE.setText(str(self.crip.e))
        self.lineD.setText(str(self.crip.d))

    def encriptar(self):
        data = self.textCrip.toPlainText()
        data = data.replace('\n', "")
        data = data.replace(' ', "")
        c = self.crip.encriptar(data)
        self.textDesCrip.setPlainText((','.join(map(lambda x: str(x), c))))
        self.textCrip.clear()

    def desencriptar(self):
        data = str(self.textDesCrip.toPlainText())
        data = data.replace('\n', "")
        data = data.replace(' ', "")
        c = []
        n = ""
        for i in range(0, len(data)) :
            n = n + data[i]
            if data[i] == ",":
                n=n[:-1]
                c.append(int(n))
                n = ""
            if i == len(data)-1:
                c.append(int(n))
        m = self.crip.desencriptar(c)
        self.textCrip.setPlainText(m)
        self.textDesCrip.clear()

    def editar(self):
        self.lineP.setDisabled(False)
        self.lineQ.setDisabled(False)
        self.lineN.setDisabled(False)
        self.lineE.setDisabled(False)
        self.lineD.setDisabled(False)
        self.bEditar.setVisible(False)
        self.bGuardar.setVisible(True)

    def guardar(self):
        p = self.lineP.text()
        q = self.lineQ.text()
        n = self.lineN.text()
        e = self.lineE.text()
        d = self.lineD.text()
        if n =="" or e=="" or d=="":
            if p=="" and q=="" :
                vent2 = main_errorDialogV(self)
                vent2.tipoError("Campos vacios")
                vent2.show()
            else :
                if e != "" and d=="" :
                    self.crip.p = int(p)
                    self.crip.q = int(q)
                    self.crip.e = int(e)
                    self.crip.d = pow(self.crip.e, -1, (int(p)-1)*(int(q)-1))
                    self.crip.n = int(p)*int(q)
                    self.crip.kPublica = (int(p)*int(q), int(e))
                    self.crip.kPrivada = (int(p)*int(q), int(d))
                    self.lineD.setText(str(self.crip.d))
                if e == "" and d=="" :
                    self.crip.p = int(p)
                    self.crip.q = int(q)
                    self.crip.n = int(p)*int(q)
                    self.lineN.setText(str(self.crip.n))
                    fn = (self.crip.p - 1) * (self.crip.q - 1)
                    while True:
                        x = random.randint(self.crip.n // 2, self.crip.n)
                        if m.gcd(fn, x) == 1:
                            self.crip.e = x
                            break
                    self.crip.d = pow(self.crip.e, -1,fn)
                    self.crip.kPublica = (self.crip.n, self.crip.e)
                    self.crip.kPrivada = (self.crip.n, self.crip.d)
                    self.lineD.setText(str(self.crip.d))
                    self.lineE.setText(str(self.crip.e))
        else:
            self.crip.kPublica = (int(n), int(e))
            self.crip.kPrivada = (int(n),int(d))
        self.lineP.setDisabled(True)
        self.lineQ.setDisabled(True)
        self.lineN.setDisabled(True)
        self.lineE.setDisabled(True)
        self.lineD.setDisabled(True)
        self.bEditar.setVisible(True)
        self.bGuardar.setVisible(False)






    def salir(self):
        ventana2 = main_Windows()
        widget.addWidget(ventana2)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class main_cripAsimeGamal(QMainWindow):

    def __init__(self):
        super(main_cripAsimeGamal, self).__init__()
        uic.loadUi("cripAsimeGamal.ui", self)
        self.crip = ClassGamal()
        self.bGuardar.setVisible(False)
        self.bAtras.clicked.connect(self.salir)
        self.bGenerar.clicked.connect(self.generarKeys)
        self.bEncriptar.clicked.connect(self.encriptar)
        self.bDesencriptar.clicked.connect(self.desencriptar)
        #self.bEditar.clicked.connect(self.editar)
        #self.bGuardar.clicked.connect(self.guardar)

    def generarKeys(self):
        self.bGuardar.setVisible(False)
        self.bEditar.setVisible(True)
        self.crip.p = self.crip.primesInRange()
        self.crip.a = random.randint(1,100)
        self.crip.b = random.randint(1,100)
        self.crip.keyPrivA = self.crip.primesInRange()
        self.crip.puntosElip()
        self.lineP.setText(str(self.crip.p))
        self.lineA.setText(str(self.crip.a))
        self.lineB.setText(str(self.crip.b))
        self.lineK.setText(str(self.crip.keyPrivA))


    def encriptar(self):
        data = self.textCrip.toPlainText()
        data = data.replace('\n', "")
        data = data.replace(' ', "")
        c = self.crip.cifrar(data)
        save = str(c)

        self.textDesCrip.setPlainText(save)
        self.textCrip.clear()

    def desencriptar(self):
        data = str(self.textDesCrip.toPlainText())
        data = data.replace('\n', "")
        data = data.replace(' ', "")
        c = list(data)
        self.textCrip.setPlainText(m)
        self.textDesCrip.clear()

    def editar(self):
        self.lineP.setDisabled(False)
        self.lineQ.setDisabled(False)
        self.lineN.setDisabled(False)
        self.lineE.setDisabled(False)
        self.lineD.setDisabled(False)
        self.bEditar.setVisible(False)
        self.bGuardar.setVisible(True)

    def guardar(self):
        p = self.lineP.text()
        q = self.lineQ.text()
        n = self.lineN.text()
        e = self.lineE.text()
        d = self.lineD.text()
        if n =="" or e=="" or d=="":
            if p=="" and q=="" :
                vent2 = main_errorDialogV(self)
                vent2.tipoError("Campos vacios")
                vent2.show()
            else :
                if e != "" and d=="" :
                    self.crip.p = int(p)
                    self.crip.q = int(q)
                    self.crip.e = int(e)
                    self.crip.d = pow(self.crip.e, -1, (int(p)-1)*(int(q)-1))
                    self.crip.n = int(p)*int(q)
                    self.crip.kPublica = (int(p)*int(q), int(e))
                    self.crip.kPrivada = (int(p)*int(q), int(d))
                    self.lineD.setText(str(self.crip.d))
                if e == "" and d=="" :
                    self.crip.p = int(p)
                    self.crip.q = int(q)
                    self.crip.n = int(p)*int(q)
                    self.lineN.setText(str(self.crip.n))
                    fn = (self.crip.p - 1) * (self.crip.q - 1)
                    while True:
                        x = random.randint(self.crip.n // 2, self.crip.n)
                        if m.gcd(fn, x) == 1:
                            self.crip.e = x
                            break
                    self.crip.d = pow(self.crip.e, -1,fn)
                    self.crip.kPublica = (self.crip.n, self.crip.e)
                    self.crip.kPrivada = (self.crip.n, self.crip.d)
                    self.lineD.setText(str(self.crip.d))
                    self.lineE.setText(str(self.crip.e))
        else:
            self.crip.kPublica = (int(n), int(e))
            self.crip.kPrivada = (int(n),int(d))
        self.lineP.setDisabled(True)
        self.lineQ.setDisabled(True)
        self.lineN.setDisabled(True)
        self.lineE.setDisabled(True)
        self.lineD.setDisabled(True)
        self.bEditar.setVisible(True)
        self.bGuardar.setVisible(False)






    def salir(self):
        ventana2 = main_Windows()
        widget.addWidget(ventana2)
        widget.setCurrentIndex(widget.currentIndex() + 1)
# </editor-fold>


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    mainW = main_Windows()
    widget.addWidget(mainW)
    widget.setFixedHeight(613)
    widget.setFixedWidth(1000)
    widget.show()
    sys.exit(app.exec())
