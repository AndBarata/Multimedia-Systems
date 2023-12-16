from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import initPageController
class PerfectPitch(QtWidgets):
    userName = "ahahah"
    
    def __init__(self, argv):
        super().__init__(argv)
        self.perfectPitch = QMainWindow()
        self.window = initPageController.Ui_MainWindow()
        self.window.setupUi(self.perfectPitch, )
        self.perfectPitch.show()