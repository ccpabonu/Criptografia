# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desp_stack.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_desp(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 500)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 500))
        MainWindow.setStyleSheet("background-color: rgb(45, 45, 45);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Top_Bar = QtWidgets.QFrame(self.centralwidget)
        self.Top_Bar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.Top_Bar.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Top_Bar.setObjectName("Top_Bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_toggle = QtWidgets.QFrame(self.Top_Bar)
        self.frame_toggle.setMaximumSize(QtCore.QSize(70, 40))
        self.frame_toggle.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.frame_toggle.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_toggle.setObjectName("frame_toggle")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Btn_Toggle = QtWidgets.QPushButton(self.frame_toggle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        self.Btn_Toggle.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px solid;")
        self.Btn_Toggle.setObjectName("Btn_Toggle")
        self.verticalLayout_2.addWidget(self.Btn_Toggle)
        self.horizontalLayout.addWidget(self.frame_toggle)
        self.frame_top = QtWidgets.QFrame(self.Top_Bar)
        self.frame_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.cripAn = QtWidgets.QPushButton(self.frame_top)
        self.cripAn.setGeometry(QtCore.QRect(200, 0, 151, 41))
        self.cripAn.setStyleSheet("background-color: rgb(21, 99, 165);\n"
"color: #00ffff;\n"
"font: 14pt \"Berlin Sans FB\";")
        self.cripAn.setObjectName("cripAn")
        self.ciDes = QtWidgets.QPushButton(self.frame_top)
        self.ciDes.setGeometry(QtCore.QRect(0, 0, 201, 41))
        self.ciDes.setStyleSheet("background-color: rgb(21, 99, 165);\n"
"color: #00ffff;\n"
"font: 14pt \"Berlin Sans FB\";")
        self.ciDes.setObjectName("ciDes")
        self.horizontalLayout.addWidget(self.frame_top)
        self.verticalLayout.addWidget(self.Top_Bar)
        self.Content = QtWidgets.QFrame(self.centralwidget)
        self.Content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Content.setObjectName("Content")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Content)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_pages = QtWidgets.QFrame(self.Content)
        self.frame_pages.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pages.setObjectName("frame_pages")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page_1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.widget_2 = QtWidgets.QWidget(self.page_1)
        self.widget_2.setObjectName("widget_2")
        self.decrIn = QtWidgets.QTextEdit(self.widget_2)
        self.decrIn.setGeometry(QtCore.QRect(550, 10, 341, 151))
        self.decrIn.setObjectName("decrIn")
        self.decrSpin = QtWidgets.QSpinBox(self.widget_2)
        self.decrSpin.setGeometry(QtCore.QRect(550, 180, 61, 41))
        self.decrSpin.setObjectName("decrSpin")
        self.encrIn = QtWidgets.QTextEdit(self.widget_2)
        self.encrIn.setGeometry(QtCore.QRect(73, 10, 341, 151))
        self.encrIn.setObjectName("encrIn")
        self.decr = QtWidgets.QPushButton(self.widget_2)
        self.decr.setGeometry(QtCore.QRect(740, 180, 151, 41))
        self.decr.setStyleSheet("background-color: rgb(21, 99, 165);\n"
"color: #00ffff;\n"
"font: 14pt \"Berlin Sans FB\";")
        self.decr.setObjectName("decr")
        self.decrOut = QtWidgets.QLabel(self.widget_2)
        self.decrOut.setGeometry(QtCore.QRect(550, 270, 341, 151))
        self.decrOut.setStyleSheet("background-color:rgba(0,0,0,50%);\n"
"color:\'white\';")
        self.decrOut.setText("")
        self.decrOut.setObjectName("decrOut")
        self.encrOut = QtWidgets.QLabel(self.widget_2)
        self.encrOut.setGeometry(QtCore.QRect(70, 270, 341, 151))
        self.encrOut.setStyleSheet("background-color:rgba(0,0,0,50%);\n"
"color:\'white\';")
        self.encrOut.setText("")
        self.encrOut.setObjectName("encrOut")
        self.encr = QtWidgets.QPushButton(self.widget_2)
        self.encr.setGeometry(QtCore.QRect(280, 180, 131, 41))
        self.encr.setStyleSheet("background-color: rgb(21, 99, 165);\n"
"color: #00ffff;\n"
"font: 14pt \"Berlin Sans FB\";")
        self.encr.setObjectName("encr")
        self.encrSpin = QtWidgets.QSpinBox(self.widget_2)
        self.encrSpin.setGeometry(QtCore.QRect(70, 180, 61, 41))
        self.encrSpin.setObjectName("encrSpin")
        self.verticalLayout_7.addWidget(self.widget_2)
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.widget_3 = QtWidgets.QWidget(self.page_2)
        self.widget_3.setObjectName("widget_3")
        self.caIn = QtWidgets.QTextEdit(self.widget_3)
        self.caIn.setGeometry(QtCore.QRect(120, 90, 551, 101))
        self.caIn.setObjectName("caIn")
        self.criAn = QtWidgets.QPushButton(self.widget_3)
        self.criAn.setGeometry(QtCore.QRect(500, 210, 171, 41))
        self.criAn.setStyleSheet("background-color: rgb(21, 99, 165);\n"
"color: #00ffff;\n"
"font: 14pt \"Berlin Sans FB\";")
        self.criAn.setObjectName("criAn")
        self.caOut = QtWidgets.QLabel(self.widget_3)
        self.caOut.setGeometry(QtCore.QRect(120, 270, 551, 421))
        self.caOut.setStyleSheet("background-color:rgba(0,0,0,50%);\n"
"color:\'white\';")
        self.caOut.setText("")
        self.caOut.setObjectName("caOut")
        self.verticalLayout_6.addWidget(self.widget_3)
        self.stackedWidget.addWidget(self.page_2)
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.stackedWidget.addWidget(self.widget)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addWidget(self.frame_pages)
        self.verticalLayout.addWidget(self.Content)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Btn_Toggle.setText(_translate("MainWindow", "Métodos"))
        self.cripAn.setText(_translate("MainWindow", "CRIPTANÁLISIS"))
        self.ciDes.setText(_translate("MainWindow", "CIFRADO/DESCIFRADO"))
        self.decr.setText(_translate("MainWindow", "DESENCRIPTAR"))
        self.encr.setText(_translate("MainWindow", "ENCRIPTAR"))
        self.criAn.setText(_translate("MainWindow", "CRIPTANALIZAR"))
