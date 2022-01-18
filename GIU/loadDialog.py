from PyQt5.QtWidgets import QDialog, QLabel
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QSize, Qt


class loadDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.create_animation()

    def create_animation(self):
        self.label_animation = QLabel(self)
        self.label_animation.setFixedSize(300, 300)
        self.loading_anim = QMovie("loading.gif")
        self.loading_anim.setScaledSize(QSize(300, 300))
        self.label_animation.setMovie(self.loading_anim)
        self.loading_anim.start()
