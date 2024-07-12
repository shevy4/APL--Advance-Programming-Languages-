from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic
from Tokenize import tokenize
from Syntax import parse
from Evaluate import evaluate
from AI_Analysis import Analyze


class GUI(QMainWindow):
    # Initialize the GUI
    def __init__(self):
        super(GUI, self).__init__()
        uic.loadUi('Final_Gui.ui', self)
        self.show()
        self.data = None
        # Connect the compute method to the button click event
        self.pushButton.clicked.connect(self.compute)

    # Get input from the text edit field
    def compute(self):
        self.data = self.textEdit.toPlainText()
        self.textEdit_2.setEnabled(True)
        data = self.data.replace('(', '').replace(')', '')
        print("Code = ", data.strip())

        # Tokenize the input data
        tokens = tokenize(data)
        print("Tokens :", tokens)

        # Parse the tokenized data
        parsed_result = parse(data)
        print("parsed result :", parsed_result)

        if 'Parser error' in parsed_result:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText(parsed_result)
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            # Connect to the restart_app method
            msg.buttonClicked.connect(self.restart_app)
            msg.exec_()
            return

        # Evaluate the parsed result
        result, steps = evaluate(parsed_result)

        # Prepare the output to display
        output = "Input : " + data + "\nSteps : \n"

        for _ in range(len(steps)):
            output = output + steps[_] + '\n'
        output = output + '\nResult : ' + str(result)
        self.textEdit.clear()
        self.textEdit.setPlainText(output)

        # Analyze the output using AI
        response = Analyze(output, data)
        self.textEdit_2.setPlainText(response)

    # Restart window
    def restart_app(self):
        # Close the current window
        self.close()
        # Reopen a new instance of the GUI
        self.new_window = GUI()
        self.new_window.show()


# Initialize and run the application
app = QApplication([])
window = GUI()
app.exec_()
