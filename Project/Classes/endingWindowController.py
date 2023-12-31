from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel
from PyQt5 import uic, QtGui
from main import resource_path

class Ui_endingWindow(QMainWindow):
    def __init__(self, initialWindow):
        super(Ui_endingWindow, self).__init__()
        # Define Variables
        self.stars = 0

        # Load .ui file
        uic.loadUi(resource_path("./guiPages/endingWindow.ui"), self)

        # Define Widgets
        self.logoButton = self.findChild(QPushButton, "logoButton")
        self.downloadButton = self.findChild(QPushButton, "downloadButton")
        self.emailButton = self.findChild(QPushButton, "emailButton")
        self.star1 = self.findChild(QPushButton, "star1")
        self.star2 = self.findChild(QPushButton, "star2")
        self.star3 = self.findChild(QPushButton, "star3")
        self.star4 = self.findChild(QPushButton, "star4")
        self.star5 = self.findChild(QPushButton, "star5")

        # Define Functions
        self.logoButton.clicked.connect(lambda: self.logoButtonPressed(initialWindow))
        self.downloadButton.clicked.connect(self.downloadButtonPressed)
        self.emailButton.clicked.connect(self.emailButtonPressed)
        self.star1.clicked.connect(self.star1Pressed)
        self.star2.clicked.connect(self.star2Pressed)
        self.star3.clicked.connect(self.star3Pressed)
        self.star4.clicked.connect(self.star4Pressed)
        self.star5.clicked.connect(self.star5Pressed)
        
        # Show Window
        self.show()

    def logoButtonPressed(self, initialWindow):
        initialWindow.show()
        self.close()

    def downloadButtonPressed(self):
        from downloadPopUpController import Ui_downloadWindow
        self.downloadWindow = Ui_downloadWindow()

    def emailButtonPressed(self):
        from emailPopUpController import Ui_emailWindow
        self.emailWindow = Ui_emailWindow()

    def star1Pressed(self):
        # Zero starts to one star
        if self.stars < 1:
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(resource_path(resource_path("./images/starYellow.jpg"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.star1.setIcon(icon)
                self.stars = 1

        # One star to zero stars
        elif self.stars == 1:
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(resource_path("./images/starWhite.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.star1.setIcon(icon)
                self.stars = 0
        
        # several stars to one star
        else :
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(resource_path("./images/starWhite.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.star2.setIcon(icon)
                self.star3.setIcon(icon)
                self.star4.setIcon(icon)
                self.star5.setIcon(icon)
                self.stars = 1

    def star2Pressed(self):
        if self.stars < 2:
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(resource_path("./images/starYellow.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.star1.setIcon(icon)
                self.star2.setIcon(icon)
                self.stars = 2

        elif self.stars == 2:
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(resource_path("./images/starWhite.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.star1.setIcon(icon)
                self.star2.setIcon(icon)
                self.stars = 0
        
        else :
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(resource_path("./images/starWhite.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.star3.setIcon(icon)
                self.star4.setIcon(icon)
                self.star5.setIcon(icon)
                self.stars = 2

    def star3Pressed(self):
        if self.stars < 3:
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(resource_path("./images/starYellow.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.star1.setIcon(icon)
                self.star2.setIcon(icon)
                self.star3.setIcon(icon)
                self.stars = 3

        elif self.stars == 3:
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(resource_path("./images/starWhite.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.star1.setIcon(icon)
                self.star2.setIcon(icon)
                self.star3.setIcon(icon)
                self.stars = 0
        
        else :
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(resource_path("./images/starWhite.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.star4.setIcon(icon)
                self.star5.setIcon(icon)
                self.stars = 3 

    def star4Pressed(self):
        if self.stars < 4:
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(resource_path("./images/starYellow.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.star1.setIcon(icon)
                self.star2.setIcon(icon)
                self.star3.setIcon(icon)
                self.star4.setIcon(icon)
                self.stars = 4

        elif self.stars == 4:
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(resource_path("./images/starWhite.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.star1.setIcon(icon)
                self.star2.setIcon(icon)
                self.star3.setIcon(icon)
                self.star4.setIcon(icon)
                self.stars = 0
        else:
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(resource_path("./images/starWhite.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.star5.setIcon(icon)
                self.stars = 4

    def star5Pressed(self):
        if self.stars < 5:
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(resource_path("./images/starYellow.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.star1.setIcon(icon)
                self.star2.setIcon(icon)
                self.star3.setIcon(icon)
                self.star4.setIcon(icon)
                self.star5.setIcon(icon)
                self.stars = 5
        else:
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(resource_path("./images/starWhite.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.star1.setIcon(icon)
                self.star2.setIcon(icon)
                self.star3.setIcon(icon)
                self.star4.setIcon(icon)
                self.star5.setIcon(icon)
                self.stars = 0