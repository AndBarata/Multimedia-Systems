from PyQt5.QtWidgets import QMainWindow, QPushButton
from PyQt5 import uic
from main import resource_path

class Ui_initialWindow(QMainWindow):
    def __init__(self):
        super(Ui_initialWindow, self).__init__()

        # Load .ui file
        uic.loadUi(resource_path("./guiPages/initialWindow.ui"), self)

        # Define Widgets
        self.startButton = self.findChild(QPushButton, "startButton")
        self.aboutButton = self.findChild(QPushButton, "aboutButton")

        # Define Functions
        self.startButton.clicked.connect(self.startButtonClicked)
        self.aboutButton.clicked.connect(self.aboutButtonClicked)
    
        # Show Window
        self.show()
    
    def startButtonClicked(self):
        from mainWindowController import Ui_MainWindow

        # Opens the main window
        self.mainWindow = Ui_MainWindow(self)
        self.close()

    def aboutButtonClicked(self):
        from aboutPopUpController import Ui_aboutWindow

        # Opens the about window
        self.aboutWindow = Ui_aboutWindow()
