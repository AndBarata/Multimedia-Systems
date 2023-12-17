from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class PerfectPitch():
    def __init__(self):
        self.a_number = "A4"

    def startInitialWindow(self):
        from initialWindowController import Ui_initialWindow
        app = QtWidgets.QApplication(sys.argv)
        self.initialWindow = QtWidgets.QMainWindow()
        self.ui = Ui_initialWindow()
        self.ui.setupUi(self.initialWindow)
        self.initialWindow.show()
        sys.exit(app.exec_())
