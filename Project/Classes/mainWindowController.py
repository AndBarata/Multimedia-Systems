from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel
from PyQt5 import uic, QtGui, QtCore
from main import resource_path, perfectPitch


class Ui_MainWindow(QMainWindow):


    def __init__(self, initialWindow):
        super(Ui_MainWindow, self).__init__()
        
        ####################### /DELETE it's for testing/ #######################
        freq = [261.63, 293.66, 329.63, 349.23, 392.00]
        for i in range(0, 5):
            noteNumber = perfectPitch.processingManager.calculatePitch(freq[i])
            musicNote = perfectPitch.processingManager.createMusicNote(
                noteNumber,
                "",
                0,
                125,
                0,
                44100,
                1
            )
            perfectPitch.musicSheetManager.addMusicNote(musicNote)

        ####################### // #######################


        # Define Variables
        self.yStartNote = 232 # y coordinate when note is on C line
        self.yStep = 7
        self.xStartNote = 100 # x coordinate of the 1st note
        self.xStep = 50

        # Load .ui file
        uic.loadUi(resource_path("./guiPages/mainWindow.ui"), self)

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
        self.updateSheet(perfectPitch.musicSheetManager.sheet)

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

    def updateSheet(self, musicSheet):
        for i, note in enumerate(musicSheet.getNotes()):
            self.placeNoteOnSheet(note, i)
           

    def placeNoteOnSheet(self, note, i):
        yCor = self.fromNoteToCoordinates(note.getPitch())
        xCor = self.xStartNote + i*self.xStep
        note = QLabel(self.mainWindowFrame)
        note.setGeometry(QtCore.QRect(xCor, yCor, 70, 137))
        note.setText("")
        note.setPixmap(QtGui.QPixmap(resource_path("./images/seminima1.png")))
        note.setScaledContents(True)
        note.setObjectName("note1")
        note.lower()
        note.show()


    def fromNoteToCoordinates(self, noteNumber):
        name = perfectPitch.musicSheetManager.pitchList[noteNumber][0:2]
        print("DEGUB: name: ", name)
        # swich case
        if name == "dó":
            y = 1
        elif name == "ré":
            y = 2
        elif name == "mi":
            y = 3
        elif name == "fa":
            y = 4
        elif name == "so":
            y = 5
        elif name == "la":
            y = 6
        elif name == "si":
            y = 9
        else:
            y = 0

        return self.yStartNote - y*self.yStep