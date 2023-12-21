from PyQt5.QtWidgets import QApplication
import sys
from ProcessingManager import ProcessingManager
from MusicSheetManager import MusicSheetManager
import threading

class PerfectPitch():
    def __init__(self):
        self.processingManager = ProcessingManager()
        self.musicSheetManager = MusicSheetManager(self.processingManager)


    def startInitialWindow(self):
        from initialWindowController import Ui_initialWindow

        app = QApplication(sys.argv)
        window = Ui_initialWindow()
        app.exec_()

        


        