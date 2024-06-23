from PyQt5.QtWidgets import *
from PyQt5 import uic


class GUI(QMainWindow):

    def __init__(self):
        super(GUI, self).__init__()
        uic.loadUi('temp.ui', self)
        self.show()
        self.data = None
        self.pushButton.clicked.connect(self.compute)

    def compute(self):
        self.data = self.textEdit.toPlainText()
        self.close()


def Run_GUI():
    app = QApplication([])
    window = GUI()
    app.exec_()
    return window.data
