from PyQt5.QtWidgets import QApplication
import sys
from ProcessingManager import ProcessingManager
from MusicSheetManager import MusicSheetManager
import threading
import queue

class PerfectPitch():
    def __init__(self):
        self.processingManager = ProcessingManager()
        self.musicSheetManager = MusicSheetManager(self.processingManager)
        self.note_queue = None


    def startInitialWindow(self):
        from initialWindowController import Ui_initialWindow

        app = QApplication(sys.argv)
        window = Ui_initialWindow()
        app.exec_()

    def startRecording(self):
        audio_queue = queue.Queue()
        self.note_queue = queue.Queue()

        self.event = threading.Event()
        self.stop_threads = threading.Event()
        
        self.audio_thread = threading.Thread(target=self.processingManager.microphone.acquireAudio, args=(audio_queue, self.event, self.stop_threads))
        self.processing_thread = threading.Thread(target=self.processingManager.processSegment, args=(audio_queue, self.note_queue, self.event, self.stop_threads))

        self.audio_thread.start()
        self.processing_thread.start()

    def stopRecording(self):
        print("Here")
        self.stop_threads.set()  # Sinalizando para as threads que é hora de parar
