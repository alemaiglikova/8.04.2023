from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QPushButton
from PyQt6.uic import loadUi

class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        loadUi('form.ui', self)

    def number_click(self):
        button = self.sender()
        self.display.setText(self.display.text() + button.text())

    def operator_click(self):
        button = self.sender()
        self.result = float(self.display.text())
        self.operator = button.text()
        self.display.setText("")

    def equal_click(self):
        if self.operator == "+":
            result = self.result + float(self.display.text())
        elif self.operator == "-":
            result = self.result - float(self.display.text())
        elif self.operator == "*":
            result = self.result * float(self.display.text())
        elif self.operator == "/":
            result = self.result / float(self.display.text())
        self.display.setText(str(result))

    def clear_click(self):
        self.display.setText("")

        app = QApplication([])
        widget = Calculator()
        widget.show()
        app.exec()