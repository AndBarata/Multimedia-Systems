import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QTextEdit, QBoxLayout, QVBoxLayout
from PyQt6.QtGui import QIcon, QFont
from PyQt6 import uic

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('demo.ui', self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myApp = MyApp()
    myApp.show()
    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing Window...')