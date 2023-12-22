from PyQt5.QtWidgets import QMainWindow, QTextEdit
from PyQt5 import uic
from main import resource_path, perfectPitch

class Ui_emailWindow(QMainWindow):
    def __init__(self):
        super(Ui_emailWindow, self).__init__()

        # Load .ui file
        uic.loadUi(resource_path("./guiPages/emailPopUp.ui"), self)

        # Show Window
        self.show()
        
        ##Define widgets
        
        self.emailText = self.findChild(QTextEdit, "emailText")
        
        self.sendButton.clicked.connect(self.sendButtonPressed)
        
    def sendButtonPressed(self):
        email = self.emailText.toPlainText()
        self.close()
        perfectPitch.musicSheetManager.sendEmail(email)
        
        
        