from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel
from PyQt5 import uic, QtGui
from main import resource_path

class Ui_MainWindow(QMainWindow):
    def __init__(self, initialWindow):
        super(Ui_MainWindow, self).__init__()
        
        # Load .ui file
        uic.loadUi(resource_path("./guiPages/mainWindowNotRecording.ui"), self)

        # Define Widgets
        self.clearSheetButton = self.findChild(QPushButton, "clearSheetButton")
        self.defenitionsButton = self.findChild(QPushButton, "defenitionsButton")
        self.exportButton = self.findChild(QPushButton, "exportButton")
        self.logoButton = self.findChild(QPushButton, "logoButton")
        self.microphoneButton = self.findChild(QPushButton, "microphoneButton")
        self.recordingLabel = self.findChild(QLabel, "recordingLabel")

        # Define Functions
        self.clearSheetButton.clicked.connect(self.clearSheetButtonPressed)
        self.defenitionsButton.clicked.connect(self.defenitionsButtonPressed)
        self.logoButton.clicked.connect(lambda: self.logoButtonPressed(initialWindow))
        self.microphoneButton.clicked.connect(self.microphoneButtonPressed)
        self.exportButton.clicked.connect(lambda: self.exportButtonPressed(initialWindow))


        #Set the App
        self.show()

    def clearSheetButtonPressed(self):
        # TODO Clear the sheet
        pass

    def defenitionsButtonPressed(self):
        from definitionPopUpController import Ui_DefWindow
        self.defWindow = Ui_DefWindow()

    def exportButtonPressed(self, initialWindow):
        from endingWindowController import Ui_endingWindow
        # Opens the ending window
        self.endWindow = Ui_endingWindow(initialWindow)
        self.close()


    def logoButtonPressed(self, initialWindow):
        initialWindow.show()
        self.close()

    def microphoneButtonPressed(self):
        
        if self.recordingLabel.text() == "Recording": # If recording, stops recording
            self.recordingLabel.setText("Not recording")
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(resource_path("./images/microphoneOff.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.microphoneButton.setIcon(icon1)

        else : # If not recording, star recording
            self.recordingLabel.setText("Recording")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(resource_path("./images/microphoneOn.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.microphoneButton.setIcon(icon)




