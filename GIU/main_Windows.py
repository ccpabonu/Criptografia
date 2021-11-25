import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from cripConve import *
class main_Windows(QMainWindow):

    def __init__(self):
        super(main_Windows, self).__init__()
        uic.loadUi("mainWin.ui", self)
        self.bCripClasica.clicked.connect(self.abrir)


    def abrir (self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui=Ui_cripConve()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = main_Windows()
    GUI.show()
    sys.exit(app.exec())