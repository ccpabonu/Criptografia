# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sistemaAfinWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets, QLineEdit


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1023, 718)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label7.setFont(font)
        self.label7.setObjectName("label7")
        self.gridLayout.addWidget(self.label7, 8, 1, 2, 11)
        self.label8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label8.setFont(font)
        self.label8.setObjectName("label8")
        self.gridLayout.addWidget(self.label8, 10, 2, 1, 1)

        #Cajas de texto
        self.plainTextEdit1 = QLineEdit(self)
        self.plainTextEdit1.setObjectName("plainTextEdit1")
        self.gridLayout.addWidget(self.plainTextEdit1, 4, 0, 1, 1)
        self.plainTextEdit2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit2.setObjectName("plainTextEdit2")
        self.gridLayout.addWidget(self.plainTextEdit2, 10, 0, 1, 1)


        self.spinBox1_2 = QtWidgets.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.spinBox1_2.setFont(font)
        self.spinBox1_2.setObjectName("spinBox1_2")
        self.gridLayout.addWidget(self.spinBox1_2, 10, 3, 1, 1)
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.gridLayout.addWidget(self.label1, 0, 0, 1, 1)
        self.spinBox1 = QtWidgets.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        
        #spinbox1 = a
        self.spinBox1.setFont(font)
        self.spinBox1.setObjectName("spinBox1")
        self.gridLayout.addWidget(self.spinBox1, 4, 3, 1, 1)
        self.label5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label5.setFont(font)
        self.label5.setObjectName("label5")
        a = self.spin.valueChanged.connect(self.get_aValue) #Connnecting with the action to get the current value
        def get_aValue():
            aValue = self.spinBox1.value()
            return aValue
        


        #Spinbox2 = b
        self.spinBox2 = QtWidgets.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.spinBox2.setFont(font)
        self.spinBox2.setObjectName("spinBox2")
        b = self.spin.valueChanged.connect(self.get_bValue) #Connnecting with the action to get the current value
        self.gridLayout.addWidget(self.spinBox2, 4, 6, 1, 1)
        self.label6 = QtWidgets.QLabel(self.centralwidget)
        #Getting the current a value
        def get_bValue():
            bValue = self.spinBox1.value()
            return bValue
        


        self.gridLayout.addWidget(self.label5, 4, 2, 1, 1)
        self.returnToMenu = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.returnToMenu.setFont(font)
        self.returnToMenu.setAutoFillBackground(False)
        self.returnToMenu.setObjectName("returnToMenu")
        self.gridLayout.addWidget(self.returnToMenu, 0, 8, 1, 1)
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label3.setFont(font)
        self.label3.setObjectName("label3")
        self.gridLayout.addWidget(self.label3, 8, 0, 1, 1)
        self.label9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label9.setFont(font)
        self.label9.setObjectName("label9")
        self.gridLayout.addWidget(self.label9, 10, 5, 1, 1)

        #Boton encriptar
        self.encriptar = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.encriptar.setFont(font)
        self.encriptar.setObjectName("encriptar")
        self.button.clicked.connect(self.on_clickEnctriptar)


        #Conectar el boton con la funcion on_click
        def on_clickEncriptar(self):
            textboxValue = self.plainTextEdit1.text()
            #QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
            word = self.textbox.setText("")
            self.encoder(word, a, b)



        self.gridLayout.addWidget(self.encriptar, 5, 8, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(955, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 7, 0, 1, 12)
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.gridLayout.addWidget(self.label2, 2, 0, 1, 1)
        self.label4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label4.setFont(font)
        self.label4.setObjectName("label4")
        self.gridLayout.addWidget(self.label4, 2, 1, 2, 11)
        self.desencriptar = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.desencriptar.setFont(font)
        self.desencriptar.setObjectName("desencriptar")
        self.gridLayout.addWidget(self.desencriptar, 11, 8, 1, 1)


        
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label6.setFont(font)
        self.label6.setObjectName("label6")
        self.gridLayout.addWidget(self.label6, 4, 5, 1, 1)
        self.spinBox2_2 = QtWidgets.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.spinBox2_2.setFont(font)
        self.spinBox2_2.setObjectName("spinBox2_2")
        self.gridLayout.addWidget(self.spinBox2_2, 10, 6, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1023, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label7.setText(_translate("MainWindow", "Escoja la pareja que a su consideración forma la clave"))
        self.label8.setText(_translate("MainWindow", "a"))
        self.label1.setText(_translate("MainWindow", "Sistema Afin"))
        self.label5.setText(_translate("MainWindow", "a"))
        self.returnToMenu.setText(_translate("MainWindow", "Menu Principal"))
        self.label3.setText(_translate("MainWindow", "Cripto análisis"))
        self.label9.setText(_translate("MainWindow", "b"))
        self.encriptar.setText(_translate("MainWindow", "Encriptar"))
        self.label2.setText(_translate("MainWindow", "Texto Claro"))
        self.label4.setText(_translate("MainWindow", "Escoja la pareja que va a conformar la clave"))
        self.desencriptar.setText(_translate("MainWindow", "Desencriptar"))
        self.label6.setText(_translate("MainWindow", "b"))

    def encoder(word, aValue, bValue):
        modword = word.replace(" ", "")
        if not modword.isalpha(): return "Unacceptable input"
        wordascii = np.array([ord(c) for c in modword.lower()])
        wordencryption = (((wordascii * aValue) + bValue ) % 26) 
        encryption = [chr(c) for c in wordencryption]
        return ''.join(encryption)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
