from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from main import resource_path, perfectPitch

class Ui_emailWindow(QMainWindow):
    def __init__(self):
        super(Ui_emailWindow, self).__init__()

        # Load .ui file
        uic.loadUi(resource_path("./guiPages/emailPopUp.ui"), self)

        # Show Window
        self.show()

        perfectPitch.musicSheetManager.sendEmail()