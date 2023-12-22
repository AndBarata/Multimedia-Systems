from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel
from PyQt5 import uic, QtGui, QtCore
from main import resource_path, perfectPitch
import threading
import numpy as np

class Ui_MainWindow(QMainWindow):
    def __init__(self, initialWindow):
        super(Ui_MainWindow, self).__init__()
        ####################### /DELETE it's for testing/ #######################
        freq = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 500, 570, 620] # C4, D4, E4, F4, G4, A4, B4
        for i in range(0, 9):
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
        self.yStartNote = 230 # y coordinate when note is on C line
        self.yStep = 7
        self.xStartNote = 100 # x coordinate of the 1st note
        self.xStep = 50
        self.notesDisplay = [] # Contains notas as a lable from the gui

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

        # Define Timer
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(lambda: self.updateSheet(perfectPitch.musicSheetManager.sheet))
        # Set the App
        self.show()

    def clearSheetButtonPressed(self):
        perfectPitch.musicSheetManager.clearSheet()
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
        perfectPitch.musicSheetManager.clearSheet()
        initialWindow.show()

        self.close()

    def microphoneButtonPressed(self):
        if self.recordingLabel.text() == "Recording": # If recording, stops recording
            self.recordingLabel.setText("Not recording")
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(resource_path("./images/microoff.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.microphoneButton.setIcon(icon1)
            self.timer.stop()
            perfectPitch.stopRecording()

        else : # If not recording, star recording
            self.recordingLabel.setText("Recording")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(resource_path("./images/microon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.microphoneButton.setIcon(icon)

            # TODO : Init record thread, when finished signals processing thread
            
            # TODO : Init processing thread when finished signals display thread

            self.timer.start(int(np.floor(perfectPitch.musicSheetManager.getUpdateFrequency()*1000)))
            perfectPitch.startRecording()


    def updateSheet(self, musicSheet):
        for note in self.notesDisplay:
            note.hide()
        
        self.notesDisplay = []
        for i, note in enumerate(musicSheet.getNotes()):
            newNote = self.noteOnGui(note, i)
            self.notesDisplay.append(newNote)
            self.notesDisplay[i].show()
                    
            
    def noteOnGui(self, note, i):
        yCor = self.fromNoteToCoordinates(note.getPitch())
        xCor = self.xStartNote + i*self.xStep
        note = QLabel(self.mainWindowFrame)
        note.setGeometry(QtCore.QRect(xCor, yCor, 70, 137))
        note.setText("")
        note.setPixmap(QtGui.QPixmap(resource_path("./images/seminima1.png")))
        note.setScaledContents(True)
        note.setObjectName("note1")
        note.setStyleSheet("background: none;")
        note.lower()

        return note
        


    def fromNoteToCoordinates(self, noteNumber):
        name = perfectPitch.musicSheetManager.pitchList[noteNumber][0:2]
        # swich case
        if name == "dó":
            y = 7
        elif name == "ré":
            y = 1
        elif name == "mi":
            y = 2
        elif name == "fá":
            y = 3
        elif name == "so":
            y = 4
        elif name == "lá":
            y = 5
        elif name == "si":
            y = 6
        else:
            y = None
        
        
        return self.yStartNote - y*self.yStep