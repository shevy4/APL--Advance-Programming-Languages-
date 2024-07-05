import sys
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic
from Tokenize import tokenize
from Syntax import parse
from Evaluate import evaluate
from AI_Analysis import Analyze


class GUI(QMainWindow):

    def __init__(self):
        super(GUI, self).__init__()
        uic.loadUi('Final_Gui.ui', self)
        self.show()
        self.data = None
        self.pushButton.clicked.connect(self.compute)

    def compute(self):
        self.data = self.textEdit.toPlainText()
        self.textEdit_2.setEnabled(True)
        data = self.data.replace('(', '').replace(')', '')
        print("Code = ", data.strip())
        tokens = tokenize(data)
        parsed_result = parse(data)
        if 'Parser error' in parsed_result:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText(parsed_result)
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.buttonClicked.connect(self.restart_app)  # Connect to the restart_app method
            msg.exec_()
            return

        print(parsed_result)
        result, steps = evaluate(parsed_result)
        output = "Steps : \n"
        for _ in range(len(steps)):
            output = output + steps[_] + '\n'
        output = output + '\nResult : ' + result
        self.textEdit.clear()
        self.textEdit.setPlainText(output)
        response = Analyze(output, data)
        self.textEdit_2.setPlainText(response)

    def restart_app(self):
        # Close the current window
        self.close()
        # Reopen a new instance of the GUI
        self.new_window = GUI()
        self.new_window.show()


app = QApplication([])
window = GUI()
app.exec_()
