from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from main import resource_path

class Ui_aboutWindow(QMainWindow):
    def __init__(self):
        super(Ui_aboutWindow, self).__init__()

        # Load .ui file
        uic.loadUi(resource_path("./guiPages/aboutPopUp.ui"), self)

        # Show Window
        self.show()
