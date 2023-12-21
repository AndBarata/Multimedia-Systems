from PyQt5.QtWidgets import QMainWindow, QPushButton
from PyQt5 import uic
from main import resource_path
from main import perfectPitch

class Ui_downloadWindow(QMainWindow):
    def __init__(self):
        super(Ui_downloadWindow, self).__init__()

        # Load .ui file
        uic.loadUi(resource_path("./guiPages/downloadPopUp.ui"), self)

        # Define Widgets
        self.finishButton = self.findChild(QPushButton, "finishButton")

        # Define Functions
        self.finishButton.clicked.connect(self.finishButtonPressed)
        
        # Show Window
        self.show()

        # Actions
        perfectPitch.musicSheetManager.downloadSheetTxt()
        
    def finishButtonPressed(self):
        self.close()